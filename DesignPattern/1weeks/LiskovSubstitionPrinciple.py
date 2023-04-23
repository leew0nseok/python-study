# 자료형 S가 자료형 T의 하위형이라면 필요한 프로그램의 속성(정확성, 수행하는 업무 등)의 변경 없이 자료형 T의 객체를 자료형 S의 객체로 교체(치환)할 수 있어야 한다는 원칙
class Cat():
    def speak(self):
        print("meow")

class BlackCat(Cat):
    def speak(self):
        print("black meow")

def speak(cat:Cat):
    cat.speak()

cat = Cat()
speak(cat)

cat = BlackCat()
speak(cat)