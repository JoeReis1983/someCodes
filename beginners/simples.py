import random

def random_number(min,max):
    return random.randint(min,max)



def main():
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))
    print(random_number(min_value, max_value))
    
if __name__ == "__main__":
    main()