input_file_name = 'PK_copy.owl'

with open(input_file_name) as f:
    all_lines_list = f.readlines()

DECLARATION_STRING = "Declaration("
OBJECT_PROPERTIES_STRING = "#   Object Properties"
DATA_PROPERTIES_STRING = "#   Data Properties"
CLASSES_STRING = "#   Classes"
NAMED_INDIVIDUALS_STRING = "#   Named Individuals"
HASH_PATTERN = "############################"

declaration_lines = []

for line in all_lines_list:
    if line.startswith(DECLARATION_STRING):
        declaration_lines.append(line.rstrip())

# lines start from 1
for line_number in range(0, len(all_lines_list)):
    if all_lines_list[line_number].startswith(OBJECT_PROPERTIES_STRING) and all_lines_list[line_number+1].rstrip() == HASH_PATTERN:
        print "line_number: " , line_number
        # element number is in the list = line number - 1 since element number starts from 0, but line number starts from 1
        object_properties_block_start_element_number = line_number+2

    if all_lines_list[line_number].startswith(DATA_PROPERTIES_STRING) and all_lines_list[line_number+1].rstrip() == HASH_PATTERN:
        data_properties_block_start_element_number = line_number + 2

    if all_lines_list[line_number].startswith(CLASSES_STRING) and all_lines_list[line_number+1].rstrip() == HASH_PATTERN:
        classes_block_start_element_number = line_number + 2

    if all_lines_list[line_number].startswith(NAMED_INDIVIDUALS_STRING) and all_lines_list[line_number+1].rstrip() == HASH_PATTERN:
        named_individuals_block_start_element_number = line_number + 2

print "all_lines_list[line_number]: " , all_lines_list[0]

print len(all_lines_list)

