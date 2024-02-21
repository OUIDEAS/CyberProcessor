import os
import re
import glob
import ast, json
import shutil
def check_consistency(base_directory):
    directory_prefixes = {}  # Dictionary to store prefixes for each directory
    
    # Iterate through each subdirectory
    for subdirectory in os.listdir(base_directory):
        subdirectory_path = os.path.join(base_directory, subdirectory)
        
        if os.path.isdir(subdirectory_path):
            print(f"Checking directory: {subdirectory_path}")
            prefixes = set()  # Use a set to store unique prefixes for each directory
            
            # Iterate through each file containing "record" in the filename
            for filename in os.listdir(subdirectory_path):
                if "record" in filename:
                    file_path = os.path.join(subdirectory_path, filename)
                    
                    # Extract the first 14 digits from the filename
                    match = re.match(r'^(\d{14})', filename)
                    if match:
                        prefix = match.group(1)
                        
                        # Add the prefix to the set
                        prefixes.add(prefix)
                        
                        # Print the filename and its corresponding prefix
                        print(f"{filename}: {prefix}")
            
            # Store the set of prefixes for this directory
            directory_prefixes[subdirectory] = prefixes
    
    # Check for consistency and print the result
    print("Consistency check result:")
    for directory, prefixes in directory_prefixes.items():
        if len(prefixes) > 1:
            print(f"Directory {directory} has multiple prefixes: {prefixes}")

            filelist = sorted(glob.glob(base_directory+"/"+directory))

            data_dir = base_directory+directory

            print(data_dir)

            for fname in filelist:
                morefiles = sorted(glob.glob(fname+"/*"))
                for mfname in morefiles:
                    if(mfname.endswith(".json") and 'VanDrive_Comments' not in mfname and 'comments' not in mfname):
                        print(mfname)
                        
                        # for pre in prefixes:
                        #     # Copy the JSON file
                        #     try:
                        #         shutil.copyfile(mfname, data_dir+"/"+str(pre)+".json")

                        #         # Read the copied JSON file
                        #         with open(data_dir+"/"+str(pre)+".json", 'r') as file:
                        #             data = json.load(file)

                        #         data['file']['filebase'] = str(pre) + '.' + 'record' + '.'

                        #         # Write %the updated data back to the file
                        #         with open(data_dir+"/"+str(pre)+".json", 'w') as file:
                        #             print("DUMPED:", data_dir+"/"+str(pre)+".json")
                        #             json.dump(data, file, indent=4)
                        #     except:
                        #         print("PROBLEM WITH", mfname)
                        #         continue


        # else:
        #     print(f"Directory {directory} has consistent prefixes: {prefixes}")

# Provide the path to the desired directory
base_directory = "/home/tmoleski_linux/s3bucket/Deployment_2_SEOhio/GreenRoute/OU Pacifica/"

# Call the function to check consistency
check_consistency(base_directory)
