# count
# 문자열 내에서 특정 문자가 몇개 있는지 세는 메서드
text = "Hello, world"
count = text.count('l')
print('count :', count)


# find
# 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드
position = text.find("world")
print('find :', position)


# index
# 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드(없을 경우 ValueError)
try:
    position = text.index('world')
    print('index : ', position)
except:
    print('찾는 문자열이 없습니다. ')

# join
# 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
fruits = ['apple', 'banana', 'cherry']
joined_fruits = ', '.join(fruits)
print('join :', joined_fruits)

# upper
# 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
uppercase_text = text.upper()
print('upper :', uppercase_text)

# lower
# 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
lowercase_text = text.lower()
print('lower :', lowercase_text)

# replace
# 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
replaced_text = text.replace("world", "python")
print('replace :', replaced_text)

# split
# 문자열을 특정 문자를 기준으로 나누는 메서드
fruit_text = 'apple,banana,cherry'
fruits = fruit_text.split(",")
print('split :', fruits)

# len
# 리스트의 길이를 반환하는 내장 함수
numbers = [4, 1, 3, 2, 5, 3]
print('len :', len(numbers))

# del
# 리스트에서 특정 요소를 삭제하는 연산자
del numbers[2]
print('del :', numbers)

# append
# 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
numbers.append(6)
print('append :', numbers)

# sort
# 리스트를 오름차순으로 정렬하는 메서드
numbers.sort()
print('sort :', numbers)

# reverse
# 리스트의 요소 순서를 반대로 뒤집는 메서드
numbers.reverse()
print('reverse :', numbers)

# index
# 리스트에서 즉정 요소의 인덱스를 반환하는 메서드
print('index :', fruits.index('banana'))

# insert
# 리스트의 특정 위치에 요소를 삽입하는 메서드
numbers.insert(3, 3)
print('insert :', numbers)

# remove
# 리스트에서 특정 요소를 제거하는 메서드
numbers.remove(3)
print('remove :', numbers)

# pop
# 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드
numbers.pop(2)
print('pop :', numbers)

# count
# 리스트에서 특정 요소의 개수를 세는 메서드
print('count :', numbers.count(3))

# extend
# 리스트를 확장하여 새로운 요소들을 추가하는 메서드
numbers.extend([4, 5, 6])
print('extend :', numbers)

# +=
numbers += [3, 2, 1]
print('+= :', numbers)

# 딕셔너리 초기화
empty_dict = {}
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print('dict 초기화 :', my_dict)

# 딕셔너리 쌍 추가
my_dict['grape'] = 4
print('dict 쌍 추가 :', my_dict)

# del
# 딕셔너리에서 특정 요소를 삭제
del my_dict['apple']
print('dict del :', my_dict)

# 특정 key에 해당하는 value값 얻기 (key값이 없으면 Keyerror)
print('dict key값 :', my_dict["banana"])

# keys
# 딕셔너리에서 모든 key를 리스트로 만들기
key_list = list(my_dict.keys())
print('keys :', key_list)

# values
# 딕셔너리에서 모든 value값을 리스트로 만들기
value_list = list(my_dict.values())
print('values :', value_list)

# items
# 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
person = {'name': 'John', 'age': 30, 'gender': 'male'}
items = person.items()
print('items :', items)
print('*items :', *items)

# clear
# 딕셔너리의 모든 요쇼를 삭제
person.clear()
print('clear :', person)

# get
# 딕셔너리에서 지정한 키에 대응하는 값을 반환 (키값이 없으면 None 반환)
person = {'name': 'John', 'age': 30, 'gender': 'male'}

name = person.get('name')
print('get_name :', name)

email = person.get('email')
print('get_email :', email)

email = person.get('email', 'unknown')
print('get_email_unknown :', email)

# in
# 해당 키가 딕셔너리 안에 있는지 확인
print('in_name :', 'name' in person)
print('in_email :', 'email' in person)
