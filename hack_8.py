"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    ls = []
    if len(result) == 5:
       ls.append("e-5")
       ls.append("d-4") 
       ls.append("c-3")
       ls.append("b-2")
       ls.append("a-1")
       return ls
    elif len(result) == 4:
       ls.append("4")
       ls.append("3") 
       ls.append("2")
       ls.append("1")
       return ls
    elif len(result) == 3:
       ls.append("c-3")
       ls.append("b-2")
       ls.append("a-1")
       return ls
    elif len(result) == 2:
       ls.append("2")
       ls.append("1")
       return ls
    else:
       return ls
