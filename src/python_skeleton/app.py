import logging
from pathlib import Path
from typing import Annotated

import typer

from python_skeleton.etl.transform import transform


def main(input_path: Annotated[Path, typer.Option(help="Path to input data file")]):
    logging.getLogger().setLevel(logging.INFO)
    logging.info(say_hello_to("Piotr"))
    transform(input_path)


def say_hello_to(me: str):
    return f"Hello {me}!"


if __name__ == "__main__":
    typer.run(main)
