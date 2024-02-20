import os
import re

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
            
            print()  # Add an empty line for better readability
    
    # Check for consistency and print the result
    print("Consistency check result:")
    for directory, prefixes in directory_prefixes.items():
        if len(prefixes) > 1:
            print(f"Directory {directory} has multiple prefixes: {prefixes}")
        else:
            print(f"Directory {directory} has consistent prefixes: {prefixes}")

# Provide the path to the desired directory
base_directory = "/home/croback_linux/s3bucket/Deployment_2_SEOhio/Blue Route/TRCVan2/"

# Call the function to check consistency
check_consistency(base_directory)
