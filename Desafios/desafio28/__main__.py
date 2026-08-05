

from classes import *
from rich import inspect

def main():
    t1 = Temperatura()
    try:
        t1.temperatura = 28
        print(t1.ftemp)
        #inspect(t1,private=True)

    except Exception as e:
        print(f"erro:{e}")
if __name__ == "__main__":
    main()