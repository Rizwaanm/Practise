print("Prime numbers between 1 and 250 are:")

for x in range(1,250):
   # all prime numbers are greater than 1
   if x > 1:
       for y in range(2, x):
           if (x % y) == 0:
               break
       else:
           print(x)
           prime = open("results.txt", "a")
           prime.write(str(x))
           prime.write("\n")
prime.close()
