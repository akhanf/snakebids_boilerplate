#!/usr/bin/env python3

"""Console script for snakebids_boilerplate."""

import os
from snakebids.app import SnakeBidsApp


def get_parser():
    """Exposes parser for sphinx doc generation, cwd is the docs dir"""
    app = SnakeBidsApp('../snakebids_boilerplate',skip_parse_args=True)
    return app.parser


def main():
    """Console script for snakebids_boilerplate."""
    app = SnakeBidsApp(os.path.abspath(os.path.dirname(__file__)))
    app.run_snakemake()
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
