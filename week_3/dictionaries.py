laptop = {"make":"HP","colour":"black","weight":"1,2","year":"2022"}

print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

laptop["colour"] = "red"
laptop["year"] = "2009"

laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop["colour"]

print(laptop)

siz_laptop = laptop.copy()
print(siz_laptop)

"""
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)   
"""  