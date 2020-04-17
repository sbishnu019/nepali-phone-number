import re
phone_number_regex = re.compile("^(984|985|986|974|975|980|981|982|961|988|972|963)\d{7}$")
ntc_phone_number_regex = re.compile("^(984|985|986|)\d{7}$")
ncell_phone_number_regex = re.compile("^(980|981|982)\d{7}$")
smart_cell_phone_number_regex = re.compile("^(961|988)\d{7}$")
utl_phone_number_regex = re.compile("^(972)\d{7}$")
sky_phone_number_regex = re.compile("^(974|975)\d{7}$")
hello_phone_number_regex = re.compile("^(963)\d{7}$")


land_line_number_regex = re.compile("^(097|095|081|053|084|083|029|056|096|089|093|010|026|041|068|049|094|"
                                    "064|079|027|046|087|091|076|061|036|025|066|077|099|044|057|023|021|069|"
                                    "055|037|075|024|067|051|086|082|071|033|031|092|047|038|063|035)(4|5|6)\d{5}$")
kathmandu_land_line_number_regex = re.compile("^(01)(4|5|6)\d{6}$")
