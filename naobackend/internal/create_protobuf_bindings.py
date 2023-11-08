import pathlib
import os
from subprocess import check_call
import sys


def generate_proto_code(protoc: str, proto_interface_dir: str):
    out_folder = "../proto/"
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    proto_it = pathlib.Path(proto_interface_dir).expanduser().glob("**/*.proto")
    protos = list(filter(lambda e: "motion" not in e, [str(proto) for proto in proto_it if proto.is_file()]))
    check_call([protoc] + protos + ["--python_out", "pyi_out:" + out_folder, "--proto_path", proto_interface_dir])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify the directory where the protobufs are stored!")
        sys.exit(1)

    protoc = "protoc"
    src_dir = sys.argv[1]

    if len(sys.argv) == 3:
        protoc = sys.argv[2]

    generate_proto_code(protoc, src_dir)
