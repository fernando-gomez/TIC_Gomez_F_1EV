def parabola():
    import math
    a=float(input("Dime el exponente de la x al cuadrado: "))
    b=float(input("Dime el exponente de la x: "))
    c=float(input("Dime el termino independiente: "))
    if (b*b)-4*a*c<0:
        print ("Es parabola tipo C")
        print ("No tiene solucion")
    if (b*b)-4*a*c==0:
        print ("Es parabola tipo B")
        x3=(-b+(math.sqrt((b*b)-4*a*c)))/2*a
        print ("Las solucion es: "),x3
    if (b*b)-4*a*c>0:
        print("Es parabola tipo A")
        x1=(-b+(math.sqrt((b*b)-4*a*c)))/2*a
        x2=(-b-(math.sqrt((b*b)-4*a*c)))/2*a
        print ("Las soluciones son: "),x1 ,(" y "),x2
parabola()
    
    
