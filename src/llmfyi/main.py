# This program defines a simple CLI app.
# It imports sys, llmfyi.dotfile, and openai.
# It defines a single function "main".
# Inside the main function, it does the following:
# * It calls the dotfile.dotfile method, saving it to a variable named prompt.
# * It then adds a line of "====\n" to the prompt variable.
# * It then adds the first sys argument to the result, along with "\n".
# * It then call the openai.Completion.create function, using text-davinci-003 as the engine, and the prompt variable as the prompt argument.
# * It prints the text field from the first entry of the choices field returned as a result.
# It invokes the main function if its __name__ is "__main__".

import sys
import llmfyi.dotfile
import openai

def main():
    prompt = llmfyi.dotfile.dotfile()
    prompt += "====\n"
    prompt += sys.argv[1] + "\n"
    choices = openai.Completion.create(engine="text-davinci-003", prompt=prompt)
    print(choices["choices"][0]["text"])

if __name__ == "__main__":
    main()

