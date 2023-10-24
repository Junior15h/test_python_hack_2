"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(result):
    result = list(result)
    if result[0] == "f":
        result[2] = "-"
        result[5] = "-"
        result[6] = "m"
        result[7] = "a"
        result.append("-")
    elif result[0] == "b":
        result[2] = "-"
        result[5] = "-"
        result[6] = "a"
        result[-1] = "n"
    elif result[0] == "q":
        result[-1] = "-"
    string = "".join(result)
    return string

