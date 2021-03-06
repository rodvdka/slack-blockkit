"""
Test composition objects.
"""

from slack_blockkit.composition_object import (
    ConfirmObject,
    MarkdownTextObject,
    OptionGroupObject,
    OptionObject,
    PlainTextObject,
    TextObject,
)


def test_plain_text_object(plain_text_object: PlainTextObject):
    assert plain_text_object.render() == {
        "type": TextObject.BTYPE_PLAINTEXT,
        "text": plain_text_object.text,
        "emoji": plain_text_object.emoji,
    }


def test_markdown_text_object(markdown_text_object: MarkdownTextObject):
    assert markdown_text_object.render() == {
        "type": markdown_text_object.btype,
        "text": markdown_text_object.text,
        "verbatim": markdown_text_object.verbatim,
    }


def test_confirm_object(confirm_object: ConfirmObject):
    assert confirm_object.render() == {
        "title": confirm_object.title.render(),
        "text": confirm_object.text.render(),
        "confirm": confirm_object.confirm.render(),
        "deny": confirm_object.deny.render(),
        "style": confirm_object.style,
    }


def test_option_object(option_object: OptionObject):
    assert option_object.render() == {
        "text": option_object.text.render(),
        "value": option_object.value,
        "url": option_object.url,
    }


def test_option_group_object(option_group_object: OptionGroupObject):
    assert option_group_object.render() == {
        "label": option_group_object.label.render(),
        "options": [item.render() for item in option_group_object.options],
    }
