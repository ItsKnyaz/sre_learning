def calculate(x, y):
    return x + y + 10  # Из feature

def multiply(x, y):
    return x * y + 100  # Из main

def main():
    print(calculate(2, 3))
    print(multiply(4, 5))
    print("Main update")  # Из main
    print("Feature update")  # Из feature

if __name__ == "__main__":
    main()
