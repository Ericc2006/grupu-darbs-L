
# uzdevuma risinājuma funkcijas katrs uzrakstījis savā failā un šos failus jāimportē pamatfailā
import erik 
import linard 
# ...............
 
def main():
	while True:
		print("""
    	1. Atņemšana
    	2. Reizināšana
   		3. Beigt darbu ar programmu
            """)
		izvele = int(input("Ievadi izvēli: "))
		a = int(input("Ievadi 1 skaitli: "))
		y = int(input("Ievadi 2 skaitli: "))
		if izvele == 1:
			linard.atn(a,y)
		elif izvele == 2:
			erik.reiz(a,y)
		elif izvele == 3:
			break

main()
