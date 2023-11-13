#contribution by Ayushi Kamrani
from itertools import combinations
class MainList:
    def __init__(self, input_list):
        self.input_list = input_list

    def generate_k_sublists(self, k):
        result = [list(comb) for comb in combinations(self.input_list,k)]
        
        print(f"Total Combinations are:",len(result))
        return result
        
#contribution by -Jay Gaonkar

    def save_sublists_to_file(self, k, filename):
       sublists = self.generate_k_sublists(k)
       with open(filename, 'w') as file:
           for sublist in sublists:
               file.write(' '.join(map(str, sublist)) + '\n')
