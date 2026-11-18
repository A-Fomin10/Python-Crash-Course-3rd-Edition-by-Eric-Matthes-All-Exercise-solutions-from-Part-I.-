buffet = ('strawberry cupcakes','pana-cota','chocolate muffins','pudding',
            'jelly',)

for desert in buffet:
    print(desert)

# buffet[0] = 'cookies'#for experiment I've used both '[]' and '()'. None worked
buffet = ('chocolate cookies','strawberry cream cookies', 'pana-cota', 'muffins',
            'pudding',)

print("\nNew desert menu:")#I assume this specific line was added to the book 
#to use "\n", since you can't use it with simple
#print in line 12. Atleast I'm not sure how(WIthout an F string)

for desert in buffet:
    print(desert.title())
#Note to self: limit comments to 72 characters on a line. Some prefer it 99.
