import subprocess
from random import randint

case_inputs = ['2271-7', '6335-2', '6140-6', '2374-4', '2400-0', '1851-5', '2933-5', '7318-7', '5202-0', '7910-0', '9660-4', '7256-3', '2359-6', '7688-0', '7142-8', '9292-4', '7547-1', '2325-0', '6296-8', '7379-6', '4778-7', '0657-2', '1282-8', '1361-0', '2674-6', '6150-0', '0033-6', '1136-8', '4943-8', '5144-0', '7215-8', '6277-9', '8531-8', '1427-6', '3115-8', '4167-4', '5791-5', '8905-9', '1962-4', '3329-9', '8332-4', '9801-8', '4968-5', '8629-1', '0132-3', '8954-6', '3564-4', '5856-1', '0980-7', '0492-3', '?539-8', '?718-6', '0?89-8', '4834-?', '0?69-5', '?896-0', '7592-?', '2702-?', '9?82-5', '074?-2', '833?-8', '71?3-9', '9298-?', '77?5-6', '?527-2', '6?49-8', '1597-8', '089?-2', '1520-?', '?903-6', '01?3-2', '760?-0', '?594-4', '96?8-1', '863?-5', '7690-?', '5114-?', '99?2-2', '023?-5', '0489-8', '604?-7', '86?8-1', '?349-8', '8177-8', '7?88-1', '4?63-4', '6907-?', '?371-8', '?661-3', '7428-4', '135?-5', '86?8-3',  '7865-0', '339?-6', '0007-?', '?127-7', '43?0-6']
case_outputs = ['INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'VALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', 'INVALID', '7539-8', '6718-6', '0589-8',  '4834-9', '0069-5', '5896-0',  '7592-0', '2702-6', '9782-5', '0747-2', '8338-8', '7133-9', '9298-4', '7775-6', '8527-2', '6449-8', 'INVALID', '0893-2', '1520-5', '1903-6', '0103-2', '7608-0', '2594-4', '9668-1', '8630-5', '7690-0', '5114-2', '9942-2', '0234-5', 'INVALID', '6049-7', '8628-1', '2349-8', 'INVALID', '7488-1', '4063-4', '6907-0', '6371-8', '7661-3', 'VALID', '1355-5', '8698-3',  'INVALID', '3398-6', '0007-5', '0127-7', '4300-6']

def get_new_digit():
	new_rand = randint(0, 9)
	if (new_rand == 10):
		new_rand = "X"
	return str(new_rand)

def run_test_case(input):
	process = subprocess.Popen("python3 the2.py", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	stdin = process.communicate(bytes(input,"utf-8"))
	stdout = str(process.communicate()[0])
	output = stdout[2:(len(stdout) - 3)]
	return output

#from stackoverflow
def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

#generate test cases from solution
case_count = 100
def gen_test_cases():
	inputs = []
	outputs = []
	for i in range(0, case_count):
		generated_input = ""
		if i >= case_count / 2:
			lucky_number = randint(0,5)
		else:
			lucky_number = -1
		for i in range(0,5):
			if (i == lucky_number):
				generated_input = generated_input + "?"
			else:
				generated_input = generated_input + get_new_digit()

		generated_input = insert(generated_input, "-", 4)
		inputs.append(generated_input)
		outputs.append(run_test_case(generated_input))

def run_test():
	grade = 0
	grade_step = 100 / len(case_inputs)
	for i in range(0, len(case_inputs)):
		wrong_output = run_test_case(case_inputs[i])
		if (wrong_output == case_outputs[i]):
			print("Passed test case " + str(i + 1))
			grade += grade_step
		else:
			print("FAILED test case " + str(i + 1))

	print("------")
	print("Grade: " + str(grade))

run_test()
