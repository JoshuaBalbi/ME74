import math
def humeq(hum):
    return 1 / (1 + (.082*(math.e**(.0891*hum))))

print(humeq(30))