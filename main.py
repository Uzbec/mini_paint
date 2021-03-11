from sys import argv
import os
import ft_len
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if len(argv) == 2:
    a = argv[1]
elif len(argv) > 2:
    print("Error: a lot of arguments")
    a = None
    print()
else:
    a = input()
    if " " in a:
        print("Error: a lot of arguments")
        a = None
        print()


if a:
    #if str(BASE_DIR) not in a:
        #a = f"{BASE_DIR}/{a}"
    print(a)
    if "operation" in a and "operation.it" not in a:
        a = None
        print("Error:Operation file has not correct extension")
        print()
    if a:
        try:
            file = open(a)
        except FileNotFoundError as e:
            a = None
            print("Error:name file\n")
        except IOError as e:
            a = None
            print("Error:Operation file corrupted")

