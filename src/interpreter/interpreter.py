import sys
from textx import metamodel_from_file
from os.path import join, dirname, exists

def interpreter(file_name):
    meta_model = metamodel_from_file('..\\grammar\\grammar.tx')
    model = meta_model.model_from_file(file_name)
    return model

def create_model():
    pass

if __name__ == '__main__':
    file_name = join('..', sys.argv[1])
    model = interpreter(file_name)
    print(model.team_a)