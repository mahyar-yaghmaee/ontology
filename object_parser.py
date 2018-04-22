# -*- coding: utf-8 -*-v
from file_parser import FilerParser


class ObjectParser():
    KEY_DECLARATION_OBJECTS = ['Class:', 'ObjectProperty:', 'DataProperty:', 'NamedIndividual:']

    def __init__(self, input_file):
        self.file_parser = FilerParser(input_file)

    def get_declaration_dictionary(self):
        declaration_dictionary = {'Class': [],
                                  'ObjectProperty': [],
                                  'DataProperty': [],
                                  'NamedIndividual': []}
        dec_list = self.file_parser.get_declaration_lines_list()

        # check for only valid key_declaration_objects
        for element in dec_list:
            # get pattern AA:BB
            key_value = element.replace('Declaration', '').replace('(', '').replace(')', '')

            # get valid key_values
            for key_dec_object in self.KEY_DECLARATION_OBJECTS:
                if key_dec_object in key_value:
                    key_value_pair = key_value.split(':')
                    declaration_dictionary[key_value_pair[0]].append(key_value_pair[1])

        return declaration_dictionary
