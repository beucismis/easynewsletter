import time
import util


class Subscriber:
    def __init__(self, email: str, active: bool = True):
        self.email = email
        self.active = active
        self.id = util.generate_id(email)
        self.created = time.strftime("%Y-%m-%d %H:%M:%S")

        if not util.is_email(email):
            raise util.InvalidMail()

    def __repr__(self) -> str:
        return f"<Subscriber(email={self.email}, active={self.active}, id={self.id}), created={self.created}>"

    def user_name(self) -> str:
        return self.email.split("@")[0]

    def domain(self) -> str:
        return self.email.split("@")[1]

    def to_tuple(self) -> tuple:
        return (self.email, self.active, self.id, self.created)
