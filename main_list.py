from itertools import combinations

class MainList:
    def __init__(self, input_list):
        self.input_list = input_list

    def generate_k_sublists(self, k):
        result = [list(comb) for comb in combinations(self.input_list,k)]
        
        print(f"Total Combinations are:",len(result))
        return result
