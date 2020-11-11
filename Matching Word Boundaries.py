#Matching Word Boundaries

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-z]*\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())