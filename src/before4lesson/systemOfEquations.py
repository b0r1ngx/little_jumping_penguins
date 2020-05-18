A, B = float(input()), float(input())
C, D = float(input()), float(input())
E, F = float(input()), float(input())
# Ax + By = E
# Cx + Dy = F
X = 0
Y = 0
if (A == 0 or B == 0) and (C == 0 or D == 0):
    if A == 0:
        print(F / C)  # X
        print(E / B)  # Y
    elif B == 0:
        print(E / A)
        print(F / D)
elif A == 0 or B == 0:
    if A == 0:
        Y = E / B
        print((F - D * Y) / C)
        print(Y)
    elif B == 0:
        X = E / A
        print(X)
        print((F - C * X) / D)
elif C == 0 or D == 0:
    if C == 0:
        Y = F / D
        print((E - B * Y) / A)
        print(Y)
    elif D == 0:
        X = F / C
        print(X)
        print((E - A * X) / B)
else:
    print((D * E - F * B) / (D * A - B * C))
    print((F * A - E * C) / (D * A - B * C))
# Ax + By = E
# Cx + Dy = F
