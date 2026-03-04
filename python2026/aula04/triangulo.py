a = float(input("digite o valor de a"))
b = float(input("digite o valor de b"))
c = float(input("digite o valor de c"))


if (a + b > c) and (a + c > b) and (b + c > a):
    perimetro = a + b + c
    print(f"o perimetro é {perimetro}")
    
else:
    area = ((a + b) * c) / 2
    print(f"a area do trapezio é {area}")

