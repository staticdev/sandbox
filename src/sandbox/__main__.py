"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Sandbox."""


if __name__ == "__main__":
    main(prog_name="sandbox")  # pragma: no cover
