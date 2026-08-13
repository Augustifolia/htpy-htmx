from htpy_htmx import hx
import htpy as h


def test_hx_fragment() -> None:
    a = h.div("#div1")[hx.partial("#part")]
    assert str(a) == '<div id="div1"><hx-partial id="part"></hx-partial></div>'


def test_get() -> None:
    a = h.div("#div1", hx.get("/new-div/"))
    assert str(a) == '<div id="div1" hx-get="/new-div/"></div>'


def test_post() -> None:
    a = h.div("#div1", hx.post("/new-div/"))
    assert str(a) == '<div id="div1" hx-post="/new-div/"></div>'


def test_put() -> None:
    a = h.div("#div1", hx.put("/new-div/"))
    assert str(a) == '<div id="div1" hx-put="/new-div/"></div>'


def test_patch() -> None:
    a = h.div("#div1", hx.patch("/new-div/"))
    assert str(a) == '<div id="div1" hx-patch="/new-div/"></div>'


def test_delete() -> None:
    a = h.div("#div1", hx.delete("/new-div/"))
    assert str(a) == '<div id="div1" hx-delete="/new-div/"></div>'


def test_trigger() -> None:
    a = h.div("#div1", hx.trigger("click"))
    assert str(a) == '<div id="div1" hx-trigger="click"></div>'


# todo: test all attributes to hx-swap
def test_swap() -> None:
    a = h.div("#div1", hx.swap("innerHTML"))
    assert str(a) == '<div id="div1" hx-swap="innerHTML"></div>'


def test_morph_skip() -> None:
    a = h.div("#div1", hx.morph_skip())
    assert str(a) == '<div id="div1" hx-morph-skip></div>'


def test_morph_skip_children() -> None:
    a = h.div("#div1", hx.morph_skip_children())
    assert str(a) == '<div id="div1" hx-morph-skip-children></div>'


def test_target() -> None:
    a = h.div("#div1", hx.target("#div1"))
    assert str(a) == '<div id="div1" hx-target="#div1"></div>'


def test_select() -> None:
    a = h.div("#div1", hx.select("#div1"))
    assert str(a) == '<div id="div1" hx-select="#div1"></div>'


def test_on() -> None:
    a = h.div("#div1", hx.on("load", "this.showModal()"))
    assert str(a) == '<div id="div1" hx-on:load="this.showModal()"></div>'


def test_on_extended_syntax() -> None:
    a = h.div("#div1", hx.on(js="load -> this.showModal()"))
    assert str(a) == '<div id="div1" hx-on="load -&gt; this.showModal()"></div>'


def test_vals() -> None:
    a = h.div("#div1", hx.vals({"name": "test", "value": [1, 2, 3]}))
    assert (
        str(a)
        == '<div id="div1" hx-vals="{&#34;name&#34;: &#34;test&#34;, &#34;value&#34;: [1, 2, 3]}"></div>'
    )


def test_vals_js() -> None:
    a = h.div(
        "#div1",
        hx.vals(
            {"name": "test", "value": [1, 2, 3], "some_js_value": hx.JS("getSomeData()")},
            js=True,
        ),
    )
    assert (
        str(a)
        == '<div id="div1" hx-vals="js:{&#34;name&#34;: &#34;test&#34;, &#34;value&#34;: [1, 2, 3], &#34;some_js_value&#34;: getSomeData()}"></div>'
    )


def test_include() -> None:
    a = h.div("#div1", hx.include("[name='email']"))
    assert str(a) == '<div id="div1" hx-include="[name=&#39;email&#39;]"></div>'


def test_swap_oob() -> None:
    a = h.div("#div1", hx.swap_oob(True))
    assert str(a) == '<div id="div1" hx-swap-oob="true"></div>'


def test_select_oob() -> None:
    a = h.div("#div1", hx.select_oob("#alert,#sidebar:afterbegin"))
    assert str(a) == '<div id="div1" hx-select-oob="#alert,#sidebar:afterbegin"></div>'


def test_push_url() -> None:
    a = h.div("#div1", hx.push_url(True))
    assert str(a) == '<div id="div1" hx-push-url="true"></div>'


def test_replace_url() -> None:
    a = h.div("#div1", hx.replace_url(True))
    assert str(a) == '<div id="div1" hx-replace-url="true"></div>'


def test_headers() -> None:
    a = h.div("#div1", hx.headers({"my-custom-header": "my custom value"}))
    assert (
        str(a)
        == '<div id="div1" hx-headers="{&#34;my-custom-header&#34;: &#34;my custom value&#34;}"></div>'
    )


def test_headers_js() -> None:
    a = h.div("#div1", hx.headers({"my-custom-header": hx.JS("getSomeData()")}, js=True))
    assert (
        str(a)
        == '<div id="div1" hx-headers="js:{&#34;my-custom-header&#34;: getSomeData()}"></div>'
    )


def test_encoding() -> None:
    a = h.div("#div1", hx.encoding("multipart/form-data"))
    assert str(a) == '<div id="div1" hx-encoding="multipart/form-data"></div>'


def test_indicator() -> None:
    a = h.div("#div1", hx.indicator("#div1"))
    assert str(a) == '<div id="div1" hx-indicator="#div1"></div>'


def test_boost() -> None:
    a = h.div("#div1", hx.boost(True))
    assert str(a) == '<div id="div1" hx-boost="true"></div>'


def test_boost_long_form() -> None:
    a = h.div("#div1", hx.boost(swap="outerSync", select="#main", target="#main"))
    assert str(a) == '<div id="div1" hx-boost="swap:outerSync target:#main select:#main"></div>'


def test_sync() -> None:
    a = h.div("#div1", hx.sync("closest form", "replace"))
    assert str(a) == '<div id="div1" hx-sync="closest form:replace"></div>'


def test_confirm() -> None:
    a = h.div("#div1", hx.confirm("Are you sure?"))
    assert str(a) == '<div id="div1" hx-confirm="Are you sure?"></div>'


def test_validate() -> None:
    a = h.div("#div1", hx.validate())
    assert str(a) == '<div id="div1" hx-validate="true"></div>'


def test_disable() -> None:
    a = h.div("#div1", hx.disable("this"))
    assert str(a) == '<div id="div1" hx-disable="this"></div>'


def test_ignore() -> None:
    a = h.div("#div1", hx.ignore())
    assert str(a) == '<div id="div1" hx-ignore=""></div>'


def test_preserve() -> None:
    a = h.div("#div1", hx.preserve())
    assert str(a) == '<div id="div1" hx-preserve="true"></div>'


# todo: test all attributes to hx-status
def test_status() -> None:
    a = h.div("#div1", hx.status(404, swap="none"))
    assert str(a) == '<div id="div1" hx-status:404="swap:none"></div>'


def test_status_string() -> None:
    a = h.div("#div1", hx.status("5xx", swap="none"))
    assert str(a) == '<div id="div1" hx-status:5xx="swap:none"></div>'


def test_action() -> None:
    a = h.div("#div1", hx.action("/some-url/"))
    assert str(a) == '<div id="div1" hx-action="/some-url/"></div>'


def test_method() -> None:
    a = h.div("#div1", hx.method("get"))
    assert str(a) == '<div id="div1" hx-method="get"></div>'


def test_config() -> None:
    a = h.div("#div1", hx.config(validate=True))
    assert str(a) == '<div id="div1" hx-config="{&#34;validate&#34;: true}"></div>'


def test_history_elt() -> None:
    a = h.div("#div1", hx.history_elt())
    assert str(a) == '<div id="div1" hx-history-elt=""></div>'
