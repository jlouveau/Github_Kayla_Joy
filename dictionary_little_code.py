#dictionary for Mixture project
import csv

####### parameters #######
time_Steps = [2, 61, 121, 181, 241]
singleAntigenTest = 1
cocktailFirst = 1
l = 12 #number of residues, 3 conserved, 9 variable

####### antigens creation ####### 
#initializer
Ag0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
 
# closely related antigens d = 1
Ag1 = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Ag2 = [1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1]
Ag3 = [1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1]

# distant antigens for sequential D = 3
Ag4 = [-1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Ag5 = [1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1]
Ag6 = [1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1]

if singleAntigenTest ==1:
    dicAgs = {c:Ag0 for c in list(range(time_Steps[0], time_Steps[3]))}
    with open('output_singleAntigenDict.csv', 'w') as output:
        w = csv.writer(output)
        w.writerows(dicAgs.items())
else:        
    if cocktailFirst==1: 
        dicCocktail = {c: [Ag0, Ag1, Ag2] for c in list(range(time_Steps[0],time_Steps[1]))}
        dicAgs = dicCocktail.copy()
        dicAgs.update({c:Ag4 for c in list(range(time_Steps[1],time_Steps[2]))})
        dicAgs.update({c:Ag5 for c in list(range(time_Steps[2],time_Steps[3]))})
        dicAgs.update({c:Ag6 for c in list(range(time_Steps[3],time_Steps[4]))})
        with open('output_cocktailDict.csv', 'w') as output:
            w = csv.writer(output)
            w.writerows(dicAgs.items())
    
    else:      
        dicAgs = {c:Ag0 for c in list(range(time_Steps[0],time_Steps[1]))}
        dicAgs.update({c:Ag4 for c in list(range(time_Steps[1],time_Steps[2]))})
        dicAgs.update({c:Ag5 for c in list(range(time_Steps[2],time_Steps[3]))})
        dicCocktail = {c: [Ag1, Ag2, Ag3] for c in list(range(time_Steps[3],time_Steps[4]))}
        dicAgs.update(dicCocktail)    
        with open('output_sequenceDict.csv', 'w') as output:
            w = csv.writer(output)
            w.writerows(dicAgs.items())
    
