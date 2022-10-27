def add(P, Q):      
   return P + Q   
def subtract(P, Q):     
   return P - Q   
def multiply(P, Q):      
   return P * Q   
def divide(P, Q):       
   return P / Q       
print ("wybierz co chcesz robic")    
print ("a. dodac")    
print ("b. odjac")    
print ("c. pomnozyc")    
print ("d. podzielic")    
    
choice = input("podaj wybor: ")    
    
a = int (input ("podaj 1 liczbe "))    
b = int (input ("podaj 2 liczbe "))    
    
if choice == 'a':    
   print (add(a, b))    
    
elif choice == 'b':    
   print (subtract(a, b))    
    
elif choice == 'c':    
   print (multiply(a, b))    
elif choice == 'd': 
    if b == 0 :
        print("nie dzieli przez 0") 
    else:  
        print (divide(a, b))    
else:    
   print ("zle podales/as")   