import sys
import requests

if len(sys.argv) != 3 :
    print("Usage: python count_word [URL] [WORD_TO_BE_COUNTED]")
    sys.exit()

url = sys.argv[1]
word = sys.argv[2]

r = requests.get(url)
if r.status_code == 200:
    print(len(word))
else:
    print("ERROR:",r.status_code)