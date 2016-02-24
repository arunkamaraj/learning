import MySQLdb

class mysql_explore():
    def __init__(self, host, usr, pwd, db):
        self.host =  host
        self.user = usr
        self.pwd = pwd
        self.database = db
        self.db = None
        self.cursor = None
        self.create_connection()

    def create_connection(self):
        self.db = MySQLdb.connect("localhost", "root", "123", "arun")
        self.cursor = self.db.cursor()
        return self.cursor

    def execution(self, query = None):
        if query:
            self.cursor.execute(query)
        else:
            print "Received query as a None"

    def fetch_data(self):
        data = self.cursor.fetchall()
        print data



if __name__ == "__main__":
    db_obj = mysql_explore("localhost", "root", "123", "arun")
    q= "select VERSION();"
    db_obj.execution(q)
    db_obj.fetch_data()
