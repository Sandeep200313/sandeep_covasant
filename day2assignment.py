#Given a directory, find out the file Name having max size recursively 

import os
path = os.path.join(os.path.expanduser("~"), "Desktop")
max_size=-1
max_file=""
for root,d_names,f_names in os.walk(path):
    for f in f_names:
        full_path=os.path.join(root,f)
        size=os.path.getsize(full_path)
        if size>max_size:
            max_size=size
            max_file=full_path
            
print("Maximum file is:",max_file)
print("Maximum size of file is:",max_size)
        
