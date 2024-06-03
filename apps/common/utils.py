import datetime


def make_password(password, salt=None, hasher="default") -> str:
    # actions to make password hash
    return "hashed_password"


def check_password(password: str, encoded: ..., setter=None, preferred="default") -> bool:
    # actions to check password
    return True


def get_default_event_date() -> datetime.datetime: ...
