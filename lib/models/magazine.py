from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self.name, self.category, self.id))
        else:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(id=row["id"], name=row["name"], category=row["category"]) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(id=row["id"], name=row["name"], category=row["category"]) if row else None

    @classmethod
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row["id"], name=row["name"], category=row["category"]) for row in rows]

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(**dict(row)) for row in rows]

    def contributors(self):
        from lib.models.author import Author 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT au.* FROM authors au
            JOIN articles a ON au.id = a.author_id
            WHERE a.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(id=row["id"], name=row["name"]) for row in rows]

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row["title"] for row in rows]

    def contributing_authors(self):
        from lib.models.author import Author 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT au.*, COUNT(a.id) AS article_count FROM authors au
            JOIN articles a ON au.id = a.author_id
            WHERE a.magazine_id = ?
            GROUP BY au.id
            HAVING article_count > 2
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(id=row["id"], name=row["name"]) for row in rows]

    @classmethod
    def top_publisher(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.*, COUNT(a.id) AS article_count FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            ORDER BY article_count DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row["id"], name=row["name"], category=row["category"])
        return None