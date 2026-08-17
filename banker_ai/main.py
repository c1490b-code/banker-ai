import sys

from banker_ai.database import initialize
from banker_ai.api.server import run as server
from banker_ai.ai.agent import agent
from banker_ai.builder.code_generator import generate_project
from banker_ai.builder.runner import build, test, run


def usage():
    print("""
Banker AI

Commands:

  banker server
  banker ai <message>

  banker create app <name> <description>

  banker build <project>
  banker test <project>
  banker run <project>
""")


def main():
    initialize()
    args = sys.argv[1:]

    if not args:
        usage()
        return

    command = args[0]

    if command == "server":
        server()
        return

    if command == "ai":
        message = " ".join(args[1:])
        print("Banker AI")
        print("Intent:", agent.understand(message))
        print(message)
        return

    if command == "create" and len(args) >= 4:
        kind = args[1]

        if kind == "app":
            name = args[2]
            description = " ".join(args[3:])

            project = generate_project(name, description)

            print(f"Created {project}")
            return

    if command == "build" and len(args) == 2:
        build(args[1])
        return

    if command == "test" and len(args) == 2:
        test(args[1])
        return

    if command == "run" and len(args) == 2:
        run(args[1])
        return

    usage()


if __name__ == "__main__":
    main()
