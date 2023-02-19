
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in "}])":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position 
    return "Success"


def main():
    inputs = input("Type F or I: ")
    text = input()
    mismatch = find_mismatch(text)

    if "I" in inputs:
        if mismatch != "Success":
            print(mismatch)
        else:
            print("Success")

    elif "F" in inputs:
        file = input("File path: ")
        with open(file, "r") as file:
            text = file.read()
            if mismatch != "Success":
                print(mismatch)
            else:
                print("Success")
    else:
        print("I said F or I")

if __name__ == "__main__":
    main()
