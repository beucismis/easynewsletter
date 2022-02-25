import util


class Subscriber:
    def __init__(self, email: str, status: bool = 1):
        self.email = email
        self.status = status
        self.id = util.generate_id(email)
        self.created = None

        if not util.is_email(email):
            raise util.InvalidMail()

    def __repr__(self) -> str:
        return f"<Subscriber(email={self.email}, status={self.status}, id={self.id})>"

    def user_name(self) -> str:
        return self.email.split("@")[0]

    def domain(self) -> str:
        return self.email.split("@")[1]
