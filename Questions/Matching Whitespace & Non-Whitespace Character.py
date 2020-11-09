#Matching Whitespace & Non-Whitespace Character
Regex_Pattern = r"\s"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())