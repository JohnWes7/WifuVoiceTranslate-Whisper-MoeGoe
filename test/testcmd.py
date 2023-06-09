# print("test cmd")
import urllib.request
# a = input("test input\n")
# print(a)

temp = 5

def start():
    global temp

    print(temp)
    temp += 5


def get():
    return temp

start()
print(temp)
urllib.request.install_opener