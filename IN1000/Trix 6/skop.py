a = "En tekst!"
def prosedyre_en(parameter):
    parameter = parameter + "12"

prosedyre_en(a)
print (a)

b = 10
print (b)
# En tekst! og 10.

def prosedyre_to():
    b = b + 10

prosedyre_to()
print(b)
# Error.

c = "hei"
print (c)

def funksjon_en(parameter):
    parameter = parameter + "verden"
    return parameter

print (funksjon_en(c))
# Error.
