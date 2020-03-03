answer01 = 12
answer02 = 3
answer03 = 10
answer04 = 20
answer05 = 30
ctr = 0

print("\nI am going to ask you 5 Questions\n")
answer01Input = input("Can you tell me what 10 + 2 equals? : ")
answer02Input = input("Can you tell me what first answer / 4 equals? : ")
answer03Input = input("Can you tell me what previous answer + 7 equals? : ")
answer04Input = input("Can you tell me what previous answer X 2 equals? : ")
answer05Input = input("Can you tell me what the previous answer + 10 equals? : ")

if answer01Input == answer01 :
    print (" Question 1 You were correct :)")
    ctr += 1
if answer02Input == answer02 :
    print (" Question 2 You were correct :)")
    ctr += 1
if answer03Input == answer03 :
    print (" Question 3 You were correct :)")
    ctr += 1
if answer04Input == answer04 :
    print (" Question 4 You were correct :)")
    ctr += 1
if answer05Input == answer05 :
    print (" Question 5 You were correct :)")
    ctr += 1