
# uzdevuma risinājuma funkcijas katrs uzrakstījis savā failā un šos failus jāimportē pamatfailā
import erik 
import linard 
# ...............
 
def main():
while True:
        print("""
    		1. darbība
    	2. darbība
	…………..
   		3. Beigt darbu ar programmu
            """)
    	izvele = int(input("Ievadi izvēli: "))
    	if izvele == 1:
            		funkcija1()
    	elif izvele == 2:
      	  	funkcija2()
    	elif izvele == 3:
        		break 
main()
