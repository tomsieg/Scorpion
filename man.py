#importation des modules
from math import *
import random 
import matplotlib.pyplot as plt
import numpy as np

#variables
#v = 0.24; #coefficient de poisson de matériel
#Lb = 50; #longueur du bras
#Lc = 51; #longueur de corde
#Lf = 20; #longueur de flèche
#Df = 2; #diamètre de flèche
#p = 10;  #masse de la flèche
#a = radians(45); #angle
#b = 5; #base de la section du bras
#h = 5; #hauteur de la section du bras
#E= 210; #module de young

#les tableaux
population = []
yMax = []
yMoy = []
yMin = []
xgeneration = []


#constance
g = 9.81; #accélaration de la pesanteur terrestre
taille_population = 10000
generation = 100
p  = 7850
E  = 210

#calcules
def ressort( E, v ):
    K = (1/3) * (E/(1-2*v));
    print ("ressort:", K, "N/m")
    return K

def longueurvide( Lb, Lc ):
    Lv = sqrt(pow(Lb, 2)-(1/4)*pow(Lc, 2))
    print ("Longueur vide:", Lv, "m")
    return Lv

def longueurdeplacement( Lf, Lv ):
    Ld = Lf-Lv
    print ("Longueur de déplacement:", Ld, "m")
    return Ld

def masseprojectile( p, Df, Lf ):
    mp = p*pi*pow((Df/2), 2)*Lf
    print ("Masse du projectile:", mp, "kg")
    return mp

def velocite( K, Ld, mp ):
    V = sqrt(K*pow(Ld, 2)/mp)
    print ("Vélocité:", V, "m/s")
    return V

def portee( V, g, a):
    d = pow(V, 2)/g*sin(2*a)
    print ("Portée:", d, "m")
    return d

def energiecinetique( mp, V):
    Ec = 1/2*mp*pow(V, 2)
    print ("Energie d'impact(cinétique):", Ec, "joules")
    return Ec

def energietnt( Ec):
    tnt = Ec/4184
    print ("Energie TNT:", tnt, "Grammes")
    return Ec

def momentquadra( b, h):
    I = b*pow(h, 2)/12
    print ("Moment quadratique du bras:", I, "m^4")
    return I

def traction( K, Ld):
    F = K*Ld
    print ("Force de traction:", F, "N")
    return F	

def fleche( F, Lb, E, I):
    f = (F*pow(Lb, 2))/(48*E*I)
    print ("Flèche du bras:", f, "max")
    return f

#génération
def GenScorpions(Tpop,p,E):
	pop = []
	for n in range(0, Tpop):
		#géneration aléatoire
		a  = radians(random.randrange(0,90))
		Lb = random.randrange(1,15)
		Lf = random.uniform(1,2)
		v  = random.uniform(0.24,0.30)
		Df = random.uniform(0.01,0.05)
		b  = random.randrange(1,15)
		h  = random.randrange(1,15)
		Lc = random.randrange(1,15)
		
		#calcules
		K = ressort( E, v);
		Lv = longueurvide( Lb, Lc);
		Ld = longueurdeplacement( Lf, Lv);
		mp = masseprojectile( p, Df, Lf );
		V = velocite( K, Ld, mp );
		d = portee( V, g, a);
		Ec = energiecinetique( mp, V);
		tnt = energietnt( Ec);
		I = momentquadra( b, h);
		F =traction( K, Ld);
		f = fleche( F, Lb, E, I)
		
		#creation du scorpion
		scorpion.ajout({"a":a,"Lb":Lb,"b":b,"h":h,"Lc":Lc,"Lf":Lf,"v":v,"K":K,"Lv":Lv,"Ld":Ld,"Df":Df,"mp":mp,"V":V,"d":d,"Ec":Ec,"Et":Et,"I":I,"F":F,"f":f})
		
		#ajout
		pop.append(scorpion)
	return pop

#test de la population
def test(pop):
	for scorpion in pop:
		scorpion["score"] = 10
		if scorpion["Ld"] <= scorpion["f"]:
			scorpion["score"] -= 3
		if scorpion["Lv"] <= scorpion["Lf"]:
			scorpion["score"] -= 3
		if scorpion["Lc"] <= scorpion["Lb"]:
			scorpion["score"] -= 3
		if scorpion["d"] >= 200 and scorpion["d"] < 270 :
			scorpion["score"] -= 1
		elif scorpion["d"] > 330 and scorpion["d"] <= 400:
			scorpion["score"] -= 1
		elif scorpion["d"] < 200 or scorpion["d"] > 400:
			scorpion["score"] -= 2
		if scorpion["Et"] >= 0.1 and scorpion["Et"] < 0.3:
			scorpion["score"] -= 1
		elif scorpion["Et"] <= 0.1:
			scorpion["score"] -= 2
		if scorpion["score"] <= 0:
			scorpion["score"] = 1
	return pop
	
#Selection naturel
def selection(population,taille_population,g,p,E):
	enfant_pop = []
	taille_selec = taille_population/2

	for i in range(0,int(taille_selec)):
		meilleur = random.sample(population,16)
		if meilleur[0]["score"] > meilleur[1]["score"]:
			qmeilleur1 = meilleur[0]
		else:
			qmeilleur1 = meilleur[1]
		if meilleur[2]["score"] > meilleur[3]["score"]:
			qmeilleur2 = meilleur[2]
		else:
			qmeilleur2 = meilleur[3]
		if meilleur[4]["score"] > meilleur[5]["score"]:
			qmeilleur3 = meilleur[4]
		else:
			qmeilleur3 = meilleur[5]
		if meilleur[6]["score"] > meilleur[7]["score"]:
			qmeilleur4 = meilleur[6]
		else:
			qmeilleur4 = meilleur[7]
		if meilleur[8]["score"] > meilleur[9]["score"]:
			qmeilleur5 = meilleur[8]
		else:
			qmeilleur5 = meilleur[9]
		if meilleur[10]["score"] > meilleur[11]["score"]:
			qmeilleur6 = meilleur[10]
		else:
			qmeilleur6 = meilleur[11]
		if meilleur[12]["score"] > meilleur[13]["score"]:
			qmeilleur7 = meilleur[12]
		else:
			qmeilleur7 = meilleur[13]
		if meilleur[14]["score"] > meilleur[15]["score"]:
			qmeilleur8 = meilleur[14]
		else:
			qmeilleur8 = meilleur[15]
		if qmeilleur1["score"] > qmeilleur2["score"]:
			dmeilleur1 = qmeilleur1
		else:
			dmeilleur1 = qmeilleur2
		if qmeilleur3["score"] > qmeilleur4["score"]:
			dmeilleur2 = qmeilleur3
		else:
			dmeilleur2 = qmeilleur4
		if qmeilleur5["score"] > qmeilleur6["score"]:
			dmeilleur3 = qmeilleur5
		else:
			dmeilleur3 = qmeilleur6
		if qmeilleur7["score"] > qmeilleur8["score"]:
			dmeilleur4 = qmeilleur7
		else:
			dmeilleur4 = qmeilleur8
		if dmeilleur1["score"] > dmeilleur2["score"]:
			fmeilleur1 = dmeilleur1
		else:
			fmeilleur1 = dmeilleur2
		if dmeilleur3["score"] > dmeilleur4["score"]:
			fmeilleur2 = dmeilleur3
		else:
			fmeilleur2 = dmeilleur4
		enfants = enfantPop(fmeilleur1,fmeilleur2,g,p,E)

		enfant_pop.append(enfants)
		enfant_pop.append(enfants)

	return enfant_pop

# Création de la population enfant
def enfantPop(parent1,parent2,g,p,E):
	scorpion = {}
	a  = parent1["a"]
	Lb = parent1["Lb"]
	b  = parent1["b"]
	h  = parent1["h"]

	Lc = parent2["Lc"]
	Lf = parent2["Lf"]
	v  = parent2["v"]
	Df = parent2["Df"]


	toChange = random.randrange(1,100)
	if toChange == 1:
		valueToChange = random.randrange(1,8)
		if valueToChange == 1:
			a  = radians(random.randrange(0,90))
		elif valueToChange == 2:
			Lb = random.randrange(1,15)
		elif valueToChange == 3:
			b  = random.randrange(1,15)
		elif valueToChange == 4:
			h  = random.randrange(1,15)
		elif valueToChange == 5:
			Lc = random.randrange(1,15)
		elif valueToChange == 6:
			Lf = random.uniform(1,2)
		elif valueToChange == 7:
			v  = random.uniform(0.24,0.30)
		elif valueToChange == 8:
			Df = random.uniform(0.01,0.05)


	K  = RessortK(E,v)
	Lv = LongeurAVide(Lb,Lc)
	Ld = LongueurDeplacement(Lf,Lv)
	mp = MasseProjectile(p,Df,Lf)
	V  = VelociteV(K,Ld,mp)
	d  = PorteeP(V,g,a)
	Ec = EnergieImpact(mp,V)
	Et = JouleToTNT(Ec)
	I = MomentQuadratique(b,h)
	F = ForceDeTraction(K,Ld)
	f = FlecheBras(F,Lb,E,I)

	scorpion.ajout({"a":a,"Lb":Lb,"b":b,"h":h,"Lc":Lc,"Lf":Lf,"v":v,"K":K,"Lv":Lv,"Ld":Ld,"Df":Df,"mp":mp,"V":V,"d":d,"Ec":Ec,"Et":Et,"I":I,"F":F,"f":f})

	return scorpion

#--------------------------------------------------------------#	
#---------------------début du jeux de tir---------------------#
#--------------------------------------------------------------#	

# Génération de la population
population = randomScorpions(taille_population,g,p,E)

for i in range(0,generation):

	#test de la population
	population = test(population)
	
	#variables pour la courbes
	scoreMax = 1
	scoreMin = 10
	listaverage = []
	xgeneration.append(i)
	
	#classement
	for scorpion in population:
		listaverage.append(scorpion["score"])
		if scorpion["score"] > scoreMax:
			scoreMax = scorpion["score"]
		if scorpion["score"] < scoreMin:
			scoreMin = scorpion["score"]

	#géneration de la moyenne
	moyenne = np.average(listaverage)

	#mise dans l'axe di min, max, moy
	yMoy.append(moyenne)
	yMax.append(scoreMax)
	yMin.append(scoreMin)
	
# Génération des enfants
	population = selection(population, taille_population,g,p,E)

# Affichage
plt.plot(xgeneration, yMax,'r',xgeneration,yMoy,'b',xgeneration,yMin,'g')
plt.ylabel('scores')
plt.xlabel('génération')
plt.show()	
