import re

post = "Loving the #Python and #Regex learning journey! #coding"
hashtags = re.findall(r"#\w+", post)
print(hashtags)