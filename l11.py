s = 'ab\ncd\nef'
print(s.replace('\n', ''))
print(s.translate({ord('\n'): None}))
