import pymysql
import os


class DbOperations(object):
    def __init__(self):
        self.db = pymysql.connect(os.environ.get('MYSQLHOST'), os.environ.get('MYSQLUSERNAME'),
                                  os.environ.get('MYSQLPASSWORD'),
                                  os.environ.get('MYSQLDB'))
        self.cursor = self.db.cursor()

    def __close_connections(self):
        self.db.commit()
        self.db.close()

    @staticmethod
    def query_response_normalizer(columns, payload):
        normalized_result = list()
        for row in payload:
            normalized_result.append(dict(zip(columns, row)))
        return normalized_result

    def insert_message_to_db(self, username, message):
        try:
            self.cursor.execute(
                "INSERT INTO messages(username, message) VALUES('{username}', '{message}')".format(username=username,
                                                                                                   message=message))

            self.cursor.execute('SELECT last_insert_id()')
            last_id = self.cursor.fetchone()
            self.cursor.execute(
                "SELECT username, message FROM messages WHERE message_id = '{last_id}'".format(last_id=last_id[0]))
            columns = [column[0] for column in self.cursor.description]
            payload = self.cursor.fetchall()
            self.__close_connections()
            return self.query_response_normalizer(columns, payload)
        except pymysql.err:
            raise

    def get_data(self):
        try:
            self.cursor.execute('SELECT username, message FROM messages LIMIT 50')
            columns = [column[0] for column in self.cursor.description]
            payload = self.cursor.fetchall()
            self.__close_connections()
            return self.query_response_normalizer(columns, payload)
        except pymysql.err:
            raise
