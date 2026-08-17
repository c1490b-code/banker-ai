class BankerAgent:
    """Basic command interpreter for Banker AI."""

    def understand(self, message):
        text = message.lower().strip()

        if "balance" in text:
            return "balance"

        if "account" in text:
            return "accounts"

        if "transaction" in text:
            return "transactions"

        if "transfer" in text:
            return "transfer"

        if "pay" in text or "payment" in text:
            return "payment"

        return "general_banking"


agent = BankerAgent()
