from __future__ import annotations

import os

import requests


def gen_xml_v1(base_dir: str):
    filename = "test_v1.xml"
    filepath = os.path.join(base_dir, filename)
    cid = "18678311"
    resp = requests.get(f"http://comment.bilibili.com/{cid}.xml")
    resp.encoding = "utf-8"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(resp.text)


def gen_protobuf(base_dir: str):
    filename = "test.pb"
    filepath = os.path.join(base_dir, filename)
    cid = "18678311"
    resp = requests.get(f"http://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={1}")
    with open(filepath, "wb") as f:
        f.write(resp.content)


def main():
    base_dir = "./tests/test_files"
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir)
    gen_xml_v1(base_dir)
    gen_protobuf(base_dir)


if __name__ == "__main__":
    main()
