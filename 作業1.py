import cmath

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
       
        root = -b / (2*a)
        return root, root
    else:
       
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


a = 1
b = -3
c = 2

root1, root2 = solve_quadratic(a, b, c)
print("Root 1:", root1)
print("Root 2:", root2)