# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

#
# Copyright 2015 MarkLogic Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# File History
# ------------
#
# Paul Hoehne       03/25/2015     Initial development
# Paul Hoehne       03/26/2015     Adding dynamic lookup of host name
#

import unittest
from marklogic.models import Database, Connection, Host, Forest
from requests.auth import HTTPDigestAuth
from resources import TestConnection as tc
from test_settings import DatabaseSettings as ds

class TestDatabase(unittest.TestCase):
    """
    Basic creation test function.

    """

    def test_simple_create(self):
        """
        TODO: The hostname should come from the server's hostname

        Test the basic create function.  Creates a database and then check to see that it
        exists by getting the database configuration from the server.  It then destroys
        the database.

        :return: None
        """
        conn = Connection(tc.hostname, HTTPDigestAuth(tc.admin, tc.password))
        hosts = Host.list_hosts(conn)
        db = Database("test-db", hosts[0].host_name())

        db.create(conn)

        validate_db = Database.lookup("test-db", conn)
        try:
            self.assertIsNotNone(validate_db)
            self.assertEqual('test-db', validate_db.database_name())

        finally:
            validate_db.remove(conn)
            validate_db = Database.lookup("test-db", conn)
            self.assertIsNone(validate_db)

    def test_no_database_found(self):
        conn = Connection(tc.hostname, HTTPDigestAuth(tc.admin, tc.password))
        db = Database.lookup("No-Such-Database", conn)

        self.assertIsNone(db)

    def test_list_databases(self):
        conn = Connection(tc.hostname, HTTPDigestAuth(tc.admin, tc.password))
        databases = Database.list_databases(conn)

        self.assertGreater(len(databases), 4)

        db_names = [db.database_name() for db in databases]
        self.assertTrue("Modules" in db_names)
        self.assertTrue("Documents" in db_names)

    def test_create_simple_forests(self):
        """
        Test the following scenario:

        The database is given the names of two forests.
        It should then create the two named forests.

        """
        conn = Connection(tc.hostname, HTTPDigestAuth(tc.admin, tc.password))

        hosts = Host.list_hosts(conn)
        db = Database("simple-forest-create-test-db", hosts[0].host_name())

        db.set_forests(["simple-forest-create-forest1", "simple-forest-create-forest2"])

        db.create(conn)

        db = Database.lookup("simple-forest-create-test-db", conn)
        try:
            self.assertEqual(2, len(db.forests()))

            self.assertIn("simple-forest-create-forest1", db.forests())
            self.assertIn("simple-forest-create-forest2", db.forests())

        finally:
            db.remove(conn)

    def test_create_single_detailed_forest(self):
        """
        Test the following scenario:

        The database is given a forest object.  It should create a forest with
        the given name.  That forest should match the features of the datailed
        forest.

        """

        conn = Connection(tc.hostname, HTTPDigestAuth(tc.admin, tc.password))

        hosts = Host.list_hosts(conn)
        db = Database("detailed-forest-create-test-db", hosts[0].host_name())

        forest = Forest("detailed-forest-create-forest1", host=hosts[0].host_name(),
                        large_data_directory=ds.large_data_directory)

        db.set_forests([forest])

        db.create(conn)

        forest = Forest.lookup("detailed-forest-create-forest1", conn)

        try:
            self.assertEqual("detailed-forest-create-forest1", forest.name())
            self.assertEqual(ds.large_data_directory, forest.large_data_directory())
        finally:
            db.remove(conn)

if __name__ == "__main__":
    unittest.main()