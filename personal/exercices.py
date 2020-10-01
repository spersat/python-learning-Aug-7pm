import math
#### application directe####
# exercice 1
'''
texte = 'texte'
entier = 1
décimal = 1.2

print (type(texte))
print (type(entier))
print (type(décimal))
'''
#exerice 2
'''
texte, entier, décimal = 'ceci', 12, 3.5

print (texte)
print (entier)
print (décimal)
'''

#exercice 3
'''
rayon = int(input("entrer le rayon: "))
hauteur = int(input("entrer la hauteur: "))

volume= 1/3 * math.pi * rayon**2 * hauteur

print ('le volume est: ',volume)
'''

#exercice 4
'''
rext = int(input("rayon du disque exterieur: "))
rint = int(input("rayon du disque interieur: "))
if rint>rext:
    print("le rayon du disque intérieur ne peut pas être supérieur à celui du disque extérieur")
else:
    sext = math.pi * rext**2
    sint = math.pi * rint**2
    sdécoupé = sext - sint
    print("la surface du disque découpé est: ", sdécoupé)
'''


###application réfléchie####
#exercice 1
'''
aff1 = a = 3
aff2 = a == 3
print(aff1)
print(type(aff1))
print(aff2)
print(type(aff2))
'''

#exercice 2
'''
chaine = input("ecrire une chaine de caracteres: ")
numéro = int(input("ecrire un numéro: "))
print(chaine + str(numéro))
'''

#exercice 2 avancé
'''
try :
    print(int(input("entrer un nombre: ")))
except Exception as a:
    print("ceci n'est pas un nombre")
print("thank you for your choice")
'''
