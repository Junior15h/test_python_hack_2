"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    lent = len(result)
    if lent >= 3:
        cambio = result.replace("a","@").replace("e","3").replace("i","¡").replace("o","0").replace("u","v")
        mayuscula =  cambio[0].upper() + cambio[1:-1] + cambio[-1].upper()
        return mayuscula
    elif lent < 3:
        a = result.replace("q","Q").replace("u","v")
        return a 
    
