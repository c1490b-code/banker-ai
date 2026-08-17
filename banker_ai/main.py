import sys

from banker_ai.database import initialize
from banker_ai.api.server import run
from banker_ai.ai.agent import agent


def main():
    initialize()

    if len(sys.argv) > 1 and sys.argv[1] == "server":
        run()
        return

    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        print("Banker AI")
        print("Intent:", agent.understand(message))
        print("Request:", message)
        return

    print("Banker AI")
    print("Usage:")
    print("  python -m banker_ai.main server")
    print("  python -m banker_ai.main 'show my balance'")


if __name__ == "__main__":
    main()
