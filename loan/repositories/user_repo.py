from loan import db

class UserRepository:

    @staticmethod
    def create(username, email, password_hash):
        db.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            [username, email, password_hash]
        )

    @staticmethod
    def get_by_email(email):
        rows = db.execute(
            "SELECT * FROM users WHERE email = ?",
            [email]
        )
        return rows[0] if rows else None

    @staticmethod
    def get_by_id(user_id):
        rows = db.execute(
            "SELECT * FROM users WHERE id = ?",
            [user_id]
        )
        return rows[0] if rows else None
