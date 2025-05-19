FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y python3-pip libgl-dev libglib2.0-0

COPY requirements.txt .

RUN apt-get install -y python3-venv virtualenv
RUN virtualenv jupyter-env

RUN source jupyter-env/bin/activate && pip install -r requirements.txt
RUN source jupyter-env/bin/activate && pip install jupyter build ipykernel

RUN mkdir -p /root/.jupyter
RUN mkdir -p /naobackend

COPY jupyter_notebook_config.py /root/.jupyter/
COPY naobackend/ /naobackend/

RUN source jupyter-env/bin/activate && cd naobackend && python3 -m build
RUN source jupyter-env/bin/activate && cd naobackend && pip install --force-reinstall ./dist/naobackend-1.0.0-py3-none-any.whl

#RUN python3 -m ipykernel install --user --name=NaoEnv
RUN python3 -c "import naobackend"

CMD source jupyter-env/bin/activate && jupyter notebook --allow-root --NotebookApp.token=''


