class TestClass():
    tt: int = 0
    def __init__(self):
        pass

    def get_tt_by_instance_method(self):
        return TestClass.tt
    
    @classmethod
    def get_tt_by_class_method(cls):
        return cls.tt

    @classmethod
    def add_tt(cls):
        cls.tt += 1

    @staticmethod
    def add_tt2():
        TestClass.tt += 1

assert TestClass.get_tt_by_instance_method(None) == 0
TestClass.add_tt()
assert TestClass.get_tt_by_instance_method(None) == 1
TestClass.add_tt2()
assert TestClass.get_tt_by_instance_method(None) == 2


a1 = TestClass()
a1.tt = 10
assert a1.get_tt_by_instance_method() == 2

TestClass.tt = 10
assert TestClass.get_tt_by_instance_method(a1) == a1.get_tt_by_instance_method() == 10


class SubClass(TestClass):
    tt: int = 100

## 부모 클래스 변수 참조
assert SubClass.get_tt_by_instance_method(None) == 10

## 자식 클래스 변수 참조
assert SubClass.get_tt_by_class_method() == 100