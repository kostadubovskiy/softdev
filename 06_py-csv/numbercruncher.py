'''
Flying Chihuahuas: Nicholas Tarsis, Kosta Dubovskiy
Soft Dev
#6
22-09-30
'''

'''
DISCO:
*Global/local variable scope in python
*fileinput
QCC:

'''
import random
import fileinput

def read():
    curr = []
    for line in fileinput.input(files = "occupations.csv"):
        if "\"" in line:
            line = line.strip().split("\"")[1:]
            line[1] = line[1][1:]
        else:
            line = line.strip().split(",")
        
        try:
            line[-1] = float(line[-1])
        except:
            pass
        curr.append(line)
    
    return curr[:-1] + [['Other', 0.2]]
    
def make_dict(l):
    result = {}
    for line in l:
        result[line[0]] = line[1]
    return result

def weighted_select(d):
    rnum = random.random() * 100
    print(rnum)
    running_val_sum = 0
    line = 0
    for k in d:
        if line != 0:
            running_val_sum += d[k]
        if running_val_sum >= rnum:
            return k
        line += 1 
d1 = {
    "hi" : 50,
    "hello": 30,
    "wassup": 20
    }
# print(weighted_select(d1))
# final test
print(f"read: {read()}")
print(f"dict: {make_dict(read())}")
print(weighted_select(make_dict(read())))
