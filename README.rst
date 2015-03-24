==============================
MarkLogic Management In Python
==============================

Good news everybody! MarkLogic has a fantastic REST-based management
API. You can use anything that produces or consumes REST to talk to the
MarkLogic server and create database, manage clusters, add forests, etc.
This project does a few things.

1. Gives lovers of other languages an example of how to leverage the
   API.
2. Provides under-cover Pythonistas a chance to use Python to script
   MarkLogic operations.
3. As a possible spring board for later integration with other
   management tools.
4. As a way to explore more complex and automated management with
   MarkLogic (like test setup and teardown).
5. Possibly serve as a way to implement a kind of “migration” API for
   MarkLogic

Above all else the scripting should be simple. My goal (outside of
imports) is to allow people to script database creation and load in
about 5 lines of Python. Ideally, it whould be about 2 lines, for just a
basic database. My other goal was to include enough inline comments,
named parameters, and to move away from configuration files so that IDEs
like PyCharm would provide meaningful auto-completion and support.

So what is this project not going to do?

-  At this time I don't expect to create a Python alternative to the
   Java or JavaScript APIs.
-  Support every possible feature - instead I'm focusing on simplicity.

This is a community-driven project to build a Python wrapper for the
MarkLogic REST API.

Features
========

-  Database creation, deletion, and configuration
-  Application server creation, deletion, and configuration
-  Load content from filesystem into a database

Getting Started
===============

Installing MarkLogic
--------------------

1. Install MarkLogic (http://developer.marklogic.com/products)

2. Follow the very simple instructions to install the MarkLogic server.
   (Note that if you're using a RedHat based distro, you should install
   LSB and include –no-deps when installing the RPM if you get a warning
   about GLIBC 2.4).

Installing this package
-----------------------

This package is not yet available from PyPI. Meanwhile, there are two options
to install this package :

Contributor installation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: console

   git clone https://github.com/paul-hoehne/MarkLogic_Python.git
   cd MarkLogic_Python
   python setup.py develop

End-user installation
~~~~~~~~~~~~~~~~~~~~~

.. code:: console

   pip install git+git://github.com/paul-hoehne/MarkLogic_Python.git#egg=marklogic

Running the tests and examples
------------------------------

Of course some tests cannot always mock a MarkLogic server.

Please provide an environment variable named ``MARKLOGIC_TEST_CONNECTION``
that has the following form:

   hostname-or-ip 

.. note::

   Never ever provide the 

Support
=======

Support for the MarkLogic_Python project comes from the developer
community.
