from qaviton.utils.databases.sqlite import DataBase as DB


class DataBase(DB):
    def close(self):
        try:
            self.connection.close()
        except:
            pass