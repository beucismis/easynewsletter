import util

from email import Email
from database import Database
from subscriber import Subscriber


class Newsletter:
    def __init__(self, email: str, password: str, database: Database):
        self.email = email
        self.password = password
        self.database = database

        if not util.is_email(user_name):
            raise util.InvalidMail()

    def __repr__(self) -> str:
        return f"<Newsletter(email={self.email}, database={self.database})>"

    def user_name(self) -> str:
        return self.email.split("@")[0]

    def domain(self) -> str:
        return self.email.split("@")[1]

    def add_subscriber(self, subscribers: list[Subscriber]) -> None:
        pass

    def remove_subscriber(self, subscribers: list[Subscriber]) -> None:
        pass

    def subscribers(self) -> list[Subscriber]:
        pass

    def send_email(self, **kwargs) -> None:
        kwargs["sender"] = self.email
        kwargs["receivers"] = "?"

        email = Email(user_name=self.user_name, password=self.password)
        email.send(kwargs)
