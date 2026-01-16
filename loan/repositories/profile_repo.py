from loan import db

class ProfileRepository:

    @staticmethod
    def create(user_id, data):
        db.execute(
            "INSERT INTO profiles VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [
                user_id,
                data["full_names"],
                data["monthly_income"],
                data["business_type"],
                data["business_level"],
                data["phone"],
                data["country"],
                data["location"]
            ]
        )

    @staticmethod
    def update(user_id, data):
        db.execute(
            "UPDATE profiles SET full_names=?, monthly_income=?, business_type=?, business_level=?, phone=?, country=?, location=? WHERE user_id=?",
            [
                data["full_names"],
                data["monthly_income"],
                data["business_type"],
                data["business_level"],
                data["phone"],
                data["country"],
                data["location"],
                user_id
            ]
        )

    @staticmethod
    def get_by_user_id(user_id):
        rows = db.execute(
            "SELECT * FROM profiles WHERE user_id=?",
            [user_id]
        )
        return rows[0] if rows else None
