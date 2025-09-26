value =5
while value >0:
    print(value)
    value -= 1

    print("---for루프---")
    for i in range(5,0,-1):
        print(i)
    print("---딕셔너리 for루프---")
    for item in {"apple":100, "banana":200}:

    d = {"apple":100, "banana":200}
    for item in d.items():
        print(item)