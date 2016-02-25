import MySQLdb

create_table_query = "create table flipkart (Attempt_key INT NOT NULL , customer_id int(10), Date DATE ,Product_Gender CHAR(10),\
                Device_Type CHAR(7), City VARCHAR(10), Category VARCHAR(15), Customer_Login_type VARCHAR(10), \
                Delivery_Type VARCHAR(20), Quantity INT(4),  STARTS INT(4),  DONES INT(4), Amount INT(8), \
                Month VARCHAR(10));"

alter_table_query = "ALTER TABlE flipkart MODIFY COLUMN STARTS TINYINT(1), MODIFY COLUMN DONES  TINYINT(1) "

version_query = "select VERSION();"

load_data_query = """LOAD DATA INFILE '/tmp/Flipkart.csv' INTO TABLE flipkart FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS; """

class mysql_explore:
    def __init__(self, host, usr, pwd, db):
        self.host = host
        self.user = usr
        self.pwd = pwd
        self.database = db
        self.db = None
        self.cursor = None
        self.create_connection()

    def __del__(self):
        self.cursor.close()

    def create_connection(self):
        self.db = MySQLdb.connect("localhost", "root", "123", "arun")
        self.cursor = self.db.cursor()
        return self.cursor

    def execution(self, query=None):
        if query:
            self.cursor.execute(query)
        else:
            print "Received query as a None"

    def fetch_all(self):
        data = self.cursor.fetchall()
        print data

    def fetch_one(self):
        data = self.cursor.fetchone()
        print data

    def commiting(self):
        self.db.commit()


if __name__ == "__main__":
    db_obj = mysql_explore("localhost", "root", "123", "arun")
    # db_obj.execution(create_table_query)
    # db_obj.execution(alter_table_query)
    db_obj.execution(load_data_query)
    db_obj.commiting()

    # db_obj.fetch_all()
    # db_obj.fetch_one()
