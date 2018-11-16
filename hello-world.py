

import os

event = {
  "key3": "value3",
  "key2": "value2",
  "key1": "value1"
}

print("Hell World")
print("From Python")


def functionExecution(levent):
    print( os.environ['USER'])
    print("Tony MCClay")
    print(event["key1"])
    print(event["key2"])
    print(event["key3"])



