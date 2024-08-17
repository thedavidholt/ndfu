# sha1sum_argparse.py

import argparse
import hashlib
import pathlib
import sys

# def process_file(filename: str) -> bytes:
#     return pathlib.Path(filename).read_bytes()

# def process_stdin() -> bytes:
#     return bytes("".join(sys.stdin), "utf-8")

# def sha1sum(data: bytes) -> str:
#     sha1_hash = hashlib.sha1()
#     sha1_hash.update(data)
#     return sha1_hash.hexdigest()

# def output_sha1sum(data: bytes, filename: str = "-") -> None:
#     print(f"{sha1sum(data)}  {filename}")

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        # usage="%(prog)s [MODE] [SOURCE] [TARGET]",
        description="Manipulate files based on their cryptographic hashes."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 0.0.1"
    )
    subparsers = parser.add_subparsers(title='commands')

    parser_ls = subparsers.add_parser('ls')
    parser_ls.add_argument('-r','--recurse', action='store_true',help='recurse through given directories')
    parser_ls.add_argument('target')

    parser_cp = subparsers.add_parser('cp')
    parser_cp.add_argument('-r','--recurse', action='store_true',help='recurse through given directories')
    parser_cp.add_argument("source", nargs='?')
    parser_cp.add_argument('target')

    parser_rm = subparsers.add_parser('rm')
    parser_rm.add_argument('-r','--recurse', action='store_true',help='recurse through given directories')
    parser_rm.add_argument("source", nargs='*')
    parser_rm.add_argument('target')
    return parser


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    print (str(args.mode))
        
    # if not args.files:
    #     print("No args detected, process stdin.")
    #     # output_sha1sum(process_stdin())
    # for file in args.files:
    #     if file == "-":
    #         print("This is for stdin.")
    #         # output_sha1sum(process_stdin(), "-")
    #         continue
    #     try:
    #         print("Process file from arguments.")
    #         # output_sha1sum(process_file(file), file)
    #     except (FileNotFoundError, IsADirectoryError) as err:
    #         print(f"{parser.prog}: {file}: {err.strerror}", file=sys.stderr)

if __name__ == "__main__":
    main()