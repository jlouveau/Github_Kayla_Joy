#dictionary for Mixture project

 ####### parameters #######
time_Steps = [2, 61, 121, 181, 241]
cocktailFirst = 1
l = 12 #number of residues, 3 conserved, 9 variable

 ####### antigens creation ####### 
# cocktail closely related antigens d = 1
Coc_Ag0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Coc_Ag1 = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Coc_Ag2 = [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Cocktail = [Coc_Ag0, Coc_Ag1, Coc_Ag2] 

# distant antigens for sequential D = 4
Seq_Ag0 = [1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
Seq_Ag1 = [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1]
Seq_Ag2 = [1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1]


if cocktailFirst==1: 
	Coc_cycles = list(range(time_Steps[0],time_Steps[1]))
	dicCocktail = {c: Cocktail for c in Coc_cycles}
	dicAgs = dicCocktail.copy()
	dicAgs.update({c:Seq_Ag0 for c in list(range(time_Steps[1]+1,time_Steps[2]))})
	dicAgs.update({c:Seq_Ag1 for c in list(range(time_Steps[2]+1,time_Steps[3]))})
	dicAgs.update({c:Seq_Ag2 for c in list(range(time_Steps[3]+1,time_Steps[4]))})


"""Seq_cycles = list(range(time_Steps[2]+1,time_Steps[4])) 
Sequence = [Seq_Ag0, Seq_Ag1, Seq_Ag2] 

dicCocktail = {c: Cocktail for c in Coc_cycles}
dicSequence = {c: Sequence for c in Seq_cycles}
dicAntigens = dicCocktail.copy()
dicAntigens.update(dicSequence)"""
