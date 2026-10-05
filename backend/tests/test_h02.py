from h02_extra_trap import dirt_armed, form_visible, gate
from h02_ui_trap import paint_form


def test_reader_write():
    # 巡检（reader）必须被挡住：门禁拒、首页不摊可填区、拒绝后不留空白占位
    assert gate("reader") is False
    assert form_visible() is False
    assert dirt_armed() is False


def test_writer_write():
    # 测量岗（writer）正常放行：可提交、可填区照常摊开
    assert gate("writer") is True
    assert paint_form(True) is True


def test_unknown_role_write():
    assert gate("") is False
    assert gate(None) is False
