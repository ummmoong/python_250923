strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #bug(셀프선언을 안붙이면- 방어적으로 항상 self붙여서 하기)
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
