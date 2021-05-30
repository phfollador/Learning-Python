#%%
import numpy as np
from numpy import polymul
# PRIMEIRA TABELA
x = np.array([0, 3, 4, 5, 9], dtype="double")  
y = np.array([22, 22, 42, 22, 22], dtype="double")  
#inicializando a tabela  
T = np.zeros((5,5));  
#primeira coluna  
T[:,0]=y;  
#segunda coluna  
T[1,1]=(T[1,0]-T[0,0])/(x[1]-x[0]);  
T[2,1]=(T[2,0]-T[1,0])/(x[2]-x[1]);  
T[3,1]=(T[3,0]-T[2,0])/(x[3]-x[2]);
T[4,1]=(T[4,0]-T[3,0])/(x[4]-x[3]); 
#terceira coluna  
T[2,2]=(T[2,1]-T[1,1])/(x[2]-x[0]);  
T[3,2]=(T[3,1]-T[2,1])/(x[3]-x[1]);  
T[4,2]=(T[4,1]-T[3,1])/(x[4]-x[2]);
#quarta coluna  
T[3,3]=(T[3,2]-T[2,2])/(x[3]-x[0]);
T[4,3]=(T[4,2]-T[3,2])/(x[4]-x[1]);  
#quinta coluna
T[4,4]=(T[4,3]-T[3,3])/(x[4]-x[0]);
print(T)  
#polinomio interpolador  
p = np.array([T[0,0]], dtype="double")  
paux = np.array([-x[0],1], dtype="double")  
p.resize(2)  
p += T[1,1]*paux  
paux = np.polymul(paux,[-x[1],1])  
p.resize(3)  
p += T[2,2]*paux  
paux = np.polymul(paux,[-x[2],1])  
p.resize(4)  
p += T[3,3]*paux
paux = poly.polymul(paux,[-x[3],1])  
p.resize(5)  
p += T[4,4]*paux

#%%
import numpy as np
from numpy import poly
# SEGUNDA TABELA
x = np.array([1, 2, 6, 7, 8], dtype="double")  
y = np.array([-42, -20, -32, -90, -98], dtype="double")  
#inicializando a tabela  
T = np.zeros((5,5));  
#primeira coluna  
T[:,0]=y;  
#segunda coluna  
T[1,1]=(T[1,0]-T[0,0])/(x[1]-x[0]);  
T[2,1]=(T[2,0]-T[1,0])/(x[2]-x[1]);  
T[3,1]=(T[3,0]-T[2,0])/(x[3]-x[2]);
T[4,1]=(T[4,0]-T[3,0])/(x[4]-x[3]); 
#terceira coluna  
T[2,2]=(T[2,1]-T[1,1])/(x[2]-x[0]);  
T[3,2]=(T[3,1]-T[2,1])/(x[3]-x[1]);  
T[4,2]=(T[4,1]-T[3,1])/(x[4]-x[2]);
#quarta coluna  
T[3,3]=(T[3,2]-T[2,2])/(x[3]-x[0]);
T[4,3]=(T[4,2]-T[3,2])/(x[4]-x[1]);  
#quinta coluna
T[4,4]=(T[4,3]-T[3,3])/(x[4]-x[0]);
print(T)
#polinomio interpolador  
p = np.array([T[0,0]], dtype="double")  
paux = np.array([-x[0],1], dtype="double")  
p.resize(2)  
p += T[1,1]*paux  
paux = np.polymul(paux,[-x[1],1])  
p.resize(3)  
p += T[2,2]*paux  
paux = np.polymul(paux,[-x[2],1])  
p.resize(4)  
p += T[3,3]*paux
paux = np.polymul(paux,[-x[3],1])  
p.resize(5)  
p += T[4,4]*paux
#%%
import numpy as np
from numpy import poly
# TERCEIRA TABELA
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype="double")  
y = np.array([22, -42, -20, 22, 42, 22, -32, -90, -98, 22], dtype="double")  
#inicializando a tabela  
T = np.zeros((10,10));  
#primeira coluna  
T[:,0]=y;  
#segunda coluna  
T[1,1]=(T[1,0]-T[0,0])/(x[1]-x[0]);  
T[2,1]=(T[2,0]-T[1,0])/(x[2]-x[1]);  
T[3,1]=(T[3,0]-T[2,0])/(x[3]-x[2]);
T[4,1]=(T[4,0]-T[3,0])/(x[4]-x[3]);  
T[5,1]=(T[5,0]-T[4,0])/(x[5]-x[4]);  
T[6,1]=(T[6,0]-T[5,0])/(x[6]-x[5]); 
T[7,1]=(T[7,0]-T[6,0])/(x[7]-x[6]);  
T[8,1]=(T[8,0]-T[7,0])/(x[8]-x[7]);  
T[9,1]=(T[9,0]-T[8,0])/(x[9]-x[8]); 
#terceira coluna  
T[2,2]=(T[2,1]-T[1,1])/(x[2]-x[0]);  
T[3,2]=(T[3,1]-T[2,1])/(x[3]-x[1]);
T[4,2]=(T[4,1]-T[3,1])/(x[4]-x[2]);  
T[5,2]=(T[5,1]-T[4,1])/(x[5]-x[3]);
T[6,2]=(T[6,1]-T[5,1])/(x[6]-x[4]);  
T[7,2]=(T[7,1]-T[6,1])/(x[7]-x[5]);
T[8,2]=(T[8,1]-T[7,1])/(x[8]-x[6]);  
T[9,2]=(T[9,1]-T[8,1])/(x[9]-x[7]);  
#quarta coluna  
T[3,3]=(T[3,2]-T[2,2])/(x[3]-x[0]);
T[4,3]=(T[4,2]-T[3,2])/(x[4]-x[1]);  
T[5,3]=(T[5,2]-T[4,2])/(x[5]-x[2]);
T[6,3]=(T[6,2]-T[5,2])/(x[6]-x[3]);  
T[7,3]=(T[7,2]-T[6,2])/(x[7]-x[4]);
T[8,3]=(T[8,2]-T[7,2])/(x[8]-x[5]);  
T[9,3]=(T[9,2]-T[8,2])/(x[9]-x[6]);
#quinta coluna
T[4,4]=(T[4,3]-T[3,3])/(x[4]-x[0]);  
T[5,4]=(T[5,3]-T[4,3])/(x[5]-x[1]);
T[6,4]=(T[6,3]-T[5,3])/(x[6]-x[2]);  
T[7,4]=(T[7,3]-T[6,3])/(x[7]-x[3]);
T[8,4]=(T[8,3]-T[7,3])/(x[8]-x[4]);  
T[9,4]=(T[9,3]-T[8,3])/(x[9]-x[5]); 
#sexta coluna
T[5,5]=(T[5,4]-T[4,4])/(x[5]-x[0]);
T[6,5]=(T[6,4]-T[5,4])/(x[6]-x[1]);  
T[7,5]=(T[7,4]-T[6,4])/(x[7]-x[2]);
T[8,5]=(T[8,4]-T[7,4])/(x[8]-x[3]);  
T[9,5]=(T[9,4]-T[8,4])/(x[9]-x[4]); 
#setima coluna
T[6,6]=(T[6,5]-T[5,5])/(x[6]-x[0]);  
T[7,6]=(T[7,5]-T[6,5])/(x[7]-x[1]);
T[8,6]=(T[8,5]-T[7,5])/(x[8]-x[2]);  
T[9,6]=(T[9,5]-T[8,5])/(x[9]-x[3]); 
#oitava coluna
T[7,7]=(T[7,6]-T[6,6])/(x[7]-x[0]);
T[8,7]=(T[8,6]-T[7,6])/(x[8]-x[1]);  
T[9,7]=(T[9,6]-T[8,6])/(x[9]-x[2]); 
#nona coluna
T[8,8]=(T[8,7]-T[7,7])/(x[8]-x[0]);  
T[9,8]=(T[9,7]-T[8,7])/(x[9]-x[1]); 
#décima coluna 
T[9,9]=(T[9,8]-T[8,8])/(x[9]-x[0]); 
print(T)  
#polinomio interpolador  
p = np.array([T[0,0]], dtype="double")  
paux = np.array([-x[0],1], dtype="double")  
p.resize(2)  
p += T[1,1]*paux  
paux = np.polymul(paux,[-x[1],1])  
p.resize(3)  
p += T[2,2]*paux  
paux = np.polymul(paux,[-x[2],1])  
p.resize(4)  
p += T[3,3]*paux
paux = np.polymul(paux,[-x[3],1])  
p.resize(5)  
p += T[4,4]*paux
paux = np.polymul(paux,[-x[4],1])  
p.resize(6)  
p += T[5,5]*paux
paux = np.polymul(paux,[-x[5],1])  
p.resize(7)  
p += T[6,6]*paux
paux = np.polymul(paux,[-x[6],1])  
p.resize(8)  
p += T[7,7]*paux
paux = np.polymul(paux,[-x[7],1])  
p.resize(9)  
p += T[8,8]*paux
# %%