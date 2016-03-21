import os
import glob
import sys
import csv

#path="C:\\Users\\cathy\\Desktop\\in\\"

locus=[{} for i in range(1000000)]
set_bio = set(['A','G','T','C','a','g','t','c'])
set_alphabet = set(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
set_num=set(['1','2','3','4','5','6','7','8','9','0'])

class CountSeq:
    def __init__(self,total,subcount):
        self.total = total
        self.sub = subcount


#input_folder=os.listdir(path)
#for filepath in input_folder:
#    print (os.path.abspath(filepath))
#filepath="2.txt"
def read(filepath):
    with open(filepath) as f:
        reader = csv.reader(f, delimiter="\t")
        d=list(reader)
        for line in d:
            if (int(line[1]) < 43000000) or (int(line[1]) > 44000000):
                continue
            elif line[3] == 0:
                continue
            else:
                index=int(line[1])-43000000
                if(index==0):
                    continue
##                print("before",index,locus[index])
                if "+" in line[4] or "-" in line[4]:
                    if (len(line[4])==1) and ((line[4][0] == '.') or (line[4][0] == ',')):
                        if ((line[2].upper()) in set_bio):
                            if (line[2].upper()) not in locus[index]:
                                tmpSeq=CountSeq(1,{filepath:1})
##                                print("#",tmpSeq)
                                locus[index][line[2].upper()]=tmpSeq                  
                            else:
                                (locus[index][line[2].upper()]).total += 1
                                if filepath not in (locus[index][line[2].upper()]).sub:
                                    ((locus[index][line[2].upper()]).sub)[filepath] = 1
                                else:
                                    ((locus[index][line[2].upper()]).sub)[filepath] += 1
                                       
                    for i in range(1,len(line[4])):
                        if((line[4][i-1] =='.' or line[4][i-1] == ',') and (line[4][i] != '+') and (line[4][i] !='-')):
                            if ((line[2].upper()) in set_bio):
                                if (line[2].upper()) not in locus[index]:
                                    tmpSeq=CountSeq(1,{filepath:1})
##                                    print("##",tmpSeq)
                                    locus[index][line[2].upper()]=tmpSeq                   
                                else:
                                    (locus[index][line[2].upper()]).total += 1
                                    if filepath not in (locus[index][line[2].upper()]).sub:
                                        ((locus[index][line[2].upper()]).sub)[filepath] = 1
                                    else:
                                        ((locus[index][line[2].upper()]).sub)[filepath] += 1
                        elif((line[4][i-1] == '.' or line[4][i-1] == ',') and (line[4][i] == '+'or line[4][i] == '-')):
                            tmp=""
                            for j in range(i,len(line[4])):
                                if(line[4][j] in set_bio) or (line[4][j] == '+') or (line[4][j] == '-' ) :
                                    tmp+=line[4][j]
                                elif(line[4][j] in set_num) :
                                    continue
                                else:
                                    break
                            if (tmp!="") and (tmp not in locus[index]):
                                tmpSeq=CountSeq(1,{filepath:1})
##                                print("###",tmpSeq)
                                locus[index][tmp.upper()] = tmpSeq
                            elif (tmp!="") and (tmp in locus[index]):
                                locus[index][tmp.upper()].total +=1
                                if filepath not in (locus[index][tmp.upper()]).sub:
                                    ((locus[index][tmp.upper()]).sub)[filepath] =1
                                else:
                                    ((locus[index][tmp.upper()]).sub)[filepath] +=1
                        elif (line[4][i] == '^'):
                            continue
                        else:
                            continue
##                print(index,locus[index])
            #locus[index] = locus[index]
    #for i in range(43000000):
        #print(i,locus[i])
        #for k in locus[i]:
            #print (k,locus[i][k].total,locus[i][k].sub)
            #for o in locus[i][k].sub:
                #print("##",o,locus[i][k].sub[o])
    #print (locus[i])

        
##        print (index,locus[index])
##                if (line[4][0] != '.') and (line[4][0] != ',')
##                if line[4][0] == '.' or line[4][-1] == ',':
##                    if (line[2] == "A" or line[2]=="a") or (line[2] == "G" or line[2]=="g") or (line[2] == "C" or line[2]=="c") or (line[2] == "T" or line[2]=="t"):
##                        if ((line[2].upper()) not in locus[index]):
##                            locus[index][(line[2]).upper()]=CountSeq(1,{filepath:1})
####                            locus[index][(line[2]).upper()].total = 1
####                            locus[index][(line[2]).upper()].sub = {filepath:1}
##                        else:
##                            locus[index][(line[2]).upper()].total += 1
##                            if filepath not in locus[index][(line[2]).upper()].sub:
##                                locus[index][(line[2]).upper()].sub[filepath] = 1
##                            else:
##                                locus[index][(line[2]).upper()].sub[filepath] += 1

#for i in range(43000000):
#    print(locus[i])
#    for k in locus[i]:
#        print (k,locus[i][k].total,locus[i][k].sub)
#        for o in locus[i][k].sub:
#            print("##",o,locus[i][k].sub[o])
    #print (locus[i])
                    
for filepath in glob.glob("/home/liuhe38/data_mpileup/data_0316_whole/*mpileup"):
    read(filepath)

print(locus)

