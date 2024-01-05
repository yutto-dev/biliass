from __future__ import annotations

from biliass import ReadCommentsBilibiliProtobuf


def test_protobuf():
    with open("./tests/test_files/test.pb", "rb") as f:
        ReadCommentsBilibiliProtobuf(f.read(), 10)
