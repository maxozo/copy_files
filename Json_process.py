import os
import glob
import shutil
import argparse
# run like python Json_process.py -ip /Users/christianodaniel/Documents/work/Json_Process/Folders -os Windows -d /Users/christianodaniel/Documents/work/Json_Process/Destination
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument(
        '-ip', '--input_path',
        action='store',
        dest='input_path',
        required=True,
        help='input_path'
)
parser.add_argument(
    "-d", "--destination", action='store',
        dest='Destination',
        required=True,
        help='Destination'
)

parser.add_argument(
    "-os", "--operating_system", action='store',
        dest='operating_system',
        required=True,
        help='Destination'
)

args = parser.parse_args()

input_path =args.input_path
Destination =args.Destination
Os = args.operating_system
# Sample inputs
# input_path = "/Users/christianodaniel/Documents/work/Json_Process/Folders"
# Destination = "/Users/christianodaniel/Documents/work/Json_Process/Destination"
if (Os =='Windows'):
    Files = glob.glob(f"{input_path}\*\*.json")
    for file1 in Files:
        name2 = file1.split('\\')[-1]
        shutil.copyfile(file1, f"Destination\{name2}")
    print('Done Windows')
elif (Os=='Linux'):
    Files = glob.glob(f"{input_path}/*/*.json")
    for file1 in Files:
        name2 = file1.split('/')[-1]
        shutil.copyfile(file1, f"Destination/{name2}")
    print('Done Linux')