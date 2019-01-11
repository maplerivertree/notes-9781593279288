l = [i**1 for i in range(1,11,1)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#forward slice
print(l[1:2]) #prints position '1'
print(l[1:0]) #prints position that doesn't exist
print(l[2:])  #prints from position 2 to infinity
print(l[0:])  #prints the entire list
print(l[-100:]) #prints the entire list

#backward slice
print(l[:3])  #prints from beginning of the list to position 2
print(l[:-3]) #prints from beginning of the list to position -4 NOT -2
print(l[2:-3]) #prints from position 2 to position -4 

#clarity
print(l[-3:]) #prints from position -3 to infinity
print(l[-9:4]) #prints from position -9 to position 3
print(l[-5:-4]) #prints from position -5 to position -5
