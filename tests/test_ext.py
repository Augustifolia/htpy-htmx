import htpy as h
from htpy_htmx import ext


def test_multipart() -> None:
    a = h.div("#div1", ext.multipart(connect="/some-url", close="contextmenu"))
    assert (
        str(a)
        == '<div id="div1" hx-multipart:connect="/some-url" hx-multipart:close="contextmenu"></div>'
    )


def test_sse() -> None:
    a = h.div("#div1", ext.sse(connect="/some-url"))
    assert str(a) == '<div id="div1" hx-sse:connect="/some-url"></div>'


def test_ws() -> None:
    a = h.div("#div1", ext.ws(connect="focus"))
    assert str(a) == '<div id="div1" hx-ws:connect="focus"></div>'


def test_live() -> None:
    a = h.div("#div1", ext.live("text", "'Hello, ' + q('previous input').value"))
    assert (
        str(a)
        == '<div id="div1" hx-live:text="&#39;Hello, &#39; + q(&#39;previous input&#39;).value"></div>'
    )


def test_optimistic() -> None:
    a = h.div("#div1", ext.optimistic("#liked-state"))
    assert str(a) == '<div id="div1" hx-optimistic="#liked-state"></div>'


def test_browser_indicator() -> None:
    a = h.div("#div1", ext.browser_indicator(True))
    assert str(a) == '<div id="div1" hx-browser-indicator="true"></div>'


def test_prompt() -> None:
    a = h.div("#div1", ext.prompt("Reason?"))
    assert str(a) == '<div id="div1" hx-prompt="Reason?"></div>'


def test_preload() -> None:
    a = h.div("#div1", ext.preload("mouseenter"))
    assert str(a) == '<div id="div1" hx-preload="mouseenter"></div>'


def test_ptag() -> None:
    a = h.div("#div1", ext.ptag("v42"))
    assert str(a) == '<div id="div1" hx-ptag="v42"></div>'


def test_history() -> None:
    a = h.div("#div1", ext.history(True))
    assert str(a) == '<div id="div1" hx-history="true"></div>'


def test_head() -> None:
    a = h.div("#div1", ext.head("append"))
    assert str(a) == '<div id="div1" hx-head="append"></div>'


def test_targets() -> None:
    a = h.div("#div1", ext.targets("#div1", "#div2"))
    assert str(a) == '<div id="div1" hx-targets="#div1, #div2"></div>'


def test_nonce() -> None:
    a = h.div("#div1", ext.nonce("some string"))
    assert str(a) == '<div id="div1" hx-nonce="some string"></div>'
