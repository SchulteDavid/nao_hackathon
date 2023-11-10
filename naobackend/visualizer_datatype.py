import io
import struct


def read_string(fp: io.BufferedIOBase) -> str:
    vs_len = read_int(fp)
    s = struct.unpack("<" + str(vs_len) + "s", fp.read(vs_len))[0]
    return s.decode("iso8859-1")


def write_string(fp: io.BytesIO, s: str):
    write_int(fp, len(s))
    fp.write(struct.pack(str(len(s)) + "s", bytes(s, 'iso8859-1')))


def read_int(fp: io.BufferedIOBase) -> int:
    return struct.unpack("<i", fp.read(4))[0]


def write_int(fp: io.BytesIO, v: int):
    fp.write(struct.pack("<i", v))


def read_short(fp: io.BufferedIOBase) -> int:
    return struct.unpack("<h", fp.read(2))[0]


def write_short(fp: io.BytesIO, v: int):
    fp.write(struct.pack("<h", v))


def read_byte(fp: io.BufferedIOBase) -> int:
    return struct.unpack("<B", fp.read(1))[0]


def write_byte(fp: io.BytesIO, v: int):
    fp.write(struct.pack("<B", v))


def read_float(fp: io.BufferedIOBase) -> float:
    return struct.unpack("<f", fp.read(4))[0]


def write_float(fp: io.BytesIO, v: float):
    fp.write(struct.pack("<f", v))
