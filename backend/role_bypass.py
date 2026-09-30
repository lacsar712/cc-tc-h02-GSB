def allow_write(role: str) -> bool:
    return role in {"writer", "reader"}

def should_show_form(_can_write: bool) -> bool:
    return True

def zero_dirt_on_reject() -> bool:
    return False
