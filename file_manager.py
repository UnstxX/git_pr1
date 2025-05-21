# file_manager.py (v1.1)
import os
import shutil
import argparse
from rich import print

def list_dir(path='.'):
    for name in os.listdir(path):
        print(name)

def copy(src, dst):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
        print(f"Copied {src} to {dst}")
    except Exception as e:
        print(f"[red]Error copying:[/red] {e}")

def move(src, dst):
    try:
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")
    except Exception as e:
        print(f"[red]Error moving:[/red] {e}")

def remove(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"Removed {path}")
    except Exception as e:
        print(f"[red]Error removing:[/red] {e}")

def main():
    parser = argparse.ArgumentParser(description="Python File Manager")
    parser.add_argument('command', choices=['ls','cp','mv','rm','mkdir'])
    parser.add_argument('src', nargs='?', default='.')
    parser.add_argument('dst', nargs='?')
    args = parser.parse_args()

    if args.command == 'ls':
        list_dir(args.src)
    elif args.command == 'mkdir':
        os.makedirs(args.src, exist_ok=True)
        print(f"Created directory {args.src}")
    elif args.command == 'cp' and args.dst:
        copy(args.src, args.dst)
    elif args.command == 'mv' and args.dst:
        move(args.src, args.dst)
    elif args.command == 'rm':
        remove(args.src)
    else:
        print("[red]Unknown usage or missing arguments[/red]")

if __name__ == '__main__':
    main()