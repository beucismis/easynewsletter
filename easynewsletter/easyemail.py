from redmail import EmailSender


class Message:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

        self.cc = kwargs.get("cc", None)
        self.bcc = kwargs.get("bcc", None)
        self.html = kwargs.get("html", None)
        self.text = kwargs.get("text", None)
        self.sender = kwargs.get("sender", None)
        self.subject = kwargs.get("subject", None)
        self.receivers = kwargs.get("receivers", None)
        self.body_images = kwargs.get("body_images", None)
        self.body_tables = kwargs.get("body_tables", None)
        self.body_params = kwargs.get("body_params", None)
        self.attachments = kwargs.get("attachments", None)
        self.html_template = kwargs.get("html_template", None)
        self.text_template = kwargs.get("text_template", None)


class Email(EmailSender):
    def __init__(
        self, user_name: str, password: str, host: str = None, port: int = None
    ):
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port

        super().__init__(user_name=user_name, password=password, host=host, port=port)

    def __repr__(self) -> str:
        return f"<Email(user_name={self.user_name}, password={len(self.password)*'*'}, host={self.host}, port={self.port})>"

    def fly_email(self, message: Message) -> None:
        self.send(**message.__dict__)
