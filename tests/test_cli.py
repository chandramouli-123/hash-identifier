import pytest
import sys
from pathlib import Path

import json
from dataclasses import asdict


# Add the parent directory to sys.path to allow importing hash_identifier
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hash_identifier.cli import main
from hash_identifier.detector import identify

# checks wheather the json output is correct.

def test_cli_output(capsys):
    main(["--json","$2b$12$"+"a"*53])
    captured = capsys.readouterr()
    expected_json = json.dumps({
        "input" : "$2b$12$"+"a"*53,
        "candidates" : [asdict(c) for c in identify("$2b$12$"+"a"*53)]
    },indent = 4)
    assert json.loads(captured.out) == json.loads(expected_json) # json.loads to prevent invisible whitespace error

def test_cli_output_no_json(capsys):
    main(["$2b$12$"+"a"*53])
    captured = capsys.readouterr()
    assert "The entered hash is " in captured.out
    assert "bcrypt" in captured.out
    assert captured.err == ""
    

def test_cli_output_no_json_no_match(capsys):
    main(["abc"])
    captured = capsys.readouterr()
    assert "The entered hash is " in captured.out
    assert "No matching algorithms found" in captured.out
    assert captured.err == ""
    

def test_cli_output_no_json_no_match_no_newline(capsys):
    main(["abc"])
    captured = capsys.readouterr()
    assert "The entered hash is " in captured.out
    assert "No matching algorithms found" in captured.out
    assert captured.err == ""


def test_cli_verbose_output(capsys):
    hash_value = "$2b$12$" + "a" * 53

    main(["--verbose", hash_value])

    captured = capsys.readouterr()
    assert "bcrypt" in captured.out
    assert "Verbose Evidence" in captured.out
    assert "Input length: 60" in captured.out
    assert "Matches Prefix" in captured.out
    assert "Confidence" in captured.out
    assert "100" in captured.out
    assert captured.err == ""
