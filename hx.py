import json
from typing import Literal, TypeAlias, Any, TypedDict

from htpy import Element

partial = Element("hx-partial")


_selector: TypeAlias = (
    str
    | Literal["this"]
    | Literal["next"]
    | Literal["previous"]
    | Literal["body"]
    | Literal["document"]
    | Literal["window"]
    | Literal["host"]
)

# todo: add support for :inherited


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


def trigger(text: str) -> dict[str, str]:
    """Controls when element issues requests.

    https://four.htmx.org/reference/attributes/hx-trigger
    """
    return {"hx-trigger": text}


_SwapStyle: TypeAlias = (
    Literal["innerHTML"]
    | Literal["outerHTML"]
    | Literal["beforebegin"]
    | Literal["before"]
    | Literal["afterbegin"]
    | Literal["prepend"]
    | Literal["beforeend"]
    | Literal["append"]
    | Literal["afterend"]
    | Literal["after"]
    | Literal["delete"]
    | Literal["none"]
    | Literal["innerMorph"]
    | Literal["outerMorph"]
    | Literal["textContent"]
    | Literal["outerSync"]
    | Literal["upsert"]  # Requires the hx-upsert extension.
)


def swap(
    style: _SwapStyle,
    transition: bool | None = None,
    swap: str = "",
    settle: str = "",
    ignoreTitle: bool | None = None,
    scroll: Literal["top"] | Literal["bottom"] | str = "",
    scrollTarget: str = "",
    show: Literal["top"] | Literal["bottom"] | Literal["none"] | str = "",
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


# todo: decide whether this is correct and should be included
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


def on(event: str = "", js: str = "") -> dict[str, str]:
    """Runs inline JavaScript when event fires.

    https://four.htmx.org/reference/attributes/hx-on
    """
    return {f"hx-on{":" + event if event else ""}": SafeString(js)}


# todo: figure out how to handle js attributes in data.
#  Currently they have "" around them that needs to be removed somehow
def vals(
    data: dict[str, Any], js: bool = False, append: bool = False
) -> dict[str, str]:
    """Adds values to request parameters.

    https://four.htmx.org/reference/attributes/hx-vals
    """
    data_string = json.dumps(data)
    return {
        f"hx-vals{":append" if append else ""}": f"{"js:" if js else ""}{data_string}"
    }


def include(selector: _selector, append: bool = False) -> dict[str, str]:
    """Includes additional element values in request.

    https://four.htmx.org/reference/attributes/hx-include
    """
    return {f"hx-include{":append" if append else ""}": selector}


def swap_oob(text: str | bool) -> dict[str, str]:
    """Marks response elements to swap into page by ID.

    https://four.htmx.org/reference/attributes/hx-swap-oob
    """
    if isinstance(text, bool):
        text = str(text).lower()
    return {"hx-swap-oob": text}


def select_oob(text: str) -> dict[str, str]:
    """Picks response elements to swap into page by ID.

    https://four.htmx.org/reference/attributes/hx-select-oob
    """
    return {"hx-select-oob": text}


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


# todo: as for vals, we need to handle js attributes properly
def headers(data: dict[str, Any], js: bool = False) -> dict[str, str]:
    """Adds custom headers to request.

    https://four.htmx.org/reference/attributes/hx-headers
    """
    return {"hx-headers": f"{"js:" if js else ""}{json.dumps(data)}"}


def encoding(text: str | Literal["application/x-www-form-urlencoded"] | Literal["multipart/form-data"]) -> dict[str, str]:
    """Sets request encoding type.

    https://four.htmx.org/reference/attributes/hx-encoding
    """
    return {"hx-encoding": text}


def indicator(selector: _selector, append: bool = False) -> dict[str, str]:
    """Specifies loading indicator element.

    https://four.htmx.org/reference/attributes/hx-indicator
    """
    return {f"hx-indicator{":append" if append else ""}": selector}


def boost(text: str | bool) -> dict[str, str]:
    """Converts links and forms to AJAX.

    https://four.htmx.org/reference/attributes/hx-boost
    """
    if isinstance(text, bool):
        text = str(text).lower()
    return {"hx-boost": text}


def sync(
    selector: _selector,
    strategy: (
        Literal["drop"]
        | Literal["abort"]
        | Literal["replace"]
        | Literal["queue first"]
        | Literal["queue last"]
        | Literal["queue all"]
    ),
) -> dict[str, str]:
    """Synchronizes requests between elements.

    https://four.htmx.org/reference/attributes/hx-sync
    """
    return {"hx-sync": f"{selector}:{strategy}"}


def confirm(text: str) -> dict[str, str]:
    """Shows confirmation dialog before request.

    https://four.htmx.org/reference/attributes/hx-confirm
    """
    return {"hx-confirm": text}


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
    text: Literal["mouseenter"] | Literal["mouseover"] | Literal["touchstart"],
) -> dict[str, str]:
    """Preloads content before user triggers request.

    Note: This is an extension attribute. To use it, you must include the preload extension.
    https://four.htmx.org/reference/attributes/hx-preload
    """
    return {"hx-preload": text}


def optimistic(text: str) -> dict[str, str]:
    """Shows optimistic content during request.

    Note: This is an extension attribute. To use it, you must include the optimistic extension.
    https://four.htmx.org/reference/attributes/hx-optimistic
    """
    return {"hx-optimistic": text}


# todo: update signature
def status(status_code: str | int, text: str) -> dict[str, str]:
    """Handles responses differently by status code.

    https://four.htmx.org/reference/attributes/hx-status
    """
    return {f"hx-status:{status_code}": text}


def action(text: str) -> dict[str, str]:
    """Specifies URL to receive request.

    https://four.htmx.org/reference/attributes/hx-action
    """
    return {"hx-action": text}


def method(
    text: (
        Literal["get"]
        | Literal["post"]
        | Literal["put"]
        | Literal["patch"]
        | Literal["delete"]
    ),
) -> dict[str, str]:
    """Specifies HTTP method for request.

    https://four.htmx.org/reference/attributes/hx-method
    """
    return {"hx-method": text}


class _ConfigData(TypedDict):
    timeout: int
    credentials: str
    cache: str
    redirect: str
    referrer: str
    integrity: str
    validate: bool


# todo: make the keys in _ConfigData optional
def config(data: _ConfigData, append: bool = False) -> dict[str, str]:
    """Configures request behavior.

    https://four.htmx.org/reference/attributes/hx-config
    """
    return {f"hx-config{":append" if append else ""}": json.dumps(data)}


def history_elt() -> dict[str, str]:
    """Marks element to swap on history restore.

    https://four.htmx.org/reference/attributes/hx-history-elt
    """
    return {"hx-history-elt": ""}
