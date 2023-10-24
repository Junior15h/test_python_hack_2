"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result):
    co = 3
    le = len(result)
    if le > co:
        nueva = result[0] + result[1].upper() + result[2:4] + result[4].upper() + result[5:]
        return nueva
    elif le == co:
        nueva_2 = result[0] + result[1].upper() + result[2:]
        return nueva_2
    else:
        return result
    
    
