# biliass

Danmaku2ASS 的 bilili 与 yutto 适配版

原版：<https://github.com/m13253/danmaku2ass>

支持 XML 弹幕和 Protobuf 弹幕

# Install

```bash
pip install biliass
```

# Usage

```bash
# XML 弹幕
biliass danmaku.xml -s 1920x1080 -o danmaku.ass
# protobuf 弹幕
biliass danmaku.protobuf -s 1920x1080 -f protobuf -o danmaku.ass
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
