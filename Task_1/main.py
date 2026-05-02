from pathlib import Path
import argparse
import shutil


def copy_files(source_dir: Path, output_dir: Path):
    for item in source_dir.iterdir():
        try:
            if item.is_dir():
                copy_files(item, output_dir)
            elif item.is_file():
                extension = item.suffix[1:] if item.suffix else "no_extension"

                target_dir = output_dir / extension
                target_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy2(item, target_dir / item.name)

        except PermissionError:
            print(f"Немає доступу до: {item}")
        except OSError as error:
            print(f"Помилка під час обробки {item}: {error}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення")

    args = parser.parse_args()

    source_dir = Path(args.source)
    output_dir = Path(args.destination)

    if not source_dir.exists() or not source_dir.is_dir():
        print("Вихідна директорія не існує або не є директорією")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    copy_files(source_dir, output_dir)


if __name__ == "__main__":
    main()