import psycopg2
import constant
import yaml
from appConfig import appConfig

class dataSource:
    __instance = None
    conn = None
    config = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if dataSource.__instance == None:
            dataSource()
        return dataSource.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if dataSource.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            dataSource.__instance = self
            self.config = appConfig()



    def connect(self):
        # establishing the connection
        self.conn = psycopg2.connect(
                        host=self.config.host, port=self.config.port,
                        database=self.config.database,
                        user=self.config.user,  password=self.config.password)

    def getData(self, sql):
        # Creating a cursor object using the cursor() method
        cursor = self.conn.cursor()

        # Executing an MYSQL function using the execute() method
        cursor.execute(sql)
        return cursor

    def close(self):
        self.conn.close()


if __name__ == '__main__':

    print('test singletone')
    a = dataSource()
    a.getInstance().connect()
    cur = a.getInstance().getData('select * from pflo_holding')
    for aRow in cur:
        print(aRow)
    a.close()