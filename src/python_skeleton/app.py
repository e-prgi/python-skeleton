import logging


def main():
    logging.getLogger().setLevel(logging.INFO)
    logging.info(say_hello_to("Piotr"))


def say_hello_to(me: str):
    return f"Hello {me}!"


if __name__ == "__main__":
    main()
