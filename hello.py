def say_hello(name=None):
    recipient = name or "tiger"
    print(f"Hi there {recipient}!")


def ask_name():
  return input("Yo! What's your name?\n> ")


if __name__ == "__main__":
  say_hello(ask_name())
