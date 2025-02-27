L = ["a","b","c","d","e","f","g","h"]
dico = {}

for elm in L:
    for i in range(1,9):
        dico[f'{elm}{i}'] = "_"

print(dico)