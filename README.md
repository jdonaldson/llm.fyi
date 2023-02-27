<!--
llm.fyi is a simple framework for managing large language model related tasks on filesystems.
The framework installs a simple "llm" command that is usable from the command line.
The .llm.fyi files should contain prompts that are relevant for the files at that directory level.
To use llm.fyi, call the llm command on a current working directory.  If there are any .llm.fyi files there, it will use them.
Otherwise, it will check the parent directories for .llm.fyi files and use those.
You can install llm.fyi by using pip install llmfyi

This is a README documenting describing how to use it.
-->

# llm.fyi

llm.fyi is a simple framework for managing large language model related tasks on filesystems.

## Installation

To install llm.fyi, use `pip install llmfyi`.

## Usage

To use llm.fyi, call the `llm` command on a current working directory.  If there are any `.llm.fyi` files there, it will use them. Otherwise, it will check the parent directories for `.llm.fyi` files and use those.

The `.llm.fyi` files should contain prompts that are relevant for the files at that directory level.

