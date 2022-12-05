
# uzdevuma risinājuma funkcijas katrs uzrakstījis savā failā un šos failus jāimportē pamatfailā
import erik 
import linard 
# ...............
 
def main():
	while True:
		print("""
    	1. Atņemšana
    	2. Reizināšana
		3. kāpinājums pakāpe
		4. saskaitīšana
		5. atņemšana
		6. skaitļu pārbaude
		7. vidējais aritmetiskais
   		8. Beigt darbu ar programmu
		
            """)
		izvele = int(input("Ievadi izvēli: "))
		a = int(input("Ievadi 1 skaitli: "))
		y = int(input("Ievadi 2 skaitli: "))
		if izvele == 1:
			linard.atn(a,y)
		elif izvele == 2:
			erik.reiz(a,y)
		elif izvele == 3:
			erik.kap(a,y)
		elif izvele == 4:
			linard.summa(a,y)
		elif izvele == 5:
			linard.atn(a,y)
		elif izvele == 6:
			linard.liel(a,y)
		elif izvele == 7:
			linard.vidap(a,y)
		elif izvele == 8:
			break

main()
