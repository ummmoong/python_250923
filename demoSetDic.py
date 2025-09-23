#demoSetDic

print("---set형식---")
a = {1,2,3,4}
b = {3,4,4,5}

print(a)
print(b)
print(a.union(b))

print("---dic형식---")
fruits = {"apple":100, "orange":200}
print(len(fruits))
print(fruits["apple"])
fruits["kiwi"]=150
fruits["apple"]=300
print(fruits)
del fruits["kiwi"]
print(fruits)

for item in fruits.items():
    print(item)

    