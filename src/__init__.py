import os
from textx import language, metamodel_from_file
from textx import generator as gen
from src.report_generator.generator import generate
from os.path import dirname

__version__ = "0.1.0.dev"


@language('scout', '*.sctv')
def scout_language():
    "scout language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'scout.tx'))

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm

@gen('scout', 'csv+pdf')
def scout_generate_files(metamodel, model, output_path, overwrite, debug): 
    "A generator function that produce csv and pdf report from model."
    input_file = model._tx_filename
    output_dir = output_path if output_path else dirname(input_file)
    print(output_dir, ' output dir')
    generate(model)