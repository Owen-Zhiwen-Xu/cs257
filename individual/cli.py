# NAME: cli.py - command-line interface exercise
# SYNOPSIS: python3 cli.py crime by district
# DESCRIPTION: Displays a list of all crimes committed in the specified district, based on partial crime records from Los Angeles in 2020.
import argparse
import csv
def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Display all crimes by district')
    parser.add_argument('district', metavar='district', nargs='+', help='one district in LA')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def get_crimes(district):
    crimes = []
    area_name = 5
    crime_type = 9
    with open('data/Crime_Data_from_2020_part.csv') as f:
        reader = csv.reader(f)
        for crime_row in reader:
            #print(f'here is area name: {crime_row[area_name]}, here is the crime: {crime_row[crime_type]}')
            print(district)
            if crime_row[area_name] == district:
                crimes.append(crime_row[crime_type])
    return crimes

def main():
    arguments = get_parsed_arguments()
    district = arguments.district[0]
    crimes = get_crimes(district=district)
    print(f'here is the some of the crimes in {district}: {crimes}')

if __name__ == '__main__':
    main()