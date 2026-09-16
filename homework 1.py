import math
def angle_sin_cos():
    for k in range(11):
        a = k * math.pi / 5 
        sin = math.sin(a)
        cos = math.cos(a)
        print(f'{a}, {sin}, {cos}')
angle_sin_cos()