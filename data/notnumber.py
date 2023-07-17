#!/usr/bin/env python3
import re

#regex = r"^[A-Z]"
regex2 = r"[A-Za-z](?!@)[A-Za-z]"
#print(regex)
#test_str = "A1_2_3_GO!"
text = "www@google"
print(text)
matches = re.search(regex2, text)
print(matches)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
