"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(result):
    ls = []
    i = 0
    while i < len(result):
        if result[i] == "a":
            ls.append("1")
        elif result[i] == "b":
            ls.append(2)
        elif result[i] == "c":
            ls.append("3")
        elif result[i] == "d":
            ls.append(4)
        elif result[i] == "e":
            ls.append("5")
        else:
            ls.append(0)
        i += 1
    return ls

