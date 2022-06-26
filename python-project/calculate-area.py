#Application of function in 2D


def square() :
  s = float(input("Type side : "))
  a = s*s
  print("The Area is :  %f" %a)

def circle() :
  r = float(input("Input Radius : "))
  a = 22*r*r/7
  print("The Area of the circle %f" %a)

def rectangle() :
  l = float(input("Input length : "))
  w = float(input( "Input width : "))
  a = l*w
  print("The Area of the rectangle %f" %a)

def triangle() :
  a = float(input("Input base : "))
  t = float(input("Input Height : "))
  lu = a*t/2
  print("The Area of the triangle %f" %lu)

def parallelogram() :
  b = float(input("Input alas  : "))
  t = float(input("Input tinggi : "))
  a = b*t
  print("The Area of the parallelogram %f" %a)

def kite() :
  d1 = float(input("Input diagonal 1 : "))
  d2 = float(input("input diagonal 2 : "))
  a = d1*d2/2
  print("The Area of the kite %f" %a)

def split_rhombus() :
  d1 = float(input("Input diagonal 1 : "))
  d2 = float(input("input diagonal 2 : "))
  a = d1*d2/2
  print("The Area of the split rhombus %f" %a)

print("Applicaticon of Area in 2D")
print("1. Square")
print("2. Circle")
print("3. Rectangle")
print("4. Triangle")
print("5. parallelogram")
print("6. Kite")
print("7. Split rhombus")

choose = int(input("Choose one from the above : "))
if choose == 1 :
  square()
elif choose == 2 :
  circle()
elif choose == 3 :
  rectangle()
elif choose == 4 :
  triangle()
elif choose == 5 :
  parallelogram()
elif choose == 6 :
  kite()
elif choose == 7 :
  split_rhombus()
else :
  print("Not in the system")
