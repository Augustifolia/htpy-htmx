from __future__ import annotations
import json
from typing import Literal, TypeAlias, Any, overload

from htpy import Element

partial = Element("hx-partial")


_selector: TypeAlias = (
    str | Literal["this", "next", "previous", "body", "document", "window", "host"]
)

# todo: add support for :inherited

# todo: decide what to do with stuff that requires extensions,
# it would probably be reasonable to include include helpers for the included extensions in htmx.
# another option would be to have all stuff related to extensions in a separate file.


class SafeString(str):
    def __html__(self) -> SafeString:
        return self

    def __str__(self) -> SafeString:
        return self


def get(url: str) -> dict[str, str]:
    """Issues GET request to specified URL.

    https://four.htmx.org/reference/attributes/hx-get
    """
    return {"hx-get": url}


def post(url: str) -> dict[str, str]:
    """Issues POST request to specified URL.

    https://four.htmx.org/reference/attributes/hx-post
    """
    return {"hx-post": url}


def put(url: str) -> dict[str, str]:
    """Issues PUT request to specified URL.

    https://four.htmx.org/reference/attributes/hx-put
    """
    return {"hx-put": url}


def patch(url: str) -> dict[str, str]:
    """Issues PATCH request to specified URL.

    https://four.htmx.org/reference/attributes/hx-patch
    """
    return {"hx-patch": url}


def delete(url: str) -> dict[str, str]:
    """Issues DELETE request to specified URL.

    https://four.htmx.org/reference/attributes/hx-delete
    """
    return {"hx-delete": url}


def trigger(*event: str) -> dict[str, str]:
    """Controls when element issues requests.

    https://four.htmx.org/reference/attributes/hx-trigger
    """
    return {"hx-trigger": ", ".join(event)}


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
    return {"hx-swap": text}


def morph_skip() -> dict[str, bool]:
    """Skip morphing with attributes and children"""
    return {"hx-morph-skip": True}


def morph_skip_children() -> dict[str, bool]:
    """Skip morphing with children only; attributes still morph"""
    return {"hx-morph-skip-children": True}


def target(selector: _selector) -> dict[str, str]:
    """Controls where response is inserted.

    https://four.htmx.org/reference/attributes/hx-target
    """
    return {"hx-target": selector}


def targets(*selector: _selector) -> dict[str, str]:
    """Target many elements.

    Requires the hx-targets extension
    https://four.htmx.org/extensions/hx-targets
    """
    return {"hx-targets": ", ".join(selector)}


def select(selector: _selector) -> dict[str, str]:
    """Controls which response part is inserted.

    https://four.htmx.org/reference/attributes/hx-select
    """
    return {"hx-select": selector}


@overload
def on(event: str, js: str) -> dict[str, str]:
    pass


@overload
def on(*, js: str) -> dict[str, str]:
    pass


def on(event: str = "", js: str = "") -> dict[str, str]:
    """Runs inline JavaScript when event fires.

    https://four.htmx.org/reference/attributes/hx-on
    """
    return {f"hx-on{':' + event if event else ''}": SafeString(js)}


class JS:
    """Used to mark strings as js expressions for use in hx-vals and hx-headers."""
    start = 'HXJS-start:'
    end = ':HXJS-end'
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{JS.start}{self.value}{JS.end}"


class _HTMXJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, JS):
            return str(o)
            # Let the base class default method raise the TypeError
        return super().default(o)

    def encode(self, o: Any) -> str:
        string: str = super().encode(o)
        string = string.replace(f'"{JS.start}',  "").replace(f'{JS.end}"', "")
        return string


def vals(data: dict[str, Any], js: bool = False, append: bool = False) -> dict[str, str]:
    """Adds values to request parameters.

    https://four.htmx.org/reference/attributes/hx-vals
    """
    data_string = json.dumps(data, cls=_HTMXJSONEncoder)
    return {f"hx-vals{':append' if append else ''}": f"{'js:' if js else ''}{data_string}"}


def include(selector: _selector, append: bool = False) -> dict[str, str]:
    """Includes additional element values in request.

    https://four.htmx.org/reference/attributes/hx-include
    """
    return {f"hx-include{':append' if append else ''}": selector}


def swap_oob(swap_style: _swap_style | bool = True, selector: _selector = "") -> dict[str, str]:
    """Marks response elements to swap into page by ID.

    https://four.htmx.org/reference/attributes/hx-swap-oob
    """
    if isinstance(swap_style, bool):
        style: str = str(swap_style).lower()
    else:
        style = str(swap_style)
    return {"hx-swap-oob": f"{style}{':' + selector if selector else ''}"}


def select_oob(*selector: str) -> dict[str, str]:
    """Picks response elements to swap into page by ID.

    https://four.htmx.org/reference/attributes/hx-select-oob
    """
    return {"hx-select-oob": ", ".join(selector)}


def push_url(push: bool = True) -> dict[str, str]:
    """Pushes URL into browser history.

    https://four.htmx.org/reference/attributes/hx-push-url
    """
    return {"hx-push-url": str(push).lower()}


def replace_url(replace: bool = True) -> dict[str, str]:
    """Replaces current URL in browser history.

    https://four.htmx.org/reference/attributes/hx-replace-url
    """
    return {"hx-replace-url": str(replace).lower()}


def headers(data: dict[str, Any], js: bool = False) -> dict[str, str]:
    """Adds custom headers to request.

    https://four.htmx.org/reference/attributes/hx-headers
    """
    return {"hx-headers": f"{'js:' if js else ''}{json.dumps(data, cls=_HTMXJSONEncoder)}"}


def encoding(
    encoding_string: str | Literal["application/x-www-form-urlencoded", "multipart/form-data"],
) -> dict[str, str]:
    """Sets request encoding type.

    https://four.htmx.org/reference/attributes/hx-encoding
    """
    return {"hx-encoding": encoding_string}


def indicator(selector: _selector, append: bool = False) -> dict[str, str]:
    """Specifies loading indicator element.

    https://four.htmx.org/reference/attributes/hx-indicator
    """
    return {f"hx-indicator{':append' if append else ''}": selector}


@overload
def boost(boost: bool) -> dict[str, str]:
    pass


@overload
def boost(
    *, swap: _swap_style | str = "", target: _selector = "", select: _selector = ""
) -> dict[str, str]:
    pass


def boost(
    boost: bool | None = None,
    *,
    swap: _swap_style | str = "",
    target: _selector = "",
    select: _selector = "",
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
    return {"hx-boost": text}


def sync(
    selector: _selector,
    strategy: Literal["drop", "abort", "replace", "queue first", "queue last", "queue all"],
) -> dict[str, str]:
    """Synchronizes requests between elements.

    https://four.htmx.org/reference/attributes/hx-sync
    """
    return {"hx-sync": f"{selector}:{strategy}"}


def confirm(confirmation_prompt: str) -> dict[str, str]:
    """Shows confirmation dialog before request.

    https://four.htmx.org/reference/attributes/hx-confirm
    """
    return {"hx-confirm": confirmation_prompt}


def validate(validate: bool = True) -> dict[str, str]:
    """Validates before submitting request.

    https://four.htmx.org/reference/attributes/hx-validate
    """
    return {"hx-validate": str(validate).lower()}


def disable(selector: _selector) -> dict[str, str]:
    """Disables elements during request.

    https://four.htmx.org/reference/attributes/hx-disable
    """
    return {"hx-disable": selector}


def ignore() -> dict[str, str]:
    """Disables htmx processing for element.

    https://four.htmx.org/reference/attributes/hx-ignore
    """
    return {"hx-ignore": ""}


def preserve() -> dict[str, str]:
    """Preserves element during swaps.

    https://four.htmx.org/reference/attributes/hx-preserve
    """
    return {"hx-preserve": "true"}


def preload(
    event: Literal["mouseenter", "mouseover", "touchstart"],
) -> dict[str, str]:
    """Preloads content before user triggers request.

    Note: This is an extension attribute. To use it, you must include the preload extension.
    https://four.htmx.org/reference/attributes/hx-preload
    """
    return {"hx-preload": event}


def optimistic(selector: _selector) -> dict[str, str]:
    """Shows optimistic content during request.

    Note: This is an extension attribute. To use it, you must include the optimistic extension.
    https://four.htmx.org/reference/attributes/hx-optimistic
    """
    return {"hx-optimistic": selector}


# todo: update signature
def status(status_code: str | int, text: str) -> dict[str, str]:
    """Handles responses differently by status code.

    https://four.htmx.org/reference/attributes/hx-status
    """
    return {f"hx-status:{status_code}": text}


def action(url: str) -> dict[str, str]:
    """Specifies URL to receive request.

    https://four.htmx.org/reference/attributes/hx-action
    """
    return {"hx-action": url}


def method(
    text: Literal["get", "post", "put", "patch", "delete"],
) -> dict[str, str]:
    """Specifies HTTP method for request.

    https://four.htmx.org/reference/attributes/hx-method
    """
    return {"hx-method": text}


def config(
    timeout: int | None = None,
    credentials: str = "",
    cache: str = "",
    redirect: str = "",
    referrer: str = "",
    integrity: str = "",
    validate: bool | None = None,
    append: bool = False,
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
    return {f"hx-config{':append' if append else ''}": json.dumps(data)}


def history_elt() -> dict[str, str]:
    """Marks element to swap on history restore.

    https://four.htmx.org/reference/attributes/hx-history-elt
    """
    return {"hx-history-elt": ""}
