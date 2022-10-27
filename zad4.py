l = input("Wpisz litere ")
chng_l =""
for i in range (len(l)):
    if l[i].isupper():
        chng_l += l[i].lower()
    elif l[i].islower():
        chng_l += l[i].upper()
    else:
        chng_l += l[i]
print(chng_l)