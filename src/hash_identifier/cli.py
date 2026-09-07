import argparse
from time import sleep

import json
from dataclasses import asdict

from rich.console import Console
from rich.progress import track
from rich.table import Table

from .detector import identify


def _positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number






def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Identify possible hash algorithms.")
    parser.add_argument("-j","--json",action="store_true",default=False,help="Ouptut results as json")
    parser.add_argument("-v","--verbose",action="store_true",default=False,help="Verbose output for detailed information")
    parser.add_argument("--top", type=_positive_int, help="Return the top N matches")
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

def _render_verbose_evidence(text, candidates):
    table = Table(title="Verbose Evidence")
    table.add_column("Input length", style="cyan", no_wrap=True)
    table.add_column("Algorithm", style="cyan", no_wrap=True)
    table.add_column("Confidence", style="yellow", justify="left")
    table.add_column("Evidence", style="green", justify="left")

    colors = {100: "green", 50: "yellow", 0: "red"}
    for item in candidates:
        color = colors.get(item.confidence, "white")
        table.add_row(
            str(len(text)),
            f"[{color}]{item.algorithm}[/{color}]",
            f"[{color}]{item.confidence}[/{color}]",
            item.reason,
        )

    return table


def main(argv=None) -> int:
    console = Console()
    args = _build_parser().parse_args(argv)
    candidate = identify(args.hashval.strip())
    if args.top is not None:
        candidate = candidate[:args.top]
    if(not args.json and not args.verbose):
        console.print(f"The entered hash is [yellow]{args.hashval}[/yellow]")        
        if candidate:
            console.print(_render_table(candidate))
        else:
            console.print("[yellow]No matching algorithms found[/yellow]")
            console.print(_render_table([]))
    elif(args.json):
        ouput_data = {
            "input" : args.hashval.strip(),
            "candidates" : [asdict(c) for c in candidate]
        }
        print(json.dumps(ouput_data,indent = 4))
    elif (args.verbose and not args.json):
        console.print(f"The entered hash is [yellow]{args.hashval}[/yellow]")
        if candidate:
            console.print(_render_verbose_evidence(args.hashval.strip(), candidate))
            console.print(f"Input length: {len(args.hashval.strip())}")
        else:
            console.print("[yellow]No matching algorithms found[/yellow]")
            console.print(_render_verbose_evidence(args.hashval.strip(), []))
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())