#from tempfile import NamedTemporaryFile
import shutil
import csv

filename_input = 'pandora_filepaths_no_commas.csv'
filename_output = 'pandora_filepath_output.csv'
filename_remove_commas = 'pandora_commas_removed.csv'
#tempfile = NamedTemporaryFile(mode='w', delete=False)

# fields = ['ID', 'Name', 'Course', 'Year']

with open(filename_output, 'w') as csvfile2:
    with open(filename_input, 'r') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile2)
        for row in reader:
            prev_row = row
            prefix = "s3://artstylequalificationsurveyallperiods/Pandora_V1-20220406T013528Z-001/Pandora_V1"
            print("row")
            print(row)
            row = [elem.strip(".") for elem in row]
            row = [prefix + elem for elem in row]

            writer.writerow(row)

with open(filename_remove_commas, 'w') as csvfile2:
    with open(filename_output, 'r') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile2)
        for row in reader:
            #prev_row = row
            #prefix = "s3://artstylequalificationsurveyallperiods/Pandora_V1-20220406T013528Z-001/Pandora_V1"

            row = [elem.replace(',', '\n') for elem in row]
            #row = [prefix + elem for elem in row]

            writer.writerow(row)

# with open('path_to_csv_file', 'r') as csv_file:
#     data = list(csv.reader(csv_file, delimiter=';'))

# data = [(int(raw_row[0]), float(raw_row[1].replace(',', '.'))) for row in data]

# with open('path_to_csv_file', 'w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     writer.writerows(data)

#shutil.move(tempfile.name, filename2)