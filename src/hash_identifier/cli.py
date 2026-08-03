import argparse
from time import sleep

from rich.console import Console
from rich.progress import track
from rich.table import Table

from .detector import identify





def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Identify possible hash algorithms.")
    parser.add_argument("hashval", help="Hash string to inspect")
    return parser


def _render_table(candidate):
    table = Table(title="Hash Results")
    table.add_column("Algorithm", style="cyan", no_wrap=True)
    table.add_column("Details", style="green", justify="left")
    table.add_column("Confidence", style="yellow", justify="left")
    table.add_column("Reason", style="green", justify="left")
    

    colors = {100: "green", 50: "yellow", 0: "red"}
    for item in candidate:
        color = colors.get(item.confidence, "white")
        table.add_row(
            f"[{color}]{item.algorithm}[/{color}]",
            item.detail,
            f"[{color}]{item.confidence}[/{color}]",
            item.reason,
        )

    return table


def main(argv=None) -> int:
    console = Console()
    args = _build_parser().parse_args(argv)
    console.print(f"The entered hash is [yellow]{args.hashval}[/yellow]")


    candidate = identify(args.hashval.strip())

    if candidate:
        console.print(_render_table(candidate))
    else:
        console.print("[yellow]No matching algorithms found[/yellow]")
        console.print(_render_table([]))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())