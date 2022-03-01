.. easynewsletter documentation master file, created by
   sphinx-quickstart on Sun Feb 27 11:44:01 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

easynewsletter
==============

.. image:: https://img.shields.io/badge/python-3.6%2B-blue
.. image:: https://img.shields.io/pypi/v/easynewsletter
.. image:: https://img.shields.io/pypi/dm/easynewsletter
.. image:: https://readthedocs.org/projects/easynewsletter/badge/?version=latest
.. image:: https://img.shields.io/github/license/beucismis/easynewsletter
.. image:: https://img.shields.io/badge/style-black-black

Newsletter module with customizable, scheduler and self-database. It uses `red-mail <https://github.com/Miksus/red-mail>`_ to send mail and scheduler for `schedule <https://github.com/dbader/schedule>`_.

Source: https://github.com/beucismis/easynewsletter

Features:
---------

- A simple API for blanning newsletters
- Customizable self-database
- Multiple message and scheduler support
- Be used in web applications (E.g: with Flask)
- A cross-platform module
- Tested on Python 3.9

Installation
------------

To install easynewsletter, run the following command from the command line:

.. code-block:: shell
  
  pip3 install --user easynewsletter

Example
-------

This example sends the "Science Weekly" newsletter to Tesla and Feynman every Monday.

.. code-block:: python

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

Read More
---------

.. toctree::
   :maxdepth: 2

   examples
   faq
   reference

.. toctree::
   :maxdepth: 1

   changelog

Issues
------

If you encounter any problems, please `file an issue <http://github.com/beucismis/easynewsletter/issues>`_ along with a detailed description. Please also use the search feature in the issue tracker beforehand to avoid creating duplicates. Thank you.

About
-----

Created by `Adil Gürbüz (beucismis) <beucismis@tutamail.com>`_

Distributed under the GNU General Public License v3.0 license. See ``LICENSE`` for more information.