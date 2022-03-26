import psycopg2
import constant
import yaml

class dataSource:
    __instance = None
    conn = None
    database = None
    host = None
    port = None
    user = None
    password = None

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


    def getConfig(self):
        with open('../config/local.yaml', 'r') as yamlfile:
            config = yaml.load(yamlfile, Loader=yaml.FullLoader)
            self.host = config[constant.DATASOURCE][constant.HOST]
            self.database = config[constant.DATASOURCE][constant.DATABASE]
            self.port = config[constant.DATASOURCE][constant.PORT]
            self.user = config[constant.DATASOURCE][constant.USER]
            self.password = config[constant.DATASOURCE][constant.PASSWORD]

    def connect(self):
        # establishing the connection
        self.getConfig()
        self.conn = psycopg2.connect(
                        host=self.host, port=self.port,
                        database=self.database,
                        user=self.user,  password=self.password)

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