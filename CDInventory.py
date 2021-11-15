#------------------------------------------#
# Title: CDInventory.py
# Desc: Modification of a solution of Assignment04. 
#       The goal is to use dictionaries as the inner data type.
# Change Log: (Who, When, What)
# HLiang, 2021-Nov-14, Created File
#------------------------------------------#


# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstTbl = []
lstTbl1 = []
dicRow = {}
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        print('ID, CD Title, Artist')
        objFile = open(strFileName, 'r')
        data = objFile.read()
        objFile.close()
        print(data)   

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        #error handling
        try:
            intID = int(strID)
        except:
            print('Please input a valid ID number!')
            intID ='N/A'
                    
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID':intID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ",")
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        idNum = input('What\'s the entry\'s ID number?' )
        for row in lstTbl:
            if row['ID'] == int(idNum):
                lstTbl.remove(row)
            else:
                pass
   
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for var in row.values():
                strRow += str(var) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

