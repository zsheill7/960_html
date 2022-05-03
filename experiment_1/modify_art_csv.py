import csv
import os
import random

filename_input = 'pandora_filepaths_input.csv'
filename_output = 'pandora_filepath_output.csv'

path = "/Users/zoe/Documents/classes-sp22/9.60/Pandora_V1"

# Takes all the files in the current file directory and adds the name in directory to a CSV
# Resulting CSV example line: HighRenaissance/25114.jpg
with open(filename_input, 'w') as f:
    writer = csv.writer(f)
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if '.jpg' in f:
                filepath = root + os.sep + f
                print("filepath")
                print(filepath)
                last_part = filepath.split("Pandora_V1/")[1]
                writer.writerow([last_part])

# Should end up being >7000 image links
total_links = []

# Take all the file lines from the previous file
# 1. Add a prefix link to make sure it links to Amazon AWS
# 2. Remove commas
# 3. Remove weird special characters
with open(filename_output, 'w') as csvfile_output:
    with open(filename_input, 'r') as csvfile_input:
        reader = csv.reader(csvfile_input)
        writer = csv.writer(csvfile_output)
        for row in reader:
            prev_row = row
            prefix = "https://artstylequalificationsurveyallperiods.s3.amazonaws.com/Pandora_V1-20220406T013528Z-001/Pandora_V1/"

            # The row should just have one element, the image link
            image_link = row[0]
            
            # Add image link prefix to image link
            image_link = prefix + image_link
            total_links.append(image_link)

            row = [image_link]

            # Image titles with commas doesn't work with CSVs
            # There is also a weird A-like character that doesn't work
            if "," not in image_link and "tienne Istv" not in image_link:
                writer.writerow(row)

# Make 10 CSVs of 15 image links each
# Image link subset is random
for i in range(0, 10):
    random_15 = random.sample(total_links, 15)
    print("random_15")
    print(random_15)
    try:
        os.mkdir("random_15_images_csv") 
    except OSError as error: 
        print(error)  
    with open("random_15_images_csv/random_15_" + str(i) + ".csv", 'w') as random_csvfile:
        writer = csv.writer(random_csvfile)
        for row in random_15:
            writer.writerow([row])
