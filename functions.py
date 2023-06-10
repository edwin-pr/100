def main():
    name = input("what's your name ?")
    hello()
    print(name)


def hello(to="world"):
    print("hello,", to)

main()