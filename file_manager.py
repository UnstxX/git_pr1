# file_manager.py (v1.2)
import os
import shutil
import argparse
from rich import print
from rich.console import Console
from rich.syntax import Syntax

console = Console()

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

def search(name_pattern, path='.'):
    """Рекурсивный поиск файлов/папок по имени."""
    for root, dirs, files in os.walk(path):
        for entry in dirs + files:
            if name_pattern.lower() in entry.lower():
                full = os.path.join(root, entry)
                print(full)

def view_file(path):
    """Вывод содержимого текстового файла с подсветкой синтаксиса."""
    if not os.path.isfile(path):
        print(f"[red]No such file:[/red] {path}")
        return
    try:
        text = open(path, encoding='utf-8').read()
        syntax = Syntax(text, "python", theme="monokai", line_numbers=True)
        console.print(syntax)
    except Exception as e:
        print(f"[red]Error reading file:[/red] {e}")

def main():
    parser = argparse.ArgumentParser(description="Python File Manager")
    parser.add_argument('command', choices=['ls','cp','mv','rm','mkdir','search','view'])
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
    elif args.command == 'search':
        search(args.src, args.dst or '.')
    elif args.command == 'view':
        view_file(args.src)
    else:
        print("[red]Unknown usage or missing arguments[/red]")

if __name__ == '__main__':
    main()