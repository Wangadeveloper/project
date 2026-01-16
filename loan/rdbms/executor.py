import re

def execute_sql(db, sql, params=None):
    if params is None:
        params = []

    updated_table = None

    # ---------------- CREATE TABLE ----------------
    if sql.startswith("CREATE TABLE"):
        table_name = re.findall(r"CREATE TABLE (\w+)", sql)[0]
        if table_name not in db.tables:
            db.tables[table_name] = []
            updated_table = table_name
        return [], updated_table

    # ---------------- INSERT ----------------
    if sql.startswith("INSERT INTO"):
        table = re.findall(r"INSERT INTO (\w+)", sql)[0]

        if table == "users":
            row = {
                "id": len(db.tables[table]) + 1,
                "username": params[0],
                "email": params[1],
                "password": params[2]
            }
        elif table == "profiles":
            row = {
                "user_id": params[0],
                "full_names": params[1],
                "monthly_income": params[2],
                "business_type": params[3],
                "business_level": params[4],
                "phone": params[5],
                "country": params[6],
                "location": params[7]
            }
        else:
            raise Exception(f"INSERT not handled for table: {table}")

        db.tables[table].append(row)
        updated_table = table
        return [], updated_table

    # ---------------- SELECT ----------------
    if sql.startswith("SELECT"):
        table_name = re.findall(r"FROM (\w+)", sql)[0]
        if table_name not in db.tables:
            raise Exception(f"Table '{table_name}' does not exist")

        results = db.tables[table_name]

        if "WHERE email" in sql:
            results = [r for r in results if r["email"] == params[0]]
        elif "WHERE id" in sql:
            results = [r for r in results if r["id"] == params[0]]
        elif "WHERE user_id" in sql:
            results = [r for r in results if r["user_id"] == params[0]]

        return results, None

    # ---------------- UPDATE ----------------
    if sql.startswith("UPDATE"):
        table_name = sql.split()[1]
        if table_name not in db.tables:
            raise Exception(f"Table '{table_name}' does not exist")

        where_val = params[-1]

        if table_name == "profiles":
            keys = ["full_names", "monthly_income", "business_type", "business_level",
                    "phone", "country", "location"]
            for row in db.tables[table_name]:
                if row["user_id"] == where_val:
                    for i, key in enumerate(keys):
                        row[key] = params[i]
            updated_table = table_name
            return [], updated_table

        else:
            raise Exception(f"UPDATE not implemented for table {table_name}")

    raise Exception(f"Unsupported SQL: {sql}")
