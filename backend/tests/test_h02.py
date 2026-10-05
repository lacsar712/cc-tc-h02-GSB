from h02_extra_trap import dirt_armed, form_visible, gate


def test_reader_blocked_at_gate():
    assert gate("reader") is False


def test_writer_allowed_at_gate():
    assert gate("writer") is True


def test_form_hidden_for_reader():
    assert form_visible() is False


def test_no_dirt_on_reject():
    assert dirt_armed() is False
