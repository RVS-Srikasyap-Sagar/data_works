import subprocess
import json
from datetime import datetime
from pathlib import Path


def handle_A1(params):
    subprocess.run(["uv", "pip", "install", "requests"])
    result = subprocess.run(
        ["python", params["script_url"], params["email"]],
        capture_output=True
    )
    return result.stdout.decode()


def handle_A2(params):
    subprocess.run([
        "prettier",
        "--write",
        params["input_path"],
        "--parser", "markdown"
    ], check=True)


def handle_A3(params):
    with open(params["input_file"], "r") as f:
        dates = [datetime.strptime(line.strip(), "%Y-%m-%d") for line in f]

    count = sum(1 for d in dates if d.weekday() == 2)  # Wednesday is 2
    Path(params["output_file"]).write_text(str(count))
