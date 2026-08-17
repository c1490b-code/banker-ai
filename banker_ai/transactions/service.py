from banker_ai.database import connect


def record(account_id, description, amount, transaction_type,
           category=None):
    with connect() as db:
        db.execute(
            """
            INSERT INTO transactions
            (account_id, description, amount, transaction_type, category)
            VALUES (?, ?, ?, ?, ?)
            """,
            (account_id, description, amount, transaction_type, category),
        )

        if transaction_type == "credit":
            db.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (amount, account_id),
            )
        elif transaction_type == "debit":
            db.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, account_id),
            )

        db.commit()


def list_transactions(account_id=None):
    with connect() as db:
        if account_id:
            rows = db.execute(
                """
                SELECT * FROM transactions
                WHERE account_id = ?
                ORDER BY id DESC
                """,
                (account_id,),
            )
        else:
            rows = db.execute(
                "SELECT * FROM transactions ORDER BY id DESC"
            )

        return [dict(row) for row in rows]
