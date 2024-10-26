import re 

sentence = "Write a program to build a bridge but beware of the beehive."
words = re.findall(r"\bb\w*e\b", sentence)
print(words)