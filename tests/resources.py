# -*- coding: utf-8 -*-
"""Some common resources for marklogic unittests and examples"""
# FIXME: Find a better place to have this available for tests and examples

from __future__ import unicode_literals, print_function, absolute_import

from collections import namedtuple
import os

# ML test server location and credentials in MARKLOGIC_TEST_CONNECTION env var
# EBNF: MARKLOGIC_TEST_CONNECTION = hostname, ":", port, ":", mgmt-port, ":", username, ":", password ;

test_connection = None


def _setup():
    global test_connection
    MARKLOGIC_TEST_CONNECTION = os.environ.get('MARKLOGIC_TEST_CONNECTION', '192.168.57.141:8000:8002:admin:admin')
    params = ['hostname', 'port', 'mgmt_port', 'username', 'password']
    values = MARKLOGIC_TEST_CONNECTION.split(':')
    try:
        assert len(values) == len(params)
        # port values -> int
        for k in (1, 2):
            values[k] = int(values[k])
    except Exception as exc:
        new_exc = type(exc)(str(exc) + " Please provide a MARKLOGIC_TEST_CONNECTION env var as described in README.rst")
        raise new_exc
    ConnectionData = namedtuple('ConnectionData', params)
    test_connection = ConnectionData(**dict(zip(params, values)))

_setup()
del _setup
