import random
rresult = {1:0, 2:0, 3:0, 4:0, 5:2, 6:0, 7:2, 8:0, 9:2, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0}
true_results = 0
false_resuls = 0
true_ansvers = {1:5, 2:3, 3:2, 4:4, 5:2, 6:4, 7:2, 8:4, 9:2, 10:1, 11:1, 12:4, 13:1, 14:5, 15:2, 16:3, 17:3, 18:5, 19:5, 20:2}
question = {1:5, 2:3, 3:2, 4:4, 5:2, 6:4, 7:2, 8:4, 9:2, 10:1, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False}

for q in range(100):
    




# print(question)

    for i in range(1,11):
        r = random.randint(1,5)
        question[10+i] = r
    for b, c in question.items():
        if true_ansvers[b] == question[b]:
            true_results +=1
        else:
            false_resuls +=1
    s = false_resuls//4
    z = true_results-s
    print(z)

  
    rresult[z] = rresult[z] +1
        
print(rresult)

# print(question)

