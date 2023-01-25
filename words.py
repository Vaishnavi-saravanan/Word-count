#Developed by : VAISHNAVI S
#RegisterNumber:22009040
num_words =0
with open('words.py','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={0}".format(num_words))