import re
phone_number_regex = re.compile("^(984|985|986|974|975|980|981|982|961|988|972|963)\d{7}$")
ntc_phone_number_regex = re.compile("^(984|985|986|)\d{7}$")
ncell_phone_number_regex = re.compile("^(980|981|982)\d{7}$")
smart_cell_phone_number_regex = re.compile("^(961|988)\d{7}$")
utl_phone_number_regex = re.compile("^(972)\d{7}$")
sky_phone_number_regex = re.compile("^(974|975)\d{7}$")
hello_phone_number_regex = re.compile("^(963)\d{7}$")

