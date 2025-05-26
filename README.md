# Articles Code Challenge

A small Python project demonstrating object-relational mapping using raw SQL and SQLite. Authors write articles for magazines, and we manage the relationships using classes and SQL quaries

---

## Project Structure

code-challenge/
├── lib/
│ ├── models/
│ │ ├── author.py
│ │ ├── article.py
│ │ └── magazine.py
│ ├── db/
│ │ ├── connection.py
│ │ ├── schema.sql
│ │ └── seed.py
│ └── debug.py
├── scripts/
│ └── setup_db.py
├── tests/
│ ├── test_author.py
│ ├── test_article.py
│ └── test_magazine.py
└── README.md


## 
- **lib/models/** — Contains model classes for Author, Article, and Magazine with SQL methods.
- **lib/db/** — Database connection, schema, and seed data.
- **tests/** — Pytest test cases verifying the correctness of models and queries.
- **scripts/** — Helper scripts for database setup and example queries.

### How to Set Up and Run

 **Create and activate a virtual environment**

```bash
=> pipenv install
=> pipenv shell
=> pytest

