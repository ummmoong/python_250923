
strC = """이번에는
다중라인으로
저장합니다."""

print(strC)

strB = "python"
#슬라이싱(인덱싱)
print(strB[0:3])
print(strB[-4:-2])


print("--list--")
lst = [10, 20, 30]
print(lst)
print(len(lst))
lst.append(40)
print(lst)
lst.remove(10)
print(lst)

print("--튜플--")
tp = (10,20,30)
print(len(tp))
print(tp.index(30)) #검색만 가능, 값이 변경되지 않아야 할 때 사용
#함수 정의
def times(a,b):
    return a+b, a*b
#호출
print(times(3,4))

#한번에 여러개 입력
print("id: %s, name: %s" % ("kim","김유신"))