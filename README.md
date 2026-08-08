# htpy-htmx

Package containing some helpers for using [htmx](https://four.htmx.org/) with [htpy](https://htpy.dev/).

It is intended to work with htmx version 4.

## Usage

You can import htpy-htmx as hx. All normal htmx attributes are available from the module, 
but without the "hx-" prefix. So `hx-get="url"` would become `hx.get("url")`

```python
import htpy as h
import hx

# pass htmx attributes as functions
h.div("#div-id", hx.get("/some-url/"), hx.trigger("click"))

# hx-partial is also available as a htpy element
h.div("#div-id")[
    h.h2["header"],
    hx.partial("#part-id"),
]
```

## Installation

Currently not available on PyPi, but it can be installed directly from GitHub:

    pip install git+https://github.com/augustifolia/htpy-htmx.git
