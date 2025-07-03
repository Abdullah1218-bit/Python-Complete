# a={'apple', 'bowl',False}
# print(type(a))
# b={  }
# print(type(b))
#                      #method to make empty set
# e=set()
# print(type(e))

# p={12 ,123,32,32,32,12,4,5,6,5,7,65,675}
# print(p)
# # WE CANNOT SORT SET
#                                #METHODS
 
# c={1,2,4,62,True,"fruits"}
# print(c,type(c))

                          #ADD METHOD
# z={1,True,'hello','boy', 12.72}
# z.add('12.78')
# print(z) 
#                                 #REMOVE METHOD
# ab={43,24,124,'HELLO',False}
# ab.remove(43)
# print(ab)
# print(len(ab))                    #LENGTH METHOD

#                                  #UNION METHOD

# s1={0,4,2,1,4,7,9,12}
# p2={4,9,6,1,0,8}

# print(s1.union(p2))                 # IT INCLUDE ALL ELEMENTS,NUMBER

# print(s1.intersection(p2))          # IT ONLY GIVES REPEATED VALUES
# print(s1-p2)
# print(p2-s1)
                                              
#                                 #SUBSET AND SUPERSET
set1={1,2,86,9,45,6,7,53}
print({1,53}.issubset(set1))

set2={99,64,72,81,49}
print({49,99}.issubset(set2))

set3={89,74,12,11}
set4={89,11}
print(set3.issuperset(set4))