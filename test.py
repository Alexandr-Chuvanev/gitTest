a=[1,2,3,4,5,6,7,8]
b=[2,4,6,8,10,12]
a_set,b_set = set(a),set(b)
a_and_b=set.symmetric_difference(a_set,b_set)
print(a_and_b)