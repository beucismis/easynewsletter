from redmail import EmailSender


class Message(object):
    """Class that stores message information.

    Parameters
    ----------
    subject : str
        Subject of the email.
    sender : str, optional
        Email address the email is sent from.
    receivers : list, optional
        Receivers of the email.
    cc : list, optional
        Cc or Carbon Copy of the email.
    bcc : list, optional
        Blind Carbon Copy of the email.
    html : str, optional
        HTML body of the email.
    text : str, optional
        Text body of the email.
    html_template : str, optional
        Name of the HTML template loaded using Jinja.
    text_template : str, optional
        Name of the text template loaded using Jinja.
    body_images : dict of bytes, dict of path-like, dict of plt Figure, dict of PIL Image, optional
        HTML images to embed with the html.
    body_tables : dict of Pandas dataframes, optional
        HTML tables to embed with the html.
    body_params : dict, optional
        Extra Jinja parameters passed to the HTML and text bodies.
    attachments : dict, optional
        Attachments of the email. If dict value is string, the attachment content is the string itself.
    """

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(**kwargs)

        self.subject = kwargs.get("subject", None)
        self.sender = kwargs.get("sender", None)
        self.receivers = kwargs.get("receivers", None)
        self.cc = kwargs.get("cc", None)
        self.bcc = kwargs.get("bcc", None)
        self.html = kwargs.get("html", None)
        self.text = kwargs.get("text", None)
        self.html_template = kwargs.get("html_template", None)
        self.text_template = kwargs.get("text_template", None)
        self.body_images = kwargs.get("body_images", None)
        self.body_tables = kwargs.get("body_tables", None)
        self.body_params = kwargs.get("body_params", None)
        self.attachments = kwargs.get("attachments", None)


class Email(EmailSender):
    """Email Class based on Red Mail.

    Parameters
    ----------
    user_name : str
        User name to authenticate on the server.
    password : str
        User password to authenticate on the server.
    host : str
        SMTP host address.
    port : int
        Port to the SMTP server.
    """

    def __init__(self, user_name: str, password: str, host: str, port: int):
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port

        super().__init__(user_name=user_name, password=password, host=host, port=port)

    def __repr__(self) -> str:
        return f"<Email(user_name={self.user_name}, password={len(self.password)*'*'}, host={self.host}, port={self.port})>"

    def fly(self, message: Message) -> None:
        self.send(**message.__dict__)
