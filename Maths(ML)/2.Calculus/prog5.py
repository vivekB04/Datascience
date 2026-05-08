#Limits
#code 3.1 : defining "infinite Training "

def error_limit(n):
    return 5/n+0.1

print(f"Error with 1M samples: {error_limit(100000)}")

