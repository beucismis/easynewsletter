from redmail import EmailSender


class Email:
    def __init__(
        self, user_name: str, password: str, host: str = "localhost", port: int = 1
    ):
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port

        self.email_sender = EmailSender(
            user_name=user_name,
            password=password,
            host=host,
            port=port,
        )

    def send(self, **kwargs) -> None:
        self.email_sender.send(kwargs)
