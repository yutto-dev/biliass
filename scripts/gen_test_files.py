from __future__ import annotations

import os

import requests

BILIBILI_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
}


def gen_xml_v1(base_dir: str):
    filename = "test_v1.xml"
    filepath = os.path.join(base_dir, filename)
    cid = "18678311"
    resp = requests.get(
        f"http://comment.bilibili.com/{cid}.xml",
        headers=BILIBILI_HEADERS,
    )
    resp.encoding = "utf-8"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(resp.text)


def gen_protobuf(base_dir: str):
    filename = "test.pb"
    filepath = os.path.join(base_dir, filename)
    cid = "18678311"
    resp = requests.get(
        f"http://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={1}",
        headers=BILIBILI_HEADERS,
    )
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
