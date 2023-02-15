# This contains a program for python 3.
# The dotfile function checks for a prompt argument and sets it to an empty string if it's missing.
# The dotfile function calls the check_parent function.
# The check_parent function recursively checks directories and parent directories.
# If the check_parent function finds a file named ".llm.fyi", it does the following:
#   1. reads the file into a content variable after stripping extra whitespace.
#   2. prepends it to the prompt with a separator line that includes the directory name surrounded by "===".
# If the check_parent function finds a directory named ".git" in the current directory it will stop searching parent directories.
# The check_parent function returns the "prompt" variable.
# The dotfile function returns the prompt.
# Remember to include the os module if it is used.

import os

def dotfile(prompt=''):
    prompt = check_parent(prompt)
    return prompt

def check_parent(prompt):
    cur_dir = os.getcwd()
    parent_dir = os.path.dirname(cur_dir)
    if os.path.exists(os.path.join(cur_dir, '.llm.fyi')):
        with open(os.path.join(cur_dir, '.llm.fyi'), 'r') as f:
            content = f.read().strip()
            prompt = '==={}===\n{}\n{}'.format(cur_dir, content, prompt)
    if os.path.exists(os.path.join(cur_dir, '.git')) or cur_dir == parent_dir:
        return prompt
    else:
        os.chdir(parent_dir)
        return check_parent(prompt)

