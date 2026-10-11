import re
text = 'sldjkh #jfghfskh #daskfj'
result = re.findall(r"#" \
"w+", text)
print(result)


import datetime

today = 5-11-2026
date2ago = today - 2
date2after = today + 2
print(date2ago, today, date2after)