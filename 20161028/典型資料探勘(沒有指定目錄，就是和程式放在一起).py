from collections import Counter
import re

words=re.findall(r'\w+',open('English.txt').read().lower())

wordcount=Counter(words)
for item in sorted(wordcount.items()):
    print('{}: {}'.format(*item))
#=================================================================
#w+-->w代表word
#沒有指定目錄，該資料就是和程式放在一起
#lower代表全部顯示小寫
#we can input wordcount and word to know how many kinds of the words and a kind of a word has how many
