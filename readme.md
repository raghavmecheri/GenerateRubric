# RubricGen
An automated grading rubric generator to make the lives of Instructors easier

# Usage
- Clone this repository
- Run the following command: ```
python3 generate_rubric.py "namelist.txt" "rubric.json" "rubric.csv"```
- Note: You may need to run ``` pip install pandas``` for this executable to run
<br>
Sample .txt and .json input files can be found in the samples/ directory. <br>
It's worth noting that the .json file has a "Total":0 row by design, to hold the total points deducted per student <br>

## Description
The purpose of this program is to compile a grading rubric spreadsheet automatically, for easy HW grading by TAs and instructors. <br>
A namelist and a rubric are both required for this program to run, both must be passed as args. A third arguement must also be passed,
which is the name of the output csv

## Courseworks Namelist Exctraction

To get this list from Courseworks: <br>
- Go to the People page for the class <br>
- Set the role to student <br>
- Run the below JS snippet in your browser console: <br>
	```javascript
	targets = document.getElementsByClassName("roster_user_name student_context_card_trigger");
	namelist = []
	for(x = 0; x < targets.length; x++) {
		namelist.push(targets[x].innerText);
	}
	console.log(namelist.toString());
	```
This should log a comma separated list that this program accepts :)
