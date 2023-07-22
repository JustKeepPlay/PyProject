#Parinyawat Saenthaweesuk
animals =["dog","cat","bat","cock","cow","pig","fox","ant","bird","bat","lion","wolf","deer","bear","frog","hen","mole","duck","goat" ]

def count_animal(txt):
    count = 0
    found = set()

    for i in animals :
        if i in txt:
            count+=1
            found.add(i)
            txt = txt.replace(i,"",1)

    return print("Number of animals is ",count," ",found)

        

count_animal("goatcode") #have 2 animals (dog ,cat)
count_animal("cockdogwdufrbir") #have 4 animals (cow ,duck , frog , bird)
count_animal("dogdogdog") #have 3 animals (dog , dog ,dog)
