# defined for answering question 1
def main():
    try:
        with open("input.txt", 'r') as file:
            for line in file:
                # Using list comprehension to filter out non-numeric characters
                numbers_only = [char for char in line if char.isdigit()]

                # Join the filtered characters to form the numeric string
                numeric_string = ''.join(numbers_only)

                # If there are numbers in the line, print them
                if numeric_string:
                    # print(numeric_string)
                    # Slice out all digits except for the first and last
                    modded_str = numeric_string[0] + numeric_string[-1]
                    print(modded_str)
    except FileNotFoundError:
        print(f"File not found: {'input.txt'}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
