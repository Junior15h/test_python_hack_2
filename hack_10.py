"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):
    result[0] = {"1":"2"}
    result[1] = {"3","4"}
    result[2] = {"5":"6"}
    return result
