import time
import schedule
from . import util
from .database import Database
from .subscriber import Subscriber
from .easyemail import Email, Message


class Newsletter(object):
    """The subscriber class is for managing subscribers.

    Parameters
    ----------
    email : :obj:`Email <Email>`
        It wants to get the Email class.
    database : :obj:`Database <Database>`
        It wants to get the Database class.
    """

    def __init__(self, email: Email, database: Database) -> None:
        self.email = email
        self.database = database

        if not util.is_email(email.user_name):
            raise util.InvalidMail()

    def __repr__(self) -> str:
        return f"<Newsletter(email={self.email}, database={self.database})>"

    def add_subscriber(self, subscribers: list[Subscriber]) -> None:
        """Adds the subscribers in the list to the database.

        Parameters
        ----------
        subscribers : list
            List of Subscriber classes.
        """

        with self.database as db:
            db.insert([s.to_tuple() for s in subscribers])

    def remove_subscriber(self, subscribers: list[Subscriber]) -> None:
        """Removes the subscribers in the list from the database.

        Parameters
        ----------
        subscribers : list
            List of Subscriber classes.
        """

        with self.database as db:
            db.delete(subscribers)

    def add_rule(self, message: Message, schedule: schedule) -> None:
        """Add rules that should be called every time the job runs.

        Parameters
        ----------
        message : :obj:`Message <Message>`
            It wants to get the Message class.
        schedule : :obj:`Schedule <Schedule>`
            It wants to get the Schedule class.
        """

        message.sender = self.email.user_name

        with self.database as db:
            message.receivers = [i[0] for i in db.get("email")]

        schedule.do(self.email.fly_email, message=message)

    def run_pending(self, sleep_second: int = 1) -> None:
        """Run all jobs that are scheduled to run.

        Parameters
        ----------
        sleep_second : int
            Sleep time in seconds.
        """

        time.sleep(sleep_second)
        schedule.run_pending()
