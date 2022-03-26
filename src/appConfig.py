import constant
import yaml

class appConfig:
    __instance = None
    _database = None
    _host = None
    _port = None
    _user = None
    _password = None

    @property
    def password(self) -> str:
        return self._password

    @property
    def user(self) -> str:
        return self._user

    @property
    def database(self) -> str:
        return self._database

    @property
    def port(self) -> str:
        return  self._port

    @property
    def host(self) -> str:
        return self._host

    @staticmethod
    def getInstance():
        """ Static access method. """
        if appConfig.__instance == None:
            appConfig()
        return appConfig.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if appConfig.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            appConfig.__instance = self
            self.readConfig()

    def readConfig(self):
            with open(constant.CONFIG_FILE, 'r') as yamlfile:
                config = yaml.load(yamlfile, Loader=yaml.FullLoader)
                self._host = config[constant.DATASOURCE][constant.HOST]
                self._database = config[constant.DATASOURCE][constant.DATABASE]
                self._port = config[constant.DATASOURCE][constant.PORT]
                self._user = config[constant.DATASOURCE][constant.USER]
                self._password = config[constant.DATASOURCE][constant.PASSWORD]
                yamlfile.close()