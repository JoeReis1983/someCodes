
def binary_to_decimal(binary):
    try:
        if not all(bit in '01' for bit in binary):
            raise ValueError("Binary number must contain only 0s and 1s")
        
        decimal = 0
        power = 0
        
        for digit in binary:
            if digit == '1':
                decimal += 2 ** power
            power += 1
            
        return decimal
    
    except ValueError as e:
        return str(e)

def main():
    binary = input("Enter a binary number: ")
    result = binary_to_decimal(binary)
    
    if isinstance(result, int):
        print(f"Decimal equivalent: {result}")
    else:
        print(f"Error: {result}")

if __name__ == "__main__":
    main()
