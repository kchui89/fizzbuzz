
def fizzbuzz(start, end):
 for num in range(start,end):
  if num % 3 == 0: 
   print("fizz")
  elif num % 5 == 0:
   print("buzz") 
  else:
   print(num)
  
 


def main():
 fizzbuzz(1,101)

if __name__ == "__main__":
    main()