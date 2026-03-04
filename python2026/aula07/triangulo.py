LADOA = "LADO A = "
LADOB = "LADO B = "
LADOC = "LADO C = "
print("digite a medida do triangulo X")
ax = float(input(LADOA))
bx = float(input(LADOB))
cx = float(input(LADOC))
print("digite a medida do triangulo Y")
ay = float(input(LADOA))
by = float(input(LADOB))
cy = float(input(LADOC))

px = (ax + bx + cx) / 2
py = (ay + by + cy) / 2
areax = (px * (px - ax) * (px * bx) * (px * cx))**0.5
areay = (px * (py - ay) * (py * by) * (py * cy))**0.5

print(f"area do triangulo x: {areax:.4f}")
print(f"area do triangulo y: {areay:.4f}")
