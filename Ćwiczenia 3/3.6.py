import math
def promien_okregu(x = 0, y = 0, a = 0, b = 0):
    return math.sqrt((x - a)**2 + (y - b)**2)
print(promien_okregu())
print(promien_okregu(2,2,2,2))
print(promien_okregu(2, 2, b = 2, a = 1))
print(promien_okregu(b = 5, x = 2, y = 2, a = 6))
print(promien_okregu(b = 5, a = 6))
