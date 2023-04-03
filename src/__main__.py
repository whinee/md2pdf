try:
    from .cli import cli
except ImportError:
    from src.cli import cli

cli()
