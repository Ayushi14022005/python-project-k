#contribution by - Jay Gaonkar
   def save_sublists_to_file(self, k, filename):
       sublists = self.generate_k_sublists(k)
       with open(filename, 'w') as file:
           for sublist in sublists:
               file.write(' '.join(map(str, sublist)) + '\n')

