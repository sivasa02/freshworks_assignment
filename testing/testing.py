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
                else:
                    print("ERROR:MEMORY Exceeded!!!")
            else:
                print("ERROR:INVALID INPUT (NUMERIC ONLY)")
        else:
            print("ERROR:INVALID KEY INPUT (ALPHABETS ONLY)")


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