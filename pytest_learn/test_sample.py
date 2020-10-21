import pytest@


def func(x):
    return x+1

@pytest.mark.parametrize('a,b', [         #参数化
    (1,2),
    (3,19),
    ('a','a1'),
    (3,4),
    (5,6)
])
def test_answear(a,b):                    #用pytest解释器运行
    assert func(a) == b




@pytest.fixture()                         #用在类中，某些类需要调用外部方法，某些类不需要调用
def login():
    usename = "ssss"
    return usename

class TestDemo:
    def test_a(self,login):
        print(f"a   login = {login}")

    def test_b(self):
        print("b")

if __name__ == '__main__':               #用python解释器运行
    pytest.main(['test_sample.py'])