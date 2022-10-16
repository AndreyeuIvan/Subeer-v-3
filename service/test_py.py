import re
import json

with open('test.srt') as f:
    text = f.read()

re_time_sub = r"(?P<time>[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}\W+[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3})\n(?P<text>^\D*)"
matches = re.finditer(re_time_sub, text, re.MULTILINE)
data = [{i.groups()[0]:i.groups()[1]} for i in matches]

json_data = json.dumps(data)
