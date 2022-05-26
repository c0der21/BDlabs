import psycopg2


class DbConnection:

    def __init__(self, config):
        self.path = config.dbfilepath
        self.prefix = config.dbtableprefix
        self.conn = psycopg2.connect(password="rocket21",
                                     user="postgres",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="project_db")

    def __del__(self):
        if self.conn:
            self.conn.close()
