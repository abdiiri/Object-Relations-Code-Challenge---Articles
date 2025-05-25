from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")

    cursor.execute("INSERT INTO authors (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO authors (name) VALUES ('Bob')")

    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Monthly', 'Technology')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Health Weekly', 'Health')")

    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in 2025', 1, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Wellness Tips', 2, 2)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
