#!/usr/bin/env python3
# file_manager.py (v1.3)
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

def rename(src, dst):
    """Переименовать файл или директорию."""
    try:
        os.rename(src, dst)
        print(f"Renamed {src} to {dst}")
    except Exception as e:
        print(f"[red]Error renaming:[/red] {e}")

def search(name_pattern, path='.'):
    """Рекурсивный поиск файлов/папок по подстроке в имени."""
    for root, dirs, files in os.walk(path):
        for entry in dirs + files:
            if name_pattern.lower() in entry.lower():
                print(os.path.join(root, entry))

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
    parser = argparse.ArgumentParser(
        description="Python File Manager v1.3"
    )
    parser.add_argument(
        'command',
        choices=['ls','cp','mv','rm','mkdir','search','view','rename'],
        help="Доступные команды: ls, cp, mv, rm, mkdir, search, view, rename"
    )
    parser.add_argument('src', nargs='?', default='.', help="Источник (файл/папка/шаблон)")
    parser.add_argument('dst', nargs='?', help="Назначение (для команд cp, mv, rename и базового пути для search)")
    args = parser.parse_args()

    cmd = args.command
    src = args.src
    dst = args.dst

    if cmd == 'ls':
        list_dir(src)
    elif cmd == 'mkdir':
        os.makedirs(src, exist_ok=True)
        print(f"Created directory {src}")
    elif cmd == 'cp' and dst:
        copy(src, dst)
    elif cmd == 'mv' and dst:
        move(src, dst)
    elif cmd == 'rm':
        remove(src)
    elif cmd == 'rename' and dst:
        rename(src, dst)
    elif cmd == 'search':
        # если dst указан, считаем его стартовой директорией
        search(src, dst or '.')
    elif cmd == 'view':
        view_file(src)
    else:
        print("[red]Unknown usage or missing arguments[/red]")

if __name__ == '__main__':
    main()