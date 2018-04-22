# -*- coding: utf-8 -*-v

class FilerParser():
    DECLARATION_STRING = "Declaration("
    OBJECT_PROPERTIES_STRING = "#   Object Properties"
    DATA_PROPERTIES_STRING = "#   Data Properties"
    NAMED_INDIVIDUALS_STRING = "#   Named Individuals"
    CLASSES_STRING = "#   Classes"
    HASH_PATTERN = "############################"
    all_lines_list = []

    def __init__(self, input_file):
        self.all_lines_list = self.__get_list_of_lines_from_file(input_file)

    #    for hh in self.all_lines_list:

     #       print(hh.decode('string_escape'))

    def __get_list_of_lines_from_file(self, input_file):
            with open(input_file) as f:
                return f.readlines()

    def get_declaration_lines_list(self):
        declaration_lines = []
        for line in self.all_lines_list:
            if line.startswith(self.DECLARATION_STRING):
                declaration_lines.append(line.rstrip())
        return declaration_lines

    def _get_start_element_number_of_each_block(self):
        object_properties_block_start_element_number = 0
        data_properties_block_start_element_number = 0
        classes_block_start_element_number = 0
        named_individuals_block_start_element_number = 0
        object_properties_block_end_element_number = 0
        data_properties_block_end_element_number = 0
        classes_block_end_element_number = 0
        named_individuals_end_element_number = 0

        for line_number_element_in_list in range(0, len(self.all_lines_list)):
            if self.all_lines_list[line_number_element_in_list].startswith(self.OBJECT_PROPERTIES_STRING) and \
                    self.all_lines_list[line_number_element_in_list + 1].rstrip() == self.HASH_PATTERN:
                # element number is in the list = line number - 1 since element number starts from 0, but line number starts from 1
                object_properties_block_start_element_number = line_number_element_in_list + 2
                for element_number_in_block in range(object_properties_block_start_element_number, len(self.all_lines_list)):
                    if self.all_lines_list[element_number_in_block].rstrip() == self.HASH_PATTERN:
                        object_properties_block_end_element_number = element_number_in_block
                        break
                    else:
                        object_properties_block_end_element_number = len(self.all_lines_list)

            if self.all_lines_list[line_number_element_in_list].startswith(self.DATA_PROPERTIES_STRING) and self.all_lines_list[
                line_number_element_in_list + 1].rstrip() == self.HASH_PATTERN:
                data_properties_block_start_element_number = line_number_element_in_list + 2

                for element_number_in_block in range(data_properties_block_start_element_number, len(self.all_lines_list)):
                    if self.all_lines_list[element_number_in_block].rstrip() == self.HASH_PATTERN:
                        data_properties_block_end_element_number = element_number_in_block
                        break
                    else:
                        data_properties_block_end_element_number = len(self.all_lines_list)

            if self.all_lines_list[line_number_element_in_list].startswith(self.CLASSES_STRING) and \
                    self.all_lines_list[line_number_element_in_list + 1].rstrip() == self.HASH_PATTERN:
                classes_block_start_element_number = line_number_element_in_list + 2

                for element_number_in_block in range(classes_block_start_element_number, len(self.all_lines_list)):
                    if self.all_lines_list[element_number_in_block].rstrip() == self.HASH_PATTERN:
                        classes_block_end_element_number = element_number_in_block
                        break
                    else:
                        classes_block_end_element_number = len(self.all_lines_list)

            if self.all_lines_list[line_number_element_in_list].startswith(self.NAMED_INDIVIDUALS_STRING) and \
                    self.all_lines_list[line_number_element_in_list + 1].rstrip() == self.HASH_PATTERN:
                named_individuals_block_start_element_number = line_number_element_in_list + 2
                print 'HEREEEEE!!!: ' , named_individuals_block_start_element_number
                print 'list_of_all_lines:  ', self.all_lines_list[named_individuals_block_start_element_number]
                print 'len(list_of_all_lines): ', len(self.all_lines_list)

                # individualS block ends at eof
                named_individuals_end_element_number = len(self.all_lines_list)

        return (object_properties_block_start_element_number, object_properties_block_end_element_number,
                data_properties_block_start_element_number, data_properties_block_end_element_number,
                classes_block_start_element_number, classes_block_end_element_number,
                named_individuals_block_start_element_number, named_individuals_end_element_number)