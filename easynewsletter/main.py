import util
import schedule

from database import Database
from subscriber import Subscriber
from easyemail import Email, Message


class Newsletter:
    def __init__(self, email: Email, database: Database):
        self.email = email
        self.database = database

        if not util.is_email(email.user_name):
            raise util.InvalidMail()

    def __repr__(self) -> str:
        return f"<Newsletter(email={self.email}, database={self.database})>"

    def add_subscriber(self, subscribers: list[Subscriber]) -> None:
        with self.database as db:
            db.insert([s.to_tuple() for s in subscribers])

    def remove_subscriber(self, subscribers: list[Subscriber]) -> None:
        with self.database as db:
            db.delete(subscribers)

    def add_rule(self, message: Message, schedule: schedule) -> None:
        message.sender = self.email.user_name

        with self.database as db:
            message.receivers = [i[0] for i in db.get("email")]

        schedule.do(self.email.fly_email, message=message)

    def run_pending(self) -> None:
        schedule.run_pending()
