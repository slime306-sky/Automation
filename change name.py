import os

def rename_files(directory, i, end=59):
    while i >= end:
        prefix = f"program_{i}"
        for filename in sorted(os.listdir(directory)):
            if filename.startswith(prefix):
                new_filename = f"program_{i+1}.cpp"
                
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
                i -= 1
                break 

# Example usage
directory = r"add file path"
rename_files(directory, i=77)


#i is file name where start's changing file name
#end is file name where it stops
