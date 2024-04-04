'''
Name: Montgomery McHargue
Date: 04032024
File Name: Ch11-13Ex.py
Purpose: Write a function that reads a file of numbers and calculates the average of the numbers.

'''


def calculate(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    total += int(line())
                    count += 1
                except ValueError:
                    print("Error: Non-integer value found in the file. Skipping...")
            if count > 0:
                average = total / count
            else:
                average = 0
        return count, average
    except IOError:
        print("Error: File not found or could not be opened.")
        return 0, 0
    except Exception as e:
        print("An unexpected error occurred:", e)
        return 0, 0

def main():
    filename = 'section1.txt'  
    count, average = calculate(filename)
    print(f"Number of scores in the file: {count}")
    print(f"Average score: {average:.2f}")

if __name__ == "__main__":
    main()





