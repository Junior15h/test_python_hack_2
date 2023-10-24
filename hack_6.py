"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    ls = []
    for i in result:
        if i == "a":
            ls.append("1")
        elif i =="c":
            ls.append("3")
        elif i =="e":
            ls.append("5")
        else:
            ls.append("-")
        
    if len(result) == 0:
        ls.append("0")
    else:
        nada = []
    return ls
  
