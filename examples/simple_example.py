__author__ = 'phoehne'

from requests.auth import HTTPDigestAuth
from marklogic.models import Database, Connection, Host, HttpServer, ElementRange, ElementAttributeRange

conn = Connection("192.168.57.141", HTTPDigestAuth("admin", "admin"))

server_hostname = hosts = Host.list_hosts(conn)[0].host_name()

db = Database("test-one", server_hostname)
db.create(conn).load_file(conn, "example_doc.json", "/test/document.json", ["example", "collection"])

modules = Database("test-one-modules", server_hostname)
modules.create(conn)

db = Database.lookup("test-one", conn)
db.add_index(ElementRange("order-id", u'int'))
db.add_index(ElementAttributeRange("customer", "id", scalar_type=u'int', element_namespace="http://foo.bar.com"))
db.save(conn)

srvr = HttpServer("test-one-http", 8400)
srvr.set_content_database(db.config[u'database-name']).set_modules_database(modules.config[u'database-name'])
srvr.create(conn)

db.load_file(conn, "example_doc.json", "/example/file.json", ["test"])
db.load_directory_files(conn, "data", "/test/data/", ["test2"])
db.load_directory(conn, "data", collections=["this", "that"])