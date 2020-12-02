import time
import json
from threading import Thread


try:
    with open('file.json') as f:
        name = json.load(f)
except:
    f = open("file.json", "w+")
    name = {}


def create(k, v, t='0'):
    if k in name:
        print("ERROR:The data already exists")
    else:
        if k.isalpha():
            if v.isnumeric() and t.isnumeric():
                v = int(v)
                t = int(t)
                if len(name) < (1024 * 1020 * 1024) and v <= (16 * 1024 * 1024):
                    if t == 0:
                        p = [v, t]
                    else:
                        p = [v, time.time() + t]
                    if len(k) <= 32:
                        name[k] = p
                        print("Key is created")
                        with open('file.json', 'w') as json_file:
                            json.dump(name, json_file)
                    else:
                        print("ERROR:Key length Exceeded")
                        time_limit()
                else:
                    print("ERROR:MEMORY Exceeded!!!")
                    time_limit()
            else:
                print("ERROR:INVALID INPUT (NUMERIC ONLY)")
                time_limit()
        else:
            print("ERROR:INVALID KEY INPUT (ALPHABETS ONLY)")
            time_limit()
    menu()


def read(k):
    if k not in name:
        print("ERROR:Key does not exists Enter a valid key!!")
    else:
        m = name[k]
        if m[1] != 0:
            if time.time() < m[1]:
                print ( k + "-" + str(m[0]))
            else:
                print("ERROR: " + k + " Time expired")
        else:
            print(k + "-" + str(m[0]))
            with open('file.json', 'w') as js:
                json.dump(name, js)
    menu()


def delete(k):
    if k not in name:
        print("ERROR:Key does not exists Enter a valid key!!")
    else:
        m = name[k]
        if m[1] != 0:
            if time.time() < m[1]:
                del name[k]
                print("Key (" + k + ") is deleted")
                with open('file.json', 'w') as js:
                    json.dump(name, js)
            else:
                print("ERROR:ERROR: " + k + " Time expired")
        else:
            del name[k]
            print("Key (" + k + ") is deleted")
            with open('file.json', 'w') as js:
                json.dump(name, js)
    menu()


def time_limit():
    print("Enter your choice If key need time limit Enter Y or N")
    o = input()
    if o.isalpha():
        if o == 'Y' or o == 'y':
            print("Enter the KEY,VALUE,TIME")
            create(input(), input(), input())
        elif o == 'N' or o == 'n':
            print("Enter the KEY,VALUE")
            create(input(), input())
        else:
            print("ERROR:Enter a valid input")
            time_limit()
    else:
        print("ERROR:Enter a valid input")
        time_limit()


def menu():
    print("Enter your choice:-1,2,3,4")
    print(" 1.Create \n 2.Read \n 3.Delete \n 4.Quit")
    global i
    i = input()
    if i.isnumeric():
        if int(i) == 1:
            time_limit()
        elif int(i) == 2:
            if name == {}:
                print("FILE IS EMPTY")
                menu()
            else:
                read(input("Enter the key you want to read: "))
        elif int(i) == 3:
            if name == {}:
                print("FILE IS EMPTY")
                menu()
            else:
                delete(input("Enter the key to be deleted: "))
        elif int(i) == 4:
            with open('file.json', 'w') as js:
                json.dump(name, js)
            quit()
        else:
            print("ERROR enter a valid input")
            menu()

    else:
        print("ERROR enter a valid input")
        menu()

if __name__ == '__main__':
    t1 = Thread(target=menu(), daemon=True)
    t1.start()
    if int(i) == 4:
        quit()
    elif int(i) in [1, 2, 3]:
        t2 = Thread(target=menu(), daemon=True)
        t2.start()
    else:
        print("ERROR enter a valid input")
        menu()

