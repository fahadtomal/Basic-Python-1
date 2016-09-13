__author__ = 'Tomal- PC'

 #LISTS IN ONE LIST.........EVERY ITEM/DATA/OBJECT CAN BE ANOTHER LIST
 #SO, EVERY LIST IS A COLLECTION OF ITEMS(DATA) SURROUNDED BY SQUARE BRACKET AND ITEMS ARE SEPARATED BY COMMAS. ANY ITEM CAN BE ANOTHER LIST

NAME =['TOMAL ', 'FAHAD ' , ['MOSTAQUE' , [ 'JOARDER' , 'MOHAMMED' ]]] ;   #INDEX -->> [0 , 1 , [[2]0 , [[1]0 , 1  ]]]

print(NAME[2][1][1]);
print(NAME[2][0]);
print(NAME[1]);
print(NAME[2][1][0]);
print(NAME[0]);

print("\n");




# INDEX PRACTISE

NUM = [0 , 1 , 2 ,   [3 , 4, 5 , 6 ,   [4 , 5 , 6 , 7 , 8 , 9 ,  [6 , 7 , 8 ,9 , 10          ]]]] ;    #INDEX 0,1,2,[3]0,1,2,3,[4]0,1,2,3,4,5,[6]0,1,2,3,4(most important)


print(NUM);                                 # TO SHOW ALL THE LISTS
print(NUM[0]);                              # perticular data/element of list 1
print(NUM[1]);                              #  "
print(NUM[2]);                              #  "

print("\n");


print(NUM[3]);                              #  TO SHOW ALL THE LISTS FROM LISTS 2(INDEX [3] FROM LIST 1(FROM 0 (START)))
print(NUM[3][0]);                           #  perticular data/element of list 2
print(NUM[3][1]);                           # perticular data/element of list 2
print(NUM[3][2]);                           # perticular data/element of list 2
print(NUM[3][3]);                           # perticular data/element of list 2

print("\n");


print(NUM[3][4]);                           # TO SHOW ALL THE LISTS FROM LISTS 3(INDEX [4] FROM LIST 2(INDEX [3] FROM LIST 1(FROM 0(START))))
print(NUM[3][4][0]);                        #  perticular data/element of list 3
print(NUM[3][4][1]);                        #  perticular data/element of list 3
print(NUM[3][4][2]);                        #  perticular data/element of list 3
print(NUM[3][4][3]);                        #  perticular data/element of list 3
print(NUM[3][4][4]);                        #  perticular data/element of list 3
print(NUM[3][4][5]);                        #  perticular data/element of list 3

print("\n");

print(NUM[3][4][6]);                        #TO SHOW ALL THE LISTS FROM LISTS 4(INDEX [6] FROM LIST 3(INDEX [4] FROM LIST 2(INDEX [3] FROM LIST 1(FROM 0 (START)))))
print(NUM[3][4][6][0]);                     #  perticular data/element of list 4
print(NUM[3][4][6][1]);                     #  perticular data/element of list 4
print(NUM[3][4][6][2]);                     #  perticular data/element of list 4
print(NUM[3][4][6][3]);                     #  perticular data/element of list 4
print(NUM[3][4][6][4]);                     #  perticular data/element of list 4
