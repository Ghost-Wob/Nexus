from app.database.database import Database


class ConceptRepository:

    def __init__(self):
        self.db = Database()

    def exists(self, slug: str) -> bool:

        result = self.db.fetchone(
            "SELECT id FROM concepts WHERE slug = ?",
            (slug,)
        )

        return result is not None

    def insert(
        self,
        title: str,
        slug: str,
        category: str,
        markdown: str
    ):

        self.db.execute(
            """
            INSERT INTO concepts(
                title,
                slug,
                category,
                markdown
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                title,
                slug,
                category,
                markdown
            )
        )

    def all(self):

        return self.db.fetchall(
            "SELECT * FROM concepts"
        )
