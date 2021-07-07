# put your python code here

group1 = int(input())
group2 = int(input())
group3 = int(input())

group1_desks = ((group1 % 2) + (group1 // 2))
group2_desks = ((group2 % 2) + (group2 // 2))
group3_desks = ((group3 % 2) + (group3 // 2))

print(group3_desks + group1_desks + group2_desks)
