#IMPORTANT

letter = '''Dear <|Name|>, 
You are selected!
<|Date|>'''

# use of ''' is to successfully code in multiple lines without error.

print(letter.replace("<|Name|>", "Harry"). replace("<|Date|>", "27 sept 2045"))

# this multiple replace is called chaining, we can use multiple replace to edit many slots.
