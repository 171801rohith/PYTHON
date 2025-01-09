# Regular Expressions
import re

para = """Michael William Balfe (1808-1870) was an Irish composer, best remembered for his operas. 
Balfe was born in Dublin and grew up on Pitt Street, which was renamed Balfe Street in 1917 in his honour. 
After moving to Wexford with his family as a child, he began a career as a violinist, moving to London in 1823 Dichael
after his father's death, later relocating again to Italy and Switzerland, where he married the Hungarian-born singer Lina Roser.
Balfe began pursuing an operatic singing career as well as composition, and moved back to London with his family in 1835. 
In a career spanning more than 40 years, he composed at least 29 operas, almost 250 songs, several cantatas, and other works. 
He was also a noted conductor, directing Italian opera at Her Majesty's Italian Opera House for seven years, among other conducting posts. 
His most notable opera is The Bohemian Girl, which continues to be performed. Jichael and Michael , michael
This photograph of Balfe was taken by the studio of the French photographer Nadar; this albumen print was made in 1900.
"""

# Simple
pattern = "was"
match = re.search(pattern,para) #only first occurrence
print(match)
print(match.span())
print(type(match.span()))
matches = re.finditer(pattern,para) #all occurrence
for match in matches:
    print(match)

# Complex
pattern = r"[A-Z]ichael"
match = re.search(pattern,para) #only first occurrence 
print(match)
matches = re.finditer(pattern,para) #all occurrence
for match in matches:
    print(match)
    print(para[match.span()[0] : match.span()[1]])

# https://regexr.com/ for more