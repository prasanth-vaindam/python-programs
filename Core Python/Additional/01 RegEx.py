# Remove Sub String by using Python

string = 'i think mabe 124 + <font color="black"><font face="Times New Roman">but I don\'t have a big experience it just how I see it in my eyes <font color="green"><font face="Arial">fun stuff'

print(string)

import re
string = re.sub('<.*?>', '', string)

print(string)