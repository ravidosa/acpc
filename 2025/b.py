import re

inp = input()

print(re.sub(r"\*\*([^\*]*)\*\*", r"\\bf{\1}", inp))