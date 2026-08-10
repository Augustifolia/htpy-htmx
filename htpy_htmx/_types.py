from typing import TypeAlias, Literal

_swap_style: TypeAlias = (
    str  # This allows extensions to add new swap_styles (like upsert and download)
    | Literal[
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
        # "upsert",  # Requires the hx-upsert extension.
        # "download",  # Required the hx-download extension.
    ]
)

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
