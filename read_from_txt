name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#above gets input

#create dictionarybelow to add split and stripped words to 
d = dict()
count = 0
#iterate through the text file and create dictionary to produce histogram

for line in handle:
    
    line = line.rstrip()
    words= line.split()
    
    if len(words) < 1 or words[0] != 'From':
        continue
        
        
# populate dictionary with key value pairs        
    email = words[1]
    d[email] = d.get(email,0) + 1

#iterate through key:value pairs and create running total for output
    
bigName = None
bigCount = None

for email, count in d.items():
    if bigCount is None or count > bigCount:
        bigName = email
        bigCount = count
        
        
print(bigName, bigCount)    
