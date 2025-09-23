import random
from os.path import *

print("==랜덤모듈--")
print(random.random())  # 0.0 ~ 1.0 사이의 임의의 실수
print(random.randint(1, 10))  # 1 ~ 10 사이의 임의의 정수
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))  # 0 ~ 19 사이의 임의의 정수


filePath = "C:/python310/python.exe"

import os
print("==os.path 모듈==")
print("os명:", os.name)
print(os.getcwd())  # 현재 작업 디렉터리
os.system("notepad.exe")