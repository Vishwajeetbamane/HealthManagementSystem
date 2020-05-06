#Author : Vishwajeet Bamane
#Last Modified on : 05/05/2020

#Included names = Suryakant,Ujawalla,Pallavi

print("Welcome to Health Manangement System\n")

import datetime
datetime1 = datetime.datetime.now()


def Suryakant():
	var2 = input("Save or Retrieve?")
	if var2 == "Save":
		DorE = input("Where you want to login?\nDiet or Exercise?")
		if DorE == "Diet":
			hda = input("What you ate?\n")
			
			Hdf = open("SuryakantDiet.txt","a")
			Hdf.write(str(datetime1)+"  "+hda+"\n")
			Hdf.close()


		if DorE == "Exercise":
			hea = input("What exercise you did?\n")
			Hef = open("SuryakantExercise.txt","a")
			Hef.write(str(datetime1)+"  "+hea+"\n")
			Hef.close()
			
			
	if var2 == "Retrieve":
		print("Here it is.\n")
		hdr = open("SuryakantDiet.txt")
		print(hdr.read())
		her = open("SuryakantExercise.txt")
		print(her.read())
		hdr.close()
		her.close()

			
def Ujawalla():
	var3 = input("Save or Retrieve?")
	if var3 == "Save":
		DorE = input("Where you want to login?\nDiet or Exercise?")
		if DorE == "Diet":
			rda = input("What you ate?\n")
			
			rdf = open("UjawallaDiet.txt","a")
			rdf.write(str(datetime1)+"  "+rda+"\n")
			rdf.close()

			
		if DorE == "Exercise":
			rea = input("What exercise you did?\n")
			ref = open("UjawallaExercise.txt","a")
			ref.write(str(datetime1)+"  "+rea+"\n")
			ref.close()

			
	if var3 == "Retrieve":
		print("Here it is.\n")

		rdr = open("UjawallaDiet.txt")
		print(rdr.read())
		rer = open("UjawallaExercise.txt")
		print(rer.read())		
		rdr.close()	
		rer.close()


def Pallavi():
	var4 = input("Save or Retrieve?")
	if var4 == "Save":
		DorE = input("Where you want to login?\nDiet or Exercise?")
		if DorE == "Diet":
			kda = input("What you ate?\n")
			
			kdf = open("PallaviDiet.txt","a")
			kdf.write(str(datetime1)+"  "+kda+"\n")
			kdf.close()

	
		if DorE == "Exercise":
			kea = input("What exercise you did?\n")
			kef = open("PallaviExercise.txt","a")
			kef.write(str(datetime1)+"  "+kea+"\n")
			kef.close()

		
	if var4 == "Retrieve":
		print("Here it is.\n")
		
		kdr = open("PallaviDiet.txt")
		print(kdr.read())
		ker = open("PallaviExercise.txt")
		print(ker.read())
		kdr.close()
		ker.close()

		
def Vishwajeet():
	var5 = input("Save or Retrieve?")
	if var5 == "Save":
		DorE = input("Where you want to login?\nDiet or Exercise?")
		if DorE == "Diet":
			vda = input("What you ate?\n")
			
			vdf = open("VishwajeetDiet.txt","a")
			vdf.write(str(datetime1)+"  "+vda+"\n")
			vdf.close()

			
		if DorE == "Exercise":
			vea = input("What exercise you did?\n")
			vef = open("VishwajeetExercise.txt","a")
			vef.write(str(datetime1)+"  "+vea+"\n")
			vef.close()

		
	if var5 == "Retrieve":
		print("Here it is.\n")
		
		vdr = open("VishwajeetDiet.txt")
		print(vdr.read())
		ver = open("VishwajeetExercise.txt")
		print(ver.read())
		vdr.close()
		ver.close()

			

name = input("Enter the name:\n")
if name == "Suryakant":
	Suryakant()
if name == "Ujawalla":
	Ujawalla()
if name == "Pallavi":
	Pallavi()
if name == "Vishwajeet":
	Vishwajeet()
else:
	print("Sorry! This name is not in database")
