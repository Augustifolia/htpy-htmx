from __future__ import annotations
import json
from typing import Literal, TypeAlias, Any, overload

from htpy import Element

partial = Element("hx-partial")


_selector: TypeAlias = (
    str | Literal["this", "next", "previous", "body", "document", "window", "host"]
)

_event: TypeAlias = (
    str
    | Literal[
        "load",
        "revealed",
        "intersect",
        "submit",
        "change",
        "input",
        "focus",
        "blur",
        "click",
        "dblclick",
        "mousedown",
        "mouseup",
        "mousemove",
        "mouseenter",
        "mouseleave",
        "wheel",
        "mousewheel",
        "keyup",
        "keydown",
        "keypress",
        "dragstart",
        "drag",
        "dragend",
        "dragenter",
        "dragover",
        "dragleave",
        "drop",
        "play",
        "pause",
        "ended",
        "volumechange",
        "touchstart",
        "touchend",
        "touchmove",
        "touchcancel",
        "resize",
        "scroll",
        "select",
        "search",
        "invalid",
        "contextmenu",
        "reset",

    ]
)


class SafeString(str):
    def __html__(self) -> SafeString:
        return self

    def __str__(self) -> SafeString:
        return self


def get(url: str, *, inherited: bool = False) -> dict[str, str]:
    """Issues GET request to specified URL.

    https://four.htmx.org/reference/attributes/hx-get
    """
    return {f"hx-get{':inherited' if inherited else ''}": url}


def post(url: str, *, inherited: bool = False) -> dict[str, str]:
    """Issues POST request to specified URL.

    https://four.htmx.org/reference/attributes/hx-post
    """
    return {f"hx-post{':inherited' if inherited else ''}": url}


def put(url: str, *, inherited: bool = False) -> dict[str, str]:
    """Issues PUT request to specified URL.

    https://four.htmx.org/reference/attributes/hx-put
    """
    return {f"hx-put{':inherited' if inherited else ''}": url}


def patch(url: str, *, inherited: bool = False) -> dict[str, str]:
    """Issues PATCH request to specified URL.

    https://four.htmx.org/reference/attributes/hx-patch
    """
    return {f"hx-patch{':inherited' if inherited else ''}": url}


def delete(url: str, *, inherited: bool = False) -> dict[str, str]:
    """Issues DELETE request to specified URL.

    https://four.htmx.org/reference/attributes/hx-delete
    """
    return {f"hx-delete{':inherited' if inherited else ''}": url}


def trigger(*event: _event, inherited: bool = False) -> dict[str, str]:
    """Controls when element issues requests.

    https://four.htmx.org/reference/attributes/hx-trigger
    """
    return {f"hx-trigger{':inherited' if inherited else ''}": ", ".join(event)}


_swap_style: TypeAlias = Literal[
    "innerHTML",
    "outerHTML",
    "beforebegin",
    "before",
    "afterbegin",
    "prepend",
    "beforeend",
    "append",
    "afterend",
    "after",
    "delete",
    "none",
    "innerMorph",
    "outerMorph",
    "textContent",
    "outerSync",
    "upsert",  # Requires the hx-upsert extension.
]


def swap(
    style: _swap_style,
    *,
    transition: bool | None = None,
    swap: str = "",
    settle: str = "",
    ignoreTitle: bool | None = None,
    scroll: Literal["top", "bottom"] | str = "",
    scrollTarget: str = "",
    show: Literal["top", "bottom", "none"] | str = "",
    showTarget: str = "",
    focusScroll: bool | None = None,
    target: str = "",
    strip: bool | None = None,
    swapEmpty: bool | None = None,
    inherited: bool = False,
) -> dict[str, str]:
    """Controls how response is inserted.

    https://four.htmx.org/reference/attributes/hx-swap
    """
    text: str = style
    if transition is not None:
        text += f" transition:{str(transition).lower()}"
    if swap:
        text += f" swap:{swap}"
    if settle:
        text += f" settle:{settle}"
    if ignoreTitle is not None:
        text += f" ignoreTitle:{str(ignoreTitle).lower()}"
    if scroll:
        text += f" scroll:{scroll}"
    if scrollTarget:
        text += f" scrollTarget:{scrollTarget}"
    if show:
        text += f" show:{show}"
    if showTarget:
        text += f" showTarget:{showTarget}"
    if focusScroll is not None:
        text += f" focusScroll:{str(focusScroll).lower()}"
    if target:
        text += f" target:{target}"
    if strip is not None:
        text += f" strip:{str(strip).lower()}"
    if swapEmpty is not None:
        text += f" swapEmpty:{str(swapEmpty).lower()}"
    return {f"hx-swap{':inherited' if inherited else ''}": text}


def morph_skip(*, inherited: bool = False) -> dict[str, bool]:
    """Skip morphing with attributes and children"""
    return {f"hx-morph-skip{':inherited' if inherited else ''}": True}


def morph_skip_children(*, inherited: bool = False) -> dict[str, bool]:
    """Skip morphing with children only; attributes still morph"""
    return {f"hx-morph-skip-children{':inherited' if inherited else ''}": True}


def target(selector: _selector, *, inherited: bool = False) -> dict[str, str]:
    """Controls where response is inserted.

    https://four.htmx.org/reference/attributes/hx-target
    """
    return {f"hx-target{':inherited' if inherited else ''}": selector}


def targets(*selector: _selector, inherited: bool = False) -> dict[str, str]:
    """Target many elements.

    Requires the hx-targets extension
    https://four.htmx.org/extensions/hx-targets
    """
    return {f"hx-targets{':inherited' if inherited else ''}": ", ".join(selector)}


def select(selector: _selector, *, inherited: bool = False) -> dict[str, str]:
    """Controls which response part is inserted.

    https://four.htmx.org/reference/attributes/hx-select
    """
    return {f"hx-select{':inherited' if inherited else ''}": selector}


_htmx_events: TypeAlias = Literal[
    "htmx:config:request",
    "htmx:before:request",
    "htmx:after:request",
    "htmx:finally:request",
    "htmx:before:swap",
    "htmx:after:swap",
    "htmx:finally:swap",
    "htmx:before:cleanup",
    "htmx:after:cleanup",
    "htmx:confirm",
    "htmx:error",
    "htmx:abort",
    "htmx:before:init",
    "htmx:after:init",
    "htmx:before:process",
    "htmx:after:process",
    "htmx:before:history:update",
    "htmx:after:history:update",
    "htmx:after:history:push",
    "htmx:after:history:replace",
    "htmx:before:history:restore",
    "htmx:before:viewTransition",
    "htmx:after:viewTransition",
    "htmx:before:response",
    "htmx:before:settle",
    "htmx:after:settle",
    "htmx:response:error",
]


@overload
def on(event: _event | _htmx_events, js: str, *, inherited: bool = False) -> dict[str, str]:
    pass


@overload
def on(*, js: str, inherited: bool = False) -> dict[str, str]:
    pass


def on(
    event: _event | _htmx_events = "", js: str = "", *, inherited: bool = False
) -> dict[str, str]:
    """Runs inline JavaScript when event fires.

    https://four.htmx.org/reference/attributes/hx-on
    """
    return {
        f"hx-on{':' + event if event else ''}{':inherited' if inherited else ''}": SafeString(js)
    }


class JS:
    """Used to mark strings as js expressions for use in hx-vals and hx-headers."""

    start = "HXJS-start:"
    end = ":HXJS-end"

    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{JS.start}{self.value}{JS.end}"

    def __str__(self) -> str:
        return f"JS({self.value})"


class _HTMXJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, JS):
            return repr(o)
            # Let the base class default method raise the TypeError
        return super().default(o)

    def encode(self, o: Any) -> str:
        string: str = super().encode(o)
        string = string.replace(f'"{JS.start}', "").replace(f'{JS.end}"', "")
        return string


def vals(
    data: dict[str, Any], *, js: bool = False, append: bool = False, inherited: bool = False
) -> dict[str, str]:
    """Adds values to request parameters.

    https://four.htmx.org/reference/attributes/hx-vals
    """
    data_string = json.dumps(data, cls=_HTMXJSONEncoder)
    return {
        f"hx-vals{':append' if append else ''}{':inherited' if inherited else ''}": f"{'js:' if js else ''}{data_string}"
    }


def include(
    selector: _selector, *, append: bool = False, inherited: bool = False
) -> dict[str, str]:
    """Includes additional element values in request.

    https://four.htmx.org/reference/attributes/hx-include
    """
    return {f"hx-include{':append' if append else ''}{':inherited' if inherited else ''}": selector}


def swap_oob(
    swap_style: _swap_style | bool = True, selector: _selector = "", *, inherited: bool = False
) -> dict[str, str]:
    """Marks response elements to swap into page by ID.

    https://four.htmx.org/reference/attributes/hx-swap-oob
    """
    if isinstance(swap_style, bool):
        style: str = str(swap_style).lower()
    else:
        style = str(swap_style)
    return {
        f"hx-swap-oob{':inherited' if inherited else ''}": f"{style}{':' + selector if selector else ''}"
    }


def select_oob(*selector: str, inherited: bool = False) -> dict[str, str]:
    """Picks response elements to swap into page by ID.

    https://four.htmx.org/reference/attributes/hx-select-oob
    """
    return {f"hx-select-oob{':inherited' if inherited else ''}": ", ".join(selector)}


def push_url(push: bool = True, *, inherited: bool = False) -> dict[str, str]:
    """Pushes URL into browser history.

    https://four.htmx.org/reference/attributes/hx-push-url
    """
    return {f"hx-push-url{':inherited' if inherited else ''}": str(push).lower()}


def replace_url(replace: bool = True, *, inherited: bool = False) -> dict[str, str]:
    """Replaces current URL in browser history.

    https://four.htmx.org/reference/attributes/hx-replace-url
    """
    return {f"hx-replace-url{':inherited' if inherited else ''}": str(replace).lower()}


def headers(data: dict[str, Any], *, js: bool = False, inherited: bool = False) -> dict[str, str]:
    """Adds custom headers to request.

    https://four.htmx.org/reference/attributes/hx-headers
    """
    return {
        f"hx-headers{':inherited' if inherited else ''}": f"{'js:' if js else ''}{json.dumps(data, cls=_HTMXJSONEncoder)}"
    }


def encoding(
    encoding_string: str | Literal["application/x-www-form-urlencoded", "multipart/form-data"],
    *,
    inherited: bool = False,
) -> dict[str, str]:
    """Sets request encoding type.

    https://four.htmx.org/reference/attributes/hx-encoding
    """
    return {f"hx-encoding{':inherited' if inherited else ''}": encoding_string}


def indicator(
    selector: _selector, *, append: bool = False, inherited: bool = False
) -> dict[str, str]:
    """Specifies loading indicator element.

    https://four.htmx.org/reference/attributes/hx-indicator
    """
    return {
        f"hx-indicator{':append' if append else ''}{':inherited' if inherited else ''}": selector
    }


@overload
def boost(boost: bool, *, inherited: bool = False) -> dict[str, str]:
    pass


@overload
def boost(
    *,
    swap: _swap_style | str = "",
    target: _selector = "",
    select: _selector = "",
    inherited: bool = False,
) -> dict[str, str]:
    pass


def boost(
    boost: bool | None = None,
    *,
    swap: _swap_style | str = "",
    target: _selector = "",
    select: _selector = "",
    inherited: bool = False,
) -> dict[str, str]:
    """Converts links and forms to AJAX.

    https://four.htmx.org/reference/attributes/hx-boost
    """
    if boost is not None:
        text = str(boost).lower()
    else:
        text = ""
        if swap:
            text += f"swap:{swap}"
        if target:
            text += f" target:{target}"
        if select:
            text += f" select:{select}"
    return {f"hx-boost{':inherited' if inherited else ''}": text}


def sync(
    selector: _selector,
    strategy: Literal["drop", "abort", "replace", "queue first", "queue last", "queue all"],
    *,
    inherited: bool = False,
) -> dict[str, str]:
    """Synchronizes requests between elements.

    https://four.htmx.org/reference/attributes/hx-sync
    """
    return {f"hx-sync{':inherited' if inherited else ''}": f"{selector}:{strategy}"}


def confirm(confirmation_prompt: str, *, inherited: bool = False) -> dict[str, str]:
    """Shows confirmation dialog before request.

    https://four.htmx.org/reference/attributes/hx-confirm
    """
    return {f"hx-confirm{':inherited' if inherited else ''}": confirmation_prompt}


def validate(validate: bool = True, *, inherited: bool = False) -> dict[str, str]:
    """Validates before submitting request.

    https://four.htmx.org/reference/attributes/hx-validate
    """
    return {f"hx-validate{':inherited' if inherited else ''}": str(validate).lower()}


def disable(*selector: _selector, merge: bool = False, inherited: bool = False) -> dict[str, str]:
    """Disables elements during request.

    https://four.htmx.org/reference/attributes/hx-disable
    """
    return {
        f"hx-disable{':merge' if merge else ''}{':inherited' if inherited else ''}": ", ".join(
            selector
        )
    }


def ignore(*, inherited: bool = False) -> dict[str, str]:
    """Disables htmx processing for element.

    https://four.htmx.org/reference/attributes/hx-ignore
    """
    return {f"hx-ignore{':inherited' if inherited else ''}": ""}


def preserve(*, inherited: bool = False) -> dict[str, str]:
    """Preserves element during swaps.

    https://four.htmx.org/reference/attributes/hx-preserve
    """
    return {f"hx-preserve{':inherited' if inherited else ''}": "true"}


def preload(
    event: Literal["mouseenter", "mouseover", "touchstart"], *, inherited: bool = False
) -> dict[str, str]:
    """Preloads content before user triggers request.

    Note: This is an extension attribute. To use it, you must include the preload extension.
    https://four.htmx.org/reference/attributes/hx-preload
    """
    return {f"hx-preload{':inherited' if inherited else ''}": event}


def optimistic(selector: _selector, *, inherited: bool = False) -> dict[str, str]:
    """Shows optimistic content during request.

    Note: This is an extension attribute. To use it, you must include the optimistic extension.
    https://four.htmx.org/reference/attributes/hx-optimistic
    """
    return {f"hx-optimistic{':inherited' if inherited else ''}": selector}


def status(
    status_code: str | int,
    *,
    swap: _swap_style | None = None,
    target: _selector = "",
    select: _selector = "",
    push: bool | str = "",
    replace: bool | str = "",
    transition: bool | None = None,
    inherited: bool = False,
) -> dict[str, str]:
    """Handles responses differently by status code.

    https://four.htmx.org/reference/attributes/hx-status
    """
    text: str = ""
    if swap is not None:
        text += f"swap:{swap}"
    if target:
        text += f" target:{target}"
    if select:
        text += f" select:{select}"
    if push != "":
        text += f" push:{push}"
    if replace != "":
        text += f" replace:{replace}"
    if transition is not None:
        text += f" transition:{transition}"
    return {f"hx-status:{status_code}{':inherited' if inherited else ''}": text}


def action(url: str, *, inherited: bool = False) -> dict[str, str]:
    """Specifies URL to receive request.

    https://four.htmx.org/reference/attributes/hx-action
    """
    return {f"hx-action{':inherited' if inherited else ''}": url}


def method(
    text: Literal["get", "post", "put", "patch", "delete"], *, inherited: bool = False
) -> dict[str, str]:
    """Specifies HTTP method for request.

    https://four.htmx.org/reference/attributes/hx-method
    """
    return {f"hx-method{':inherited' if inherited else ''}": text}


def config(
    *,
    timeout: int | None = None,
    credentials: str = "",
    cache: str = "",
    redirect: str = "",
    referrer: str = "",
    integrity: str = "",
    validate: bool | None = None,
    append: bool = False,
    inherited: bool = False,
) -> dict[str, str]:
    """Configures request behavior.

    https://four.htmx.org/reference/attributes/hx-config
    """
    data: dict[str, int | str | bool] = {}
    if timeout is not None:
        data["timeout"] = timeout
    if credentials:
        data["credentials"] = credentials
    if cache:
        data["cache"] = cache
    if redirect:
        data["redirect"] = redirect
    if referrer:
        data["referrer"] = referrer
    if integrity:
        data["integrity"] = integrity
    if validate is not None:
        data["validate"] = validate
    return {
        f"hx-config{':append' if append else ''}{':inherited' if inherited else ''}": json.dumps(
            data
        )
    }


def history_elt(*, inherited: bool = False) -> dict[str, str]:
    """Marks element to swap on history restore.

    https://four.htmx.org/reference/attributes/hx-history-elt
    """
    return {f"hx-history-elt{':inherited' if inherited else ''}": ""}
