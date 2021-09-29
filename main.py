def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help" or command == "h":
            print("psh: a simple shell written in Python")
        else:
            execute_commands(command)