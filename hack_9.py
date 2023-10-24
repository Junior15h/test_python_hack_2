"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    del result["bar"]
    new = {k.capitalize(): v.capitalize() for k, v in   result.items()}
    for i in new:
        new[i]  = new[i].replace("k", "")
    return new
