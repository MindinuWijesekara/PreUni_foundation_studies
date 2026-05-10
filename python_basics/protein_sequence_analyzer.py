prtn = input('Please enter your protein sequence.',).upper()
amino = input('What amino acid are you looking for ?',).upper()
if amino in prtn:
  counter = prtn.count(amino)
  finder = prtn.find(amino)
  print('You have',counter,'of',amino,'amino acid(s) in you protein sequence.')
  print(finder,'is the first index number for',amino,'amino acid.')
  print('Here are the last 5 letters of you protein sequence :-',prtn[-5:])
else:
 print("Protein sequence doesn't include exact amino acid you're looking for.!")
