def my_coroutine():
    while True:
        value = yield
        print('Received value:', value)


# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행 준비
next(co)

# 값을 보내기
co.send('Hello, world!')

# ======================================================================================


def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# ======================================================================================


def my_coroutine():
    while True:
        x = yield
        print('Received :', x)


co = my_coroutine()
next(co)

co.send(10)
co.send(20)
co.send(30)

# ======================================================================================

phone_book = {'John': '123-4567', 'Jane': '234-5678', 'Max': '345-6789'}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = 'Cannot find the name in the phone book.'
        name = yield phone_number


search_coroutine = search()
next(search_coroutine)

result = search_coroutine.send('John')
print(result)

result = search_coroutine.send('Jane')
print(result)

result = search_coroutine.send('Sarah')
print(result)
