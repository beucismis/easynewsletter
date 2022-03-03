import time
from . import util


class Subscriber(object):
    """The subscriber class is for managing subscribers.

    Parameters
    ----------
    email : str
        Email address of subscriber.
    active : bool
        Activity status of subscriber.
    """

    def __init__(self, email: str, active: bool = True):
        self.email = email
        self.active = active
        self.id = util.generate_id(email)
        self.created = time.strftime("%Y-%m-%d %H:%M:%S")

        if not util.is_email(email):
            raise util.InvalidEmail()

    def __repr__(self) -> str:
        return f"<Subscriber(email={self.email}, active={self.active}, id={self.id}), created={self.created}>"

    def user_name(self) -> str:
        """Returns the name of the subscriber.

        Returns
        -------
        str
            Name of the subscriber.
        """

        return self.email.split("@")[0]

    def domain(self) -> str:
        """Returns the domain of the subscriber.

        Returns
        -------
        str
            Name of the domain.
        """

        return self.email.split("@")[1]

    def to_tuple(self) -> tuple:
        """Returns subscriber information as a tuple.

        Returns
        -------
        tuple
            Subscriber informations.
        """

        return (self.email, self.active, self.id, self.created)
