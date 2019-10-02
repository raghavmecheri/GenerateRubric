import pandas as pd
import json
import sys
import re
import os

def refactor_rules(gradepoints, namelist):
	rows = []
	for rule,points in gradepoints.items():
		row = {}
		row["Rule"] = rule
		row["Deduction"] = points
		for x in namelist:
			row[x] = 0
		rows.append(row)
	return rows

def are_invalid(name, grades, output):
	test_name = re.search(".txt$", name)
	test_grades = re.search(".json$", grades)
	test_output = re.search(".csv$", output)
	if((not test_name) or (not test_grades) or (not test_output)):
		return True
	return False

def delete_file(filename):
	if(os.path.exists(filename)):
		os.remove(filename)

if __name__ == "__main__":

	try:
		NAME_FILE = sys.argv[1]
		GRADE_FILE = sys.argv[2]
		OUTPUT_FILE = sys.argv[3]
	except:
		print("Please pass three command line arguements!")
		raise SystemExit

	if(are_invalid(NAME_FILE, GRADE_FILE, OUTPUT_FILE)):
		print("Please pass three filenames, a .txt namelist, a json rubric, and an output csv file in that order")
		raise SystemExit

	# delete_file(NAME_FILE)
	# delete_file(GRADE_FILE)
	delete_file(OUTPUT_FILE)

	print("Extracting names...")

	namelist = open(NAME_FILE,"r").read().split(',')

	while("" in namelist) : 
	    namelist.remove("")

	print("Extracting grades...")

	with open(GRADE_FILE) as json_file:
	    gradepoints = json.load(json_file)

	# print(namelist)
	# print(gradepoints)

	print("Compiling CSV...")

	cols = ["Rule", "Deduction"] + namelist
	my_csv = pd.DataFrame(columns=cols)

	row_entries = refactor_rules(gradepoints,namelist)
	my_csv = my_csv.append(row_entries)

	my_csv.to_csv(OUTPUT_FILE, index=False)

	print("Compiled CSV!")
