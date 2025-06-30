from sqlite3 import Connection, connect


class UserRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def create(self, id: int, username: str):
        sql = "INSERT INTO users (id, name) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id, username))
        self.connection.commit()


if __name__ == "__main__":
    connection = connect("db.db")
    user_repo = UserRepository(connection)

    user_repo.create(1234, "Степан")