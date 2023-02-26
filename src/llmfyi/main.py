# This program defines a simple CLI app.
# It defines a single function "main"
# It imports sys
# It prints "hello world" plus the text from the first sys argument if it exists

import sys

def main():
    if len(sys.argv) > 1:
        print("Hello world " + sys.argv[1])
    else:
        print("Hello world")

if __name__ == "__main__":
    main()


