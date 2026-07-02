import  configparser
config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def get_username():
        username=config.get("login","username")
        return username

    @staticmethod
    def get_password():
        pwd=config.get("login","password")
        return pwd

    @staticmethod
    def get_login_url():
        url=config.get("urls","login_url")
        return url