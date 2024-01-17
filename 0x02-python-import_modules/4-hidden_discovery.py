#!/usr/bin/python3
import marshal
import types


def print_hidden_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    names.sort()
    for name in names:
        print(name)


def load_compiled_module(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        code = marshal.loads(file_content[16:])
        module = types.ModuleType(file_path)
        exec(code, module.__dict__)
        return module


if __name__ == "__main__":
    file_path = "hidden_4.pyc"
    compiled_module = load_compiled_module(file_path)
    print_hidden_names(compiled_module)
