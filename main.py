import sys
from file_parser import FilerParser

input_file_name = 'PK_copy.owl'

DECLARATION_STRING = "Declaration("
OBJECT_PROPERTIES_STRING = "#   Object Properties"
DATA_PROPERTIES_STRING = "#   Data Properties"
CLASSES_STRING = "#   Classes"
NAMED_INDIVIDUALS_STRING = "#   Named Individuals"
HASH_PATTERN = "############################"

declaration_lines = []


def main(argv):
    file_parser = FilerParser()
    all_lines_list = file_parser.get_list_of_lines_from_file(input_file_name)

    a = file_parser._get_start_element_number_of_each_block(all_lines_list)
    print a

   # print(all_lines_list[a[0]])





if __name__ == "__main__":
    main(sys.argv[1:])