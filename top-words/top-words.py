#!/mnt/c/Users/wulfa/AppData/Local/Programs/Python/Python36-32/python.exe
import re
import sys
from collections import Counter
num_words = int(sys.argv[1])
text = sys.stdin.read().lower()
words = re.split('\W+', text)
cnt = Counter(words)
for word, count in cnt.most_common(num_words):
    print (word + " " + str(count))