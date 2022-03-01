# easynewsletter

![](https://img.shields.io/badge/python-3.6%2B-blue)
![](https://img.shields.io/pypi/v/easynewsletter)
![](https://img.shields.io/pypi/dm/easynewsletter)
![](https://readthedocs.org/projects/easynewsletter/badge/?version=latest)
![](https://img.shields.io/github/license/beucismis/easynewsletter)
![](https://img.shields.io/badge/style-black-black)

Newsletter module with customizable, scheduler and self-database. It uses [red-mail](https://github.com/Miksus/red-mail) to send mail and scheduler for [schedule](https://github.com/dbader/schedule).

## Features
- A simple API for blanning newsletters
- Customizable self-database
- Multiple message and scheduler support
- Be used in web applications (E.g: with Flask)
- A cross-platform module
- Tested on Python 3.9

## Installation
To install easynewsletter, run the following command from the command line:

```shell
pip3 install --user easynewsletter
```

## Example
This example sends the "Science Weekly" newsletter to Tesla and Feynman every Monday.

```python
import easynewsletter as enl
  
  
root = enl.Newsletter(
	enl.Email(
    	sender="me@example.com",
        password="password",
        host="smtp.example.com",
        port=123,
    ),
    enl.Database()
)
  
root.add_subscriber(
    [
        enl.Subscriber("tesla@example.com"),
        enl.Subscriber("feynman@example.com"),
    ],
)
  
message = enl.Message(
    subject="Science Weekly",
    text="What is evolution?",
)
  
root.add_rule(message, enl.Schedule.every().monday)

while True:
    root.run_pending()
```

## Docs and Changelog
easynewsletter's documentation lives at [easynewsletter.readthedocs.io](https://easynewsletter.readthedocs.io) and changelog lives at [Changelog](https://easynewsletter.readthedocs.io/en/latest/changelog.html).

## License
This project is licensed under the GPL-3.0 - see the [LICENSE](LICENSE) file for details.
