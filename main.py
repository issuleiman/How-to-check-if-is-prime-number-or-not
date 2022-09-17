def prime_checker(number):
  is_true=True
  for i in range(2,n):
    if number % i ==0:
      is_true=False
  if is_true:
    print("is a prime number.")
  else:
    print("is  not a prime number. ")
