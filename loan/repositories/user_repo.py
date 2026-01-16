from flask import current_app

class UserRepository:

    @staticmethod
    def create(username, email, password_hash):
        current_app.db.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            [username, email, password_hash]
        )

    @staticmethod
    def get_by_email(email):
        rows, _ = current_app.db.execute(
            "SELECT * FROM users WHERE email = ?",
            [email]
        )
        return rows[0] if rows else None

    @staticmethod
    def get_by_id(user_id):
        rows, _ = current_app.db.execute(
            "SELECT * FROM users WHERE id = ?",
            [user_id]
        )
        return rows[0] if rows else None
