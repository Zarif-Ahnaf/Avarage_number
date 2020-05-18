input_number=int(input("How many numbers you want to avarage?:"))

total_sum=0

if (input_number>0) and (input_number!=0) and (input_number!=1):

  for i in range(input_number):

    number=float(int(input("Enter number:")))

    total_sum += number

else:

  print("Enter correct numbers")

average  = total_sum/input_number

print(average)
