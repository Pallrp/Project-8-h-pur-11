#<
#>
# <= less than or equal
#>= greater than or equal
#== equal
# != not equal


band = int(input("band"))
if band == 1:
    band = True
else:
    band = False
print(band)

print(2>3) 
#returns false

#Boolean operators
#not p
#   p   not.p
#  true false
#p and q
#   p   q   p and q
# true true  true
#false false false
# true true  false
#p or q
# false ef bæði er false


#swap
a_int = 3
b_int = 2
temp = a_int
a_int = b_int
b_int = temp
print(a_int)
#returns 2
print(b_int)
#returns 3

#Líka hægt að gera svona

a_int, b_int = b_int, a_int
print(a_int)
print(b_int)

if a_int ^ b_int == 2:
    print(True)
b_int = a_int -1
if a_int ^ b_int == 2:
    print(False)
else:
    print(True)