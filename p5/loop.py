



print("\nLOOPING IN PYTHON")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda :"))
while a < b: #a < b adalah syarat
    print (a)
    a += 1 # increment
    
print("\nPengunaan break pada looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda"))
while a < b: # a < b adalah syarat 
    print(a)
    if a == 5: # seleksi kondisi
        break # seleksi kondisi
    a += 1 # increment
    
print("\nPengunaan continue pada looping")
print("-------------------\n")
a = 0
b = float(input("masukakan angka anda : "))
while a < b: # a < b: # a < b adalah syarat
    a += 1 #increment
    if a == 5: # seleksi kondisi
        continue # continue point
    print(a)
    
print("\nPengunaan if else dalam looping")
print("-------------------\n")
a = 0
b = float(input("masukan angka anda: "))
while a < b:
    if a == (b-1):
        print("perulangan berhenti")
        break;
    else:
        print("perulangan ke -",a)
        a += 1
     