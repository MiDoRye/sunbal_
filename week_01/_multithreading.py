import threading
import os


def foo():
    print('thread id :', threading.get_native_id())
    print('process id :', os.getpid())


if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()
    # 같은 프로세스 id가 출력됨
    # 가끔씩 순서가 다르게 출력? -> 스레드가 같이 실행되는 거니까 그래서 그런가


def foo():
    print('foo :', threading.get_native_id())


def bar():
    print('bar :', threading.get_native_id())


def baz():
    print('baz :', threading.get_native_id())


if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()
    # 다른 스레드에서 실행되기 때문에 다른 id 출력됨
