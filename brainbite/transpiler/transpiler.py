import json
from pathlib import Path


_dir = Path(__file__).parent

with (_dir / 'substitute.json').open() as f:
    _replace_table = json.load(f)

print(_replace_table)
