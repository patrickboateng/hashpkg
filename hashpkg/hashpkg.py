from __future__ import annotations

import hashlib
from pathlib import Path


def generate_hash(filepath: str | Path, hash_algorithm: str):
    hash_algo = hashlib.new(hash_algorithm)

    with open(filepath, "rb") as f:
        hash_algo.update(f.read())

    return hash_algo.hexdigest()


def cli(): ...


if __name__ == "__main__":
    p = Path(__file__).parent
    print(generate_hash(p / "geolysis-0.2.0-py3-none-any.whl", "sha256"))
