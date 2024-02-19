def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

def is_prime(n):
    if n < 2:
        return 0
    else:
        for i in range(2, int(n * 0.5) + 1):
            if n % i == 0:
                return "Not prime"
        else:
            return "Is prime"
<<<<<<< HEAD
<<<<<<< Updated upstream
=======

def is_power_of_5(num):
    return num & (num - 1) == 0 and num != 0

def is_power_of_2(num):
    return num & (num - 1) == 0 and num != 0
>>>>>>> Stashed changes
=======

def is_power_of_5(num):
    return num & (num - 1) == 0 and num != 0
>>>>>>> dev5
