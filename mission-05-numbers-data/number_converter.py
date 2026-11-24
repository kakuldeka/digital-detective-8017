#!/usr/bin/env python3
"""
Number Converter Program
Converts user-supplied decimal numbers into binary and hexadecimal representations.
"""

def main():
    print("====================================")
    print(" Digital Detective Number Converter ")
    print("====================================")
    try:
        user_input = input("Enter a positive decimal integer: ").strip()
        num = int(user_input)
        if num < 0:
            print("Error: Please enter a positive integer.")
            return

        bin_val = bin(num)
        hex_val = hex(num)

        print("\n--- Conversion Results ---")
        print(f"Decimal Value:     {num}")
        print(f"Binary (bin()):    {bin_val} (raw bits: {bin_val[2:]})")
        print(f"Hexadecimal (hex): {hex_val} (uppercase: {hex_val[2:].upper()})")
        print("--------------------------\n")
    except ValueError:
        print("Error: Invalid input. Please enter a valid decimal integer.")

if __name__ == "__main__":
    main()
