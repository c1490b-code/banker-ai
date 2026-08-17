import sys

from banker_ai.database import initialize
from banker_ai.api.server import run
from banker_ai.ai.agent import agent
from banker_ai.builder.app_builder import create_app


def main():
    initialize()

    args = sys.argv[1:]

    if not args:
        print("Banker AI")
        print()
        print("Commands:")
        print("  banker server")
        print("  banker ai <message>")
        print("  banker create app <name>")
        return

    command = args[0]

    if command == "server":
        run()
        return

    if command == "ai":
        message = " ".join(args[1:])
        print("Banker AI")
        print("Intent:", agent.understand(message))
        print("Request:", message)
        return

    if command == "create" and len(args) >= 3:
        kind = args[1]
        name = " ".join(args[2:])

        if kind == "app":
            project = create_app(name)
            print("Created:", project)
            return

        print("Unknown project type:", kind)
        return

    print("Unknown command:", command)


if __name__ == "__main__":
    main()
