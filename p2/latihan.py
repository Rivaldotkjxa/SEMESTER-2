olahraga =("voly","badminton","lompat","basket","futsal")
olahraga_list= list(olahraga)
print("tuple = ",olahraga)
print("list=",olahraga_list)
olahraga_list.append("tenis")
print(olahraga_list)
del olahraga_list[3]
print(olahraga_list)
olahraga_list[4]="sepakbola"
print(olahraga_list)
olahraga_tuple= tuple(olahraga_list)
print(olahraga_tuple)