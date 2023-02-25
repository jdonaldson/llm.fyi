# This program defines a simple CLI app.
# It defines a single function "main"
# It prints "hello world" plus the text from the first argument.

def main(arg1):
    print("Hello world " + arg1)

if __name__ == "__main__":
    main("from the CLI")

