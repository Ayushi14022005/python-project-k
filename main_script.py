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


    # Convert the input elements to integers
   
    main_list = MainList(input_list)
    
    # Save the unique k-sized sublists to a file
    main_list.save_sublists_to_file(k, f'unique_sublists_{k}.txt')
    print(f"Unique {k}-sized sublists have been saved to 'unique_sublists_{k}.txt'.")

if __name__ == "__main__":
    mainmain()
