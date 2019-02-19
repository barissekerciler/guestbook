import pymysql
import os


class DbOperations(object):
    @staticmethod
    def query_response_normalizer(columns, payload):
        normalized_result = list()
        for row in payload:
            normalized_result.append(dict(zip(columns, row)))
        return normalized_result

    def insert_message_to_db(self, username, message):
        try:
            db = pymysql.connect(host=os.environ.get('MYSQLHOST'), user=os.environ.get('MYSQLUSERNAME'),
                                 passwd=os.environ.get('MYSQLPASSWORD'),
                                 db=os.environ.get('MYSQLDB'), port=int(os.environ.get('MYSQLPORT')))
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO messages(username, message) VALUES('{username}', '{message}')".format(username=username,
                                                                                                   message=message))

            cursor.execute('SELECT last_insert_id()')
            last_id = cursor.fetchone()
            cursor.execute(
                "SELECT username, message FROM messages WHERE message_id = '{last_id}'".format(last_id=last_id[0]))
            columns = [column[0] for column in cursor.description]
            payload = cursor.fetchall()
            cursor.close()
            db.commit()
            db.close()
            return self.query_response_normalizer(columns, payload)
        except Exception('could not insert'):
            raise

    def get_data(self):
        try:
            db = pymysql.connect(os.environ.get('MYSQLHOST'), os.environ.get('MYSQLUSERNAME'),
                                 os.environ.get('MYSQLPASSWORD'),
                                 os.environ.get('MYSQLDB'))
            cursor = db.cursor()
            cursor.execute('SELECT username, message FROM messages LIMIT 50')
            columns = [column[0] for column in cursor.description]
            payload = cursor.fetchall()
            cursor.close()
            db.commit()
            db.close()
            return self.query_response_normalizer(columns, payload)
        except Exception('could not get'):
            raise
