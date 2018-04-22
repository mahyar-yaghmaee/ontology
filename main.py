
# -*- coding: utf-8 -*-
import sys
from file_parser import FilerParser
from object_parser import ObjectParser

input_file_name = 'PK_copy.owl'


def main(argv):
    file_parser = FilerParser(input_file_name)
    object_parser = ObjectParser(input_file_name)


    gg = object_parser.get_declaration_dictionary()
    print(gg)






if __name__ == "__main__":
    main(sys.argv[1:])