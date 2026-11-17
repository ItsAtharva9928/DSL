# Implement Hash table in Python
import numpy as np
HT = np.zeros(10) #Initialize the hash table as zeros. Assumption that accept non zero keys only
#print("Hash Table:\n",HT)

def insert_record():
    for i in range(len(HT)):
        key = input("\nEnter key")
        ind = int(key) % 10
        #print(ind)
        if(HT[ind]==0):
            HT[ind] = key

        #Linear Probing without replacement
        else:             
            for j in range(len(HT)):
                ind = (int(key)+j) % 10
                if(HT[ind]==0):
                    HT[ind] = key
                    break

def display_record():
    print("Hash Table:\n",HT)

def search_record():
	Flag = 0
	key = int(input("\nEnter key to be search :"))
	for j in range(len(HT)):
           ind = (int(key)+j) % 10
           if(HT[ind]==key):
                 print("\nKey Found :")
			Flag = 1
			break
	if(Flag == 0):
		print("\nKey Not Found :")

def delete_record():
	key = int(input("\nEnter key to be delete :"))
	for j in range(len(HT)):
		ind = (int(key)+j) % 10
		if(HT[ind]==key):
			print("\nKey deleted successfully :")
			HT[ind]= 0
			break



# Main Program
choice1 = 0
while(choice1 != 4):
    print("1. Insert              *")
    print("2. Search              *")
    print("3. Display             *")
    print("3. Delete             *")
    print("4. Exit                *")
    choice1 = int(input("Enter Choice"))
    if choice1>5:
        print("Please Enter Valid Choice")
    if(choice1==1):
        insert_record()
    elif(choice1==2):
        add = search_record()
        print("Key Address",add)
        #if(add != -1):
        #    print("Key found at location ",add)
        #else:
        #    print("Key not found ")
    elif(choice1==3):
        display_record()
    elif(choice1==4):
	  delete_record()





