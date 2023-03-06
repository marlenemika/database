import os

# get the current working directory
cwd = os.getcwd()

# get all files in the directory
files = os.listdir(cwd)

# loop through each file
for file in files:
    # check if the file is a txt file
    if file.endswith(".txt"):
        # open the file
        with open(file, "r") as f:
            # read the contents of the file
            contents = f.readlines()
        
        # replace the first letter of each line with 1
        new_contents = []
        for line in contents:
            new_line = "1" + line[1:]
            new_contents.append(new_line)
        
        # write the new contents to the file
        with open(file, "w") as f:
            for line in new_contents:
                f.write(line)

# Done!
print("Replacement completed.")