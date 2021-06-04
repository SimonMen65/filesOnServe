from pymysql import connect
from pymysql.cursors import DictCursor
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


class FilesAnubis(object):
    def __init__(self):
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(DictCursor)
        self.newID = None

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def getNewID(self):
        return self.newID

    def setNewID(self):
        sql = "select max(id) as m from Files"
        self.cursor.execute(sql)
        curr = self.cursor.fetchone()
        if curr['m'] is None:
            self.newID = 1
        else:
            self.newID = curr['m'] +1

    def uploadFile(self, file,name):

        if self.newID is None:
            print("Error: no id given")
            return

        sql = "insert into Files Values (%s,%s,%s);"
        self.cursor.execute(sql, (self.newID, name,file))
        self.newID += 1
        self.conn.commit()

    def viewFiles(self):
        res = []
        sql = "select * from Files"
        self.cursor.execute(sql)
        for f in self.cursor.fetchall():
            temp = {'id':f['id'],'name':f['name']}
            res.append(temp)
        return res
    
    def getFile(self,num):
        sql = "select name,file from Files where id = %s"
        self.cursor.execute(sql,num)
        return self.cursor.fetchone()
        
