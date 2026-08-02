from rich.console import Console

console = Console()


def info(text):
    console.print(f"[cyan][INFO][/cyan] {text}")


def success(text):
    console.print(f"[green][OK][/green] {text}")


def warning(text):
    console.print(f"[yellow][WARN][/yellow] {text}")


def error(text):
    console.print(f"[red][ERROR][/red] {text}")
