amount=int(input("please enter amount for withraw:"))
note_1=amount//100
note_2=(amount%100)//10
note_3=((amount%100)%50)//10
print("notes of 100rs",note_1)
print("notes of 50rs",note_2)
print("notes of 10rs",note_3)
