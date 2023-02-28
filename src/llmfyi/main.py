# This program defines a simple CLI app.
# It imports sys, llmfyi.dotfile, and openai.
# It defines a single function "main".
# Inside the main function, it does the following:
# * It calls the dotfile.dotfile method, saving it to a variable named prompt.
# * It then adds a line of "====\n" to the prompt variable.
# * It then checks for and adds the first sys argument to the result, along with "\n".
# * It then call the openai.Completion.create function:
#       * It uses text-davinci-003 as the engine,
#       * The prompt variable as the prompt argument
#       * The max_tokens as 2048
# * It prints the text field from the first entry of the choices field returned as a result.
# It invokes the main function if its __name__ is "__main__".

import sys
import llmfyi.dotfile
import openai

def main():
    prompt = llmfyi.dotfile.dotfile()
    prompt += "====\n"
    if len(sys.argv) > 1:
        prompt += sys.argv[1] + "\n"
    choices = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)
    print(choices["choices"][0]["text"])

if __name__ == "__main__":
    main()

