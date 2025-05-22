import asyncio
import tornado
import os
import subprocess
import uuid
from sqlalchemy import String, create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
import json
import shutil
from typing import List
import sys
import pycmarkgfm
import markdown

NEXT_PORT=9000

RUNNING_CONTAINERS = []
CONFIG = {}

class Base(DeclarativeBase):
    pass

class Container(Base):
    __tablename__ = "container"

    id: Mapped[int] = mapped_column(primary_key=True)
    docker_id: Mapped[str] = mapped_column(String(128))
    port: Mapped[int] = mapped_column()
    host_dir: Mapped[str] = mapped_column(String(256))

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_uuid: Mapped[str] = mapped_column(String(128))
    current_container_id: Mapped[int] = mapped_column(ForeignKey("container.id"))
    current_container: Mapped["Container"] = relationship()
    root_dir: Mapped[str] = mapped_column(String(256))

def connect_to_db():
    engine = create_engine("sqlite:///containers.db")
    Base.metadata.create_all(engine)

    return Session(engine)
    
def start_jupyter_container(session: Session, root_dir:str="/home/david/Documents/nao_hackathon"):
    global NEXT_PORT

    host_dir = root_dir
    
    proc = subprocess.Popen(["docker", "run", "--rm", "-it", "-p", "8888", "-v", f"{host_dir}:/mnt/notebooks", "-d", "htwk-robots:hackathon"], stdout=subprocess.PIPE)
    docker_id = proc.stdout.readline().decode('utf-8').strip()
    print(docker_id, NEXT_PORT)
    NEXT_PORT = NEXT_PORT + 1

    RUNNING_CONTAINERS.append(docker_id)

    proc2 = subprocess.Popen(["docker", "inspect", docker_id], stdout=subprocess.PIPE)
    proc2.wait()
    container_data = json.load(proc2.stdout)

    host_port = int(container_data[0]['NetworkSettings']['Ports']['8888/tcp'][0]['HostPort'])

    container = Container(docker_id=docker_id, port=host_port, host_dir=host_dir)

    session.add_all([container])
    
    return container
    

def get_jupyter_container(session: Session, docker_id: str) -> Container | None:
    stmt = select(Container).where(Container.docker_id == docker_id)
    containers = list(session.scalars(stmt))
    if len(containers) > 0:
        return containers[0]
    return None


def create_user(session: Session) -> User:
    user_uuid = str(uuid.uuid4())

    root_dir = os.path.join(CONFIG["root-dir"], user_uuid)

    shutil.copytree(os.path.join(CONFIG["origin-dir"], "Beginner"), os.path.join(root_dir, "Beginner"))
    shutil.copytree(os.path.join(CONFIG["origin-dir"], "Intermediate"), os.path.join(root_dir, "Intermediate"))
    shutil.copytree(os.path.join(CONFIG["origin-dir"], "Advanced"), os.path.join(root_dir, "Advanced"))
    shutil.copytree(os.path.join(CONFIG["origin-dir"], "data"), os.path.join(root_dir, "data"))
    shutil.copytree(os.path.join(CONFIG["origin-dir"], "images"), os.path.join(root_dir, "images"))
    
    container = start_jupyter_container(session, root_dir=root_dir)
    user = User(user_uuid=user_uuid, current_container=container, root_dir=root_dir)
    session.add_all([user])
    session.commit()
    return user

def get_user(session: Session, user_uuid: str) -> User | None:
    stmt = select(User).where(User.user_uuid == user_uuid)
    users = list(session.scalars(stmt))
    if len(users) > 0:
        return users[0]
    return None

def container_running(container: Container) -> bool:
    proc = subprocess.Popen(["docker", "inspect", "-f", "{{.State.Running}}", container.docker_id], stdout=subprocess.PIPE)
    return proc.stdout.readline().decode('utf-8').strip() == "true"

def list_containers(session: Session) -> List[Container]:
    stmt = select(Container)
    return session.scalars(stmt)

def stop_containers():
    session = connect_to_db()
    for c in list_containers(session):
        proc = subprocess.Popen(["docker", "kill", c.docker_id])
        proc.wait()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #loader = tornado.template.Loader("templates/")
        #template = loader.load("index.html")
        #self.write(template.generate(user_id=self.get_cookie("user-id")))
        self.write(open("templates/index.html").read())

class JupyterHandler(tornado.web.RequestHandler):

    def get(self):
        docker_id = None
        docker_port = 0
        host_ip = self.request.host.split(':')[0]
        host_port = int(self.request.host.split(':')[1])

        session = connect_to_db()
        
        if not self.get_cookie("user-id"):
            user = create_user(session)
            self.set_cookie("user-id", user.user_uuid, expires_days=364)
        else:
            user = get_user(session, self.get_cookie("user-id"))
            if user is None:
                print(f"No user found for id")
                user = create_user(session)
                session.commit()
                self.set_cookie("user-id", user.user_uuid, expires_days=364)
            if not container_running(user.current_container):
                print(f"Container {user.current_container.docker_id} is not running")
                user.current_container = start_jupyter_container(session, user.root_dir)
                session.commit()

        container = user.current_container
        docker_id = container.docker_id
        docker_port = container.port
        #self.redirect(f"http://{host_ip}:{docker_port}")
        self.write(f'<meta http-equiv="refresh" content="3;url=http://{host_ip}:{host_port}/container/{docker_id}" />')
        self.write(f"<h1>Starting Container and jupyter server...</h1>")

class ContainerHandler(tornado.web.RequestHandler):

    def get(self, docker_id):
        print(f"Redirecting to container {docker_id}")
        session = connect_to_db()
        container = get_jupyter_container(session, docker_id)
        
        host_ip = self.request.host.split(':')[0]

        if container is not None:
            self.redirect(f"http://{host_ip}:{container.port}")
        else:
            self.write("No such container")

class DocumentationHandler(tornado.web.RequestHandler):

    def get(self, path):
        loader = tornado.template.Loader("templates/")
        template = loader.load("doc.html")
        file_path = os.path.join("doc", path)
        md = markdown.Markdown(extensions=['pymdownx.superfences'])
        self.write(template.generate(document=md.convert(open(file_path).read())))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/jupyter", JupyterHandler),
        (r"/container/(.*)?", ContainerHandler),
        (r"/static/(.*)?", tornado.web.StaticFileHandler, {"path": "resources"}),
        (r"/doc/(.*)?", DocumentationHandler)
    ], debug=True)

async def main():
    try:
        app = make_app()
        app.listen(8888)
        await asyncio.Event().wait()
    except:
        print("Ending gracefully")
        stop_containers()

if __name__ == "__main__":

    CONFIG["origin-dir"] = os.path.abspath(sys.argv[1])
    CONFIG["root-dir"] = os.path.abspath(sys.argv[2])
    
    asyncio.run(main())

