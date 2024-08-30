import argparse
import hashlib
import pathlib
import sys


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        # usage="%(prog)s [MODE] [SOURCE] [TARGET]",
        description="Manipulate files based on their cryptographic hashes."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 0.0.1"
    )
    subparsers = parser.add_subparsers(
        title='commands',
        help='use help options on each respective command for more info', 
        required=True
        )

    parser_ls = subparsers.add_parser('list', aliases=['ls'], help='list duplicate files based on their hashes')
    # parser_ls.add_argument('-R','--recursive', action='store_true',help='recurse through given directories')
    parser_ls.add_argument('target', help='target directory or file', type=pathlib.Path)
    parser_ls.set_defaults(func=list)

    # parser_cp = subparsers.add_parser('copy', aliases=['cp'], help='copy files ignoring duplicates')
    # parser_cp.add_argument('-R','--recursive', action='store_true',help='recurse through given directories')
    # parser_cp.add_argument("source", nargs='?')
    # parser_cp.add_argument('target')
    # parser_ls.set_defaults(func=copy)

    # parser_rm = subparsers.add_parser('remove', aliases=['rm'], help='remove duplicate files')
    # parser_rm.add_argument('-R','--recursive', action='store_true',help='recurse through given directories')
    # parser_rm.add_argument("source", nargs='*')
    # parser_rm.add_argument('target')
    # parser_ls.set_defaults(func=remove)
    return parser

# def path_exists(path: str) -> pathlib.Path:
#     path = pathlib.Path(path)
#     print(path.exists)
#     if path.exists():
#         return path
#     else:
#         raise FileNotFoundError(str(path))

def list(args) -> None:
    target = args.target
    if target.is_dir():
        files = {}
        dirs = []

        for child in target.iterdir():
            if child.is_file():
                file_hash = hash_file(child.read_bytes())

                if file_hash in files:
                    value = files[str(file_hash)]
                    value.append({
                        "name": child.name,
                        "full_path": str(child.absolute())
                    })
                    files[str(file_hash)] = value
                else:
                    files[str(file_hash)] = [{
                        "name": child.name,
                        "full_path": str(child.absolute())
                    }]

            elif child.is_dir():
                dirs.append(child)

        dirs.sort()

        dupes = { hash : dupe_list for hash, dupe_list in files.items() 
            if len(files[str(hash)]) > 1 }

        for dir in dirs:
            print(f"{'':>65}{dir}/")

        for hash in dupes:
            print(65 * '-', file=sys.stderr)
            for dupe in dupes[str(hash)]:
                print(f"{hash} {dupe['name']}")


def hash_file(data: bytes) -> str:
    hash = hashlib.sha256(data)
    return hash.hexdigest()

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()