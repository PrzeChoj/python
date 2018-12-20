import math

t = [0, 7, 1, 2, math.nan, 4, 5]

wynikie = [l for l in t if l is not math.nan]
print(wynikie)