import random
pattern = ["hi", "hi there", "hello", "hey", "good afternoon", "good morning", "good evening", "good day"]
response = ["hi", "hey", "hello","hello,how are you?"]
my_lst=[]
for i in pattern:
    for j in response:
        my_lst.append([i,j])
print(my_lst)