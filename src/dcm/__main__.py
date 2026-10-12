from dcm import db

db.init_db()
print("Database ready at", db.DB_PATH)