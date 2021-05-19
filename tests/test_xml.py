from biliass import ReadCommentsBilibiliXml


def test_xml_v1_text():
    with open("./tests/test_files/test_v1.xml", "r") as f:
        ReadCommentsBilibiliXml(f.read(), 10)


def test_xml_v1_bytes():
    with open("./tests/test_files/test_v1.xml", "rb") as f:
        ReadCommentsBilibiliXml(f.read(), 10)
