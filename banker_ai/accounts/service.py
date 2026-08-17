from banker_ai.database import connect


def create_account(name, account_type, institution="", currency="USD"):
    with connect() as db:
        cursor = db.execute(
            """
            INSERT INTO accounts
            (name, account_type, institution, currency)
            VALUES (?, ?, ?, ?)
            """,
            (name, account_type, institution, currency),
        )
        db.commit()
        return cursor.lastrowid


def list_accounts():
    with connect() as db:
        return [dict(row) for row in db.execute(
            "SELECT * FROM accounts ORDER BY id"
        )]


def get_account(account_id):
    with connect() as db:
        row = db.execute(
            "SELECT * FROM accounts WHERE id = ?",
            (account_id,),
        ).fetchone()
        return dict(row) if row else None
