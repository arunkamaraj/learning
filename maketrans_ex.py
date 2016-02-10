
#replacing the vowels

import string


str = "this is vowel replacing example"

actual = "aeiou"
replace = "12345"
metadata = string.maketrans(actual,replace)

final_str = str.translate(metadata)

print final_str




