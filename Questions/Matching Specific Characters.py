#Matching Specific Characters

Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
or
Regex_Pattern =# r'[\d{2}\S{2}\W{2}]'	

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())