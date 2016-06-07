#!/usr/bin/env python
# encoding: utf-8

import argparse


"""
swift_system start|status
            pgs (1)
                monitor (2)
                    mfp (3)
                        stats|stats_summary
                    tda (3)
                        hip|hop
                server (2)
                    stats (3)
                        start|status
                    activity (3)
                        start|status
"""

DESCRIPTION = """
A program that all SWIFT Engineers to handle the most common
task for interacting with the application.
"""

EPILOG = """
A few example of commands:
    %(prog)s status
"""

common_args = argparse.ArgumentParser(add_help=False)
common_args.add_argument("arg", choices=[
                                      "start",
                                      "status",
                                      "stop",
                                      ])

parser = argparse.ArgumentParser(
        prog="swift_system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=DESCRIPTION,
        epilog=EPILOG,
        )

parser.add_argument("cmd", choices=["start", "status", "stop"])

subpar_pgs = parser.add_subparsers(title='pgs')
subpar_mfp = parser.add_subparsers(title='mfp')
parser_pgs = subpar_pgs.add_parser('pgs')
parser_mfp = subpar_mfp.add_parser('mfp')

subpar_pgs_moni = parser_pgs.add_subparsers(title='pgs_moni')
subpar_pgs_srv = parser_pgs.add_subparsers(title='pgs_srv')
parser_pgs_moni = subpar_pgs_moni.add_parser('pgs_moni')
parser_pgs_srv = subpar_pgs_moni.add_parser('pgs_srv')

subpar_pgs_moni_mfp = parser_pgs_moni.add_subparsers(title='pgs_moni_mfp')
subpar_pgs_srv_stats = parser_pgs_srv.add_subparsers(title='pgs_srv_stats')
parser_pgs_moni_mfp = subpar_pgs_moni_mfp.add_parser('pgs_moni_mfp')
parser_pgs_srv_stats = subpar_pgs_srv_stats.add_parser('pgs_srv_stats')

parser_pgs_moni_mfp.add_argument("cmd", choices=["start", "status", "stop"])
parser_pgs_srv_stats.add_argument("cmd", choices=["start", "status", "stop"])

parser.print_help()
