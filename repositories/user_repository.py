from sqlite3 import Connection, connect


class UserRepository:
    def __init__(self, connection: Connection):
        self.connection = connection
        
    def check_user(self, user_id: int)  -> bool:
        sql = "SELECT * FROM users WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (user_id,))
        return cursor.fetchone() is not None

    def create(self, id: int, username: str):
        sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id, username))
        self.connection.commit()


if __name__ == "__main__":
    connection = connect("db.db")
    user_repo = UserRepository(connection)

    user_repo.create(1234, "Степан")