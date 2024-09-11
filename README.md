# biliass

> [!NOTE]
>
> biliass has been moved to [yutto-dev/yutto](https://github.com/yutto-dev/yutto/tree/main/packages/biliass).

<p align="center">
   <a href="https://python.org/" target="_blank"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/biliass?logo=python&style=flat-square"></a>
   <a href="https://pypi.org/project/biliass/" target="_blank"><img src="https://img.shields.io/pypi/v/biliass?style=flat-square" alt="pypi"></a>
   <a href="https://pypi.org/project/biliass/" target="_blank"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/biliass?style=flat-square"></a>
   <a href="https://actions-badge.atrox.dev/yutto-dev/biliass/goto?ref=main"><img alt="Build Status" src="https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fyutto-dev%2Fbiliass%2Fbadge%3Fref%3Dmain&style=flat-square&label=Test" /></a>
   <a href="LICENSE"><img alt="LICENSE" src="https://img.shields.io/github/license/yutto-dev/biliass?style=flat-square"></a>
   <a href="https://gitmoji.dev"><img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67?style=flat-square" alt="Gitmoji"></a>
</p>

biliass，只是 Danmaku2ASS 的 bilili 与 yutto 适配版

原版：<https://github.com/m13253/danmaku2ass>

仅支持 bilibili 弹幕，支持 XML 弹幕和 Protobuf 弹幕

## Install

```bash
pip install biliass
```

## Usage

```bash
# XML 弹幕
biliass danmaku.xml -s 1920x1080 -o danmaku.ass
# protobuf 弹幕
biliass danmaku.pb -s 1920x1080 -f protobuf -o danmaku.ass
```

```python
from biliass import Danmaku2ASS

# xml
Danmaku2ASS(
    xml_text_or_bytes,
    width,
    height,
    input_format="xml",
    reserve_blank=0,
    font_face="sans-serif",
    font_size=width / 40,
    text_opacity=0.8,
    duration_marquee=15.0,
    duration_still=10.0,
    comment_filter=None,
    is_reduce_comments=False,
    progress_callback=None,
)

# protobuf
Danmaku2ASS(
    protobuf_bytes, # only bytes
    width,
    height,
    input_format="protobuf",
    reserve_blank=0,
    font_face="sans-serif",
    font_size=width / 40,
    text_opacity=0.8,
    duration_marquee=15.0,
    duration_still=10.0,
    comment_filter=None,
    is_reduce_comments=False,
    progress_callback=None,
)
```

## TODO

- 导出 bilibili 网页上的弹幕设置，并导入到 biliass
