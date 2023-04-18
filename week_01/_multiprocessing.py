import os
from multiprocessing import Process

# multiprocessing에서 Process를 가져와야되서 이 파일 이름을 multiprocessing으로 하면 import를 제대로 하지 못함
# 따라서 _multiprocessing.py로 파일 명 변경

# 프로세스 id (pid) : 특정 포로세스를 식별하기 위해 부여하는 고유한 번호
# getpid : 프로세스의 pid값을 가져오는 함수
# Process(target=foo).start() : foo라는 함수를 프로세스로 실행할 객체 child 생성과 동시에 실행


def foo():
    print('foo :', os.getpid())


if __name__ == '__main__':
    print('parents process :', os.getpid())
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()
    # 전부 다른 pid값이 출력됨


def foo():
    print('foo :', os.getpid())


def bar():
    print('bar :', os.getpid())


def baz():
    print('baz :', os.getpid())


if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()
    # 전부 다른 pid값이 출력됨
