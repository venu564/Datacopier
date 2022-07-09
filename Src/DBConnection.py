class ConnectDB:
    srvname = ''
    port = ''
    db = ''
    uname = ''
    pwd = ''
    def __init__(self,port,hostname,uname,pwd,db):
        self.port = port
        self.db = db
        self.srvname = hostname
        self.uname = uname
        self.pwd = pwd

    def get_connection(self):
        connection = f'postgresql://{self.uname}:{self.pwd}@{self.srvname}:{self.port}/{self.db}'
        return connection