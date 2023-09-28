import os

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "recette " + os.environ['plat']

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
