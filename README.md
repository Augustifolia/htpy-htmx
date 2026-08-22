# htpy-htmx

htpy-htmx is a library to make it easier to work with [htmx](https://four.htmx.org/) in [htpy](https://htpy.dev/).

This library is intended to work with htmx 4.

Note: This project is still a work in progress and there may be breaking changes.

## Usage

You can import htpy-htmx as htpy_htmx.hx. All normal htmx attributes are available from the module,
but without the "hx-" prefix. So `hx-get="url"` would become `hx.get("url")`.

Some htmx extension attributes are available in the htpy_htmx.ext module.

```python
import htpy as h
from htpy_htmx import hx
from htpy_htmx import ext

# pass htmx attributes as functions
h.div("#div-id", hx.get("/some-url/"), hx.trigger("click"))

# hx-partial is also available as a htpy element
h.div("#div-id")[
    h.h2["header"],
    hx.partial("#part-id", hx.target("#some-element"))[
        h.div("#div1")[
            h.p["part one"]
        ]
    ],
]

h.div(
    # trigger allows a list of trigger events
    hx.trigger("blur", "keyup[key=='Enter']"),
    # swap takes a swap style as string and modifiers as keyword arguments
    hx.swap("before", swap="1s", scroll="bottom"),
    # hx-on takes an event and a JavaScript expression
    hx.on("htmx:before:request", "showSpinner()"),
    # vals takes a dict of data.
    # To evaluate JavaScript, wrap your js expression in hx.JS() and pass js=True.
    hx.vals({"foo": "bar", "some_js": hx.JS("getSomeData()")}, js=True),
)

# to enable inheritance pass inherited=True to a hx-function
h.div(hx.confirm("Are you sure?", inherited=True))[
    h.button(hx.delete("/account"))["Delete My Account"],
    h.button(hx.put("/account"))["Update My Account"],
]

# Some extension attributes are available in ext:
h.div(
    ext.preload("touchstart"),
    ext.optimistic("#msg-opt"),
    ext.ws(connect="click"),
)
```

## Installation

To install with pip run:

    pip install htpy-htmx
