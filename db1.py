import sqlite3

#연결객체 생성(임시로 메모리에 저장, 일단 메모리에서 작업)
con = sqlite3.connect(":memory:") #하드에 저장하지 않고 메모리에 저장, 저장안함
#SQL구문을 실행할 커서 객체 리턴 (전역함수)
cur = con.cursor()
#테이블 스키마 생성
cur.execute( #스키마 생성
    "CREATE table PhoneBook (name text, phoneNum text);")
#데이터 삽입
cur.execute("INSERT INTO PhoneBook (name, phoneNum) values (?,?);",
            ("Alice","010-222-1234"))

for row in cur.execute("SELECT * FROM PhoneBook;"):
    print(row) 