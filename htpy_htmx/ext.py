from __future__ import annotations
from typing import Literal
from ._types import _selector, _event


def multipart(*, connect: str, close: _event, inherited: bool = False) -> dict[str, str]:
    """Stream HTML with multipart/mixed.

    https://four.htmx.org/extensions/hx-multipart
    """
    data: dict[str, str] = {}
    if connect:
        data[f"hx-multipart:connect{':inherited' if inherited else ''}"] = connect
    if close:
        data[f"hx-multipart:close{':inherited' if inherited else ''}"] = close
    return data


def sse(*, connect: _event = "", close: _event = "", inherited: bool = False) -> dict[str, str]:
    """Stream HTML with text/event-stream (SSE).

    https://four.htmx.org/extensions/hx-sse
    """
    data: dict[str, str] = {}
    if connect:
        data[f"hx-sse:connect{':inherited' if inherited else ''}"] = connect
    if close:
        data[f"hx-sse:close{':inherited' if inherited else ''}"] = close
    return data


def ws(*, connect: _event = "", send: bool = False, inherited: bool = False) -> dict[str, str]:
    """Stream HTML and send data over WebSockets.

    https://four.htmx.org/extensions/hx-ws
    """
    data: dict[str, str] = {}
    if connect:
        data[f"hx-ws:connect{':inherited' if inherited else ''}"] = connect
    if send:
        data[f"hx-ws:send{':inherited' if inherited else ''}"] = ""
    return data


def live(attribute: str, expression: str, *, inherited: bool = False) -> dict[str, str]:
    """Add reactive bindings to HTML.

    https://four.htmx.org/extensions/hx-live
    """
    return {f"hx-live:{attribute}{':inherited' if inherited else ''}": expression}


def optimistic(selector: _selector, *, inherited: bool = False) -> dict[str, str]:
    """Shows optimistic content during request.

    Note: This is an extension attribute. To use it, you must include the optimistic extension.
    https://four.htmx.org/reference/attributes/hx-optimistic
    """
    return {f"hx-optimistic{':inherited' if inherited else ''}": selector}


def browser_indicator(show_indicator: bool = True, *, inherited: bool = False) -> dict[str, str]:
    """Show tab's spinner with hx-browser-indicator.

    https://four.htmx.org/extensions/hx-browser-indicator
    """
    return {f"hx-browser-indicator{':inherited' if inherited else ''}": str(show_indicator).lower()}


def prompt(prompt: str, *, inherited: bool = False) -> dict[str, str]:
    """Prompt before requests with hx-prompt='Reason?'

    https://four.htmx.org/extensions/hx-prompt
    """
    return {f"hx-prompt{':inherited' if inherited else ''}": prompt}


def preload(
    event: Literal["mouseenter", "mouseover", "touchstart"], *, inherited: bool = False
) -> dict[str, str]:
    """Preloads content before user triggers request.

    Note: This is an extension attribute. To use it, you must include the preload extension.
    https://four.htmx.org/reference/attributes/hx-preload
    """
    return {f"hx-preload{':inherited' if inherited else ''}": event}


def ptag(tag: str, *, inherited: bool = False) -> dict[str, str]:
    """Skip unchanged polls with HX-PTag: "v42".

    https://four.htmx.org/extensions/hx-ptag
    """
    return {f"hx-ptag{':inherited' if inherited else ''}": tag}


def history(save_to_cache: bool, *, inherited: bool = False) -> dict[str, str]:
    """Restore back/forward pages from sessionStorage.

    https://four.htmx.org/extensions/hx-history-cache
    """
    return {f"hx-history{':inherited' if inherited else ''}": str(save_to_cache).lower()}


def head(
    strategy: Literal["merge", "append", "re-eval"], *, inherited: bool = False
) -> dict[str, str]:
    """Merge <head> tags with hx-head='merge'.

    https://four.htmx.org/extensions/hx-head
    """
    return {f"hx-head{':inherited' if inherited else ''}": strategy}


def targets(*selector: _selector, inherited: bool = False) -> dict[str, str]:
    """Target many elements.

    Requires the hx-targets extension
    https://four.htmx.org/extensions/hx-targets
    """
    return {f"hx-targets{':inherited' if inherited else ''}": ", ".join(selector)}


def nonce(csp_nonce: str, *, inherited: bool = False) -> dict[str, str]:
    """Make htmx work under strict Content Security Policy.

    https://four.htmx.org/extensions/hx-csp
    """
    return {f"hx-nonce{':inherited' if inherited else ''}": csp_nonce}
