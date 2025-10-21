import re
m = re.search('(?<=abc)def', 'abcdef',)
m.group(0)
print(m.group(0))

#See the use of (? followed by = sign. It is the letter after ? that defines operations
print("This one follows an hyphen")
m = re.search(r'(?<=-)\w+', 'spam-egg-ok')
print(m.group(0))
#print(m.group(1))


#the split algorithm in re
print(re.split(r'\W+', 'Words, words, words.'))

print(" ")

#showcasing the escape method for escaping metadata in strings
print(re.escape('https://www.usiu.ac.ke'))

operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))