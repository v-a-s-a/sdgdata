import sys

import httpx

_enabled = False


def enable() -> None:
    """
    Enables debug query output for all pyunsdg clients in this process.
    """
    global _enabled
    _enabled = True


def disable() -> None:
    """
    Disables debug query output for all pyunsdg clients in this process.
    """
    global _enabled
    _enabled = False


def is_enabled() -> bool:
    """
    Returns whether debug query output is enabled.
    """
    return _enabled


def print_query(request: httpx.Request) -> None:
    """
    Prints the fully constructed request URL when debug mode is enabled.
    """
    if _enabled:
        print(f"pyunsdg query: {request.url}", file=sys.stderr)
