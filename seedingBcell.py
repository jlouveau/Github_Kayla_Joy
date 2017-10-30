# Seeding B cells dictionary

import csv
import numpy as np

#parameters
length            = 46
nb_seeding_cells  = 15
N                 = 5000
activation_energy = 10.8
delta_energy      = 0.50
lower_res         = -0.18
upper_res         = 0.90

#Bcells
seedingCells = []

n = 0
for i in range(N):   
    if n < nb_seeding_cells:
        cell = np.random.uniform(-0.18,0.9, length)
        if (sum(cell) > activation_energy - delta_energy) and (sum(cell) < activation_energy + delta_energy):
            n +=1
            seedingCells.append(cell)
    else:
        #print(n)
        #print(i)
        break
#print(len(seedingCells))
#print(seedingCells)

with open('seedingCells.csv', 'w') as output:
    w = csv.writer(output)
    w.writerow(['res0','res1','res2','res3','res4','res5','res6','res7','res8','res9','res10','res11','res12','res13','res14','res15','res16','res17','res18','res19','res20','res21','res22','res23','res24','res25','res26','res27','res28','res29','res30','res31','res32','res33','res34','res35','res36','res37','res38','res39','res40','res41','res42','res43','res44','res45'])
    w.writerows(seedingCells)

