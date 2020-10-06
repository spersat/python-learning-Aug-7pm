#exercice
'''
nombre1 = int(input("entrer le nombre 1: "))
nombre2 = int(input("entrer le nombre 2: "))

if nombre1 > nombre2:
    print("le plus grand nombre est: ", nombre1)
else :
    print("le plus grand nombre est: ", nombre2)
'''
#exercice
'''
chaine1 = input("entrer la première chaine: ")
chaine2 = input("entrer la deuxieme chaine: ")
if len(chaine1) == len(chaine2) :
    print("les deux chaines ont la meme longueur")
elif len(chaine1) > len(chaine2):
    print("la chaine 1 est la plus longue")
else :
    print("la chaine 2 est la plus longue")
'''

#exercice
'''
print("taux de conversion: 1 euro = 1,27 dollar")
facteur_euro_dollar = 1.27
value = int(input("entrer la valeur à convertir: "))
devise = input("entrer la devise (E pour euro, D pour dollar): ")

if devise == 'E':
    #print ("le montant correspondant en dollar est: ", value/2)
    print("le montant est: ","%f dollars" %(value*facteur_euro_dollar))
elif devise == 'D':
    print("le montant est: ","%f euros" %(value/facteur_euro_dollar))
else:
    print("la devise sélectionnée n'est pas connue")
'''

#exercice
'''
for i in range(10):
    print("%i je dois ranger mon bureau" %i)
'''

#exercice
'''
n=10
while (n > 0):
    print("c'est dans %i ans" %n)
    n=n-1
print("c'est maintenant")
'''

# exercice
'''
a= int(input("entrer un nombre: "))
if a%2 ==0:
    print("ce nombre est pair")
elif a%3 != 0 :
    print("ce nombre n'est ni pair ni multiple de 3")
else:
    print("ce nombre est impair et multiple de 3")
'''

#Exerice
'''
for i in range (0, 100, 2):
    print(i)

i = 0
while i<101 :
    print(i)
    i = i + 2
'''

#exercice
'''
print("les tables de multiplication")
for x in range (11):
    print("table des %i" %x)
    for y in range (11):
        print("%i * %i = %i" % (x,y,x*y))
'''

#Exercice

'''
1 ligne --> 1                           vvavv
2 lignes --> 3 nbligne*2 - 1            vaaav
3 lignes --> 5                          aaaaa    
4 lignes --> 7
5 lignes --> 9
'''
nblignes = int(input("Entrer le nb de lignes: "))
for i in range (1, nblignes):
    nbspace = nblignes - i
    nbarbre = i * 2 - 1
    print(' '*nbspace, '^'*nbarbre, ' '*nbspace)


