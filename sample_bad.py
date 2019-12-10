import os
import sys

# TODO: clean this up later
# FIXME: this whole thing is a mess

x = 10
temp = 20
data = []
foo = "hello"

def calculate(a, b, c):
    val = a + b
    temp = val * c
    x = temp / 2
    result = []
    for i in range(10):
        if i > 2:
            if val > 5:
                if x > 1:
                    for j in range(5):
                        result.append(i + j)
    return result


def save_user(name, age, email, address, phone):
    temp = name.strip()
    data = {}
    data['name'] = temp
    data['age'] = age
    data['email'] = email
    data['address'] = address
    data['phone'] = phone
    if age > 0:
        if age < 150:
            if len(name) > 0:
                if "@" in email:
                    if len(phone) > 9:
                        print("user looks valid")
                        try:
                            # pretend we save to a file
                            with open("users.txt", "a") as f:
                                f.write(str(data))
                        except:
                            print("something went wrong")
    return data


def process(data):
    val = []
    for x in data:
        if x > 0:
            val.append(x * 2)
    return val


def run():
    foo = calculate(1, 2, 3)
    bar = process(foo)
    baz = save_user("john", 25, "john@email.com", "123 street", "1234567890")
    print(foo)
    print(bar)
    print(baz)


run()