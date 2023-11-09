#contribution by- Atmaram Mahale  
from main_list import MainList

def main():
    k = int(input("Enter the value of k: "))
    input_list = input("Enter a list of numbers separated by spaces: ").split()
    
    # Remove leading and trailing spaces from input elements
    input_list = [x.strip() for x in input_list]


    if len(input_list) < k:
        print("Error: The length of the input list is less than k.")
        print("NOTE: The number of elements in the input list should be greater than k.")
        return
