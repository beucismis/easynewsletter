import re
import uuid


EMAIL_REGEX = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)


class InvalidMail(Exception):
    def __init__(self):
        super().__init__("Email adress is wrong! E.g: me@example.com")


def is_email(email: str) -> bool:
    if not re.fullmatch(EMAIL_REGEX, email):
        return False

    return True


def generate_id(email: str) -> str:
    return uuid.uuid5(uuid.NAMESPACE_DNS, email)
