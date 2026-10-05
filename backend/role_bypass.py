def allow_write(role: str) -> bool:
    return role in {"writer"}

def should_show_form(can_write: bool) -> bool:
    return bool(can_write)

def zero_dirt_on_reject() -> bool:
    return True
