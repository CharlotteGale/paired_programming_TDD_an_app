from lib.database_connection import DatabaseConnection


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        pass

if __name__ == '__main__':
    app = Application()
    app.run()
