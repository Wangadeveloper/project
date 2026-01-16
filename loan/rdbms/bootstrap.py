def bootstrap(db):
    db.execute("""
    CREATE TABLE users (
        id INT PRIMARY KEY,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    db.execute("""
    CREATE TABLE profiles (
        user_id INT PRIMARY KEY,
        full_names TEXT,
        monthly_income INT,
        business_type TEXT,
        business_level TEXT,
        phone TEXT,
        country TEXT,
        location TEXT
    )
    """)
