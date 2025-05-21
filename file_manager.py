# file_manager.py
import os, shutil, argparse
from rich import print

def list_dir(path='.'):
    for name in os.listdir(path):
        print(name)

def main():
    parser = argparse.ArgumentParser(description="Python File Manager")
    parser.add_argument('command', choices=['ls','cp','mv','rm','mkdir'])
    parser.add_argument('src', nargs='?', default='.')
    parser.add_argument('dst', nargs='?')
    args = parser.parse_args()

    if args.command == 'ls':
        list_dir(args.src)
    elif args.command == 'mkdir' and args.src:
        os.makedirs(args.src, exist_ok=True)
        print(f"Created directory {args.src}")
    # … другие команды
    else:
        print("[red]Unknown usage[/red]")

if __name__ == '__main__':
    main()