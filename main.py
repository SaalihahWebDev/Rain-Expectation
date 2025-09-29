import math
print("Probability of exactly 6 rainy days:",math.exp(-10)*(10**6)/math.factorial(6))
print("Probability of 12-13 rainy days:",math.exp(-10)*(10**12)/math.factorial(12)+math.exp(-10)*(10**13)/math.factorial(13)+math.exp(-10)*(10**13)/math.factorial(14))