import subprocess

# Define the command to run the user's script
command = ["python", "sample.py"]

outputs = []

# Redirect input from the input file
with open('./tests/input/A/input_1.txt', "r") as input_file:
    output = subprocess.check_output(command, stdin=input_file, universal_newlines=True)

with open('./tests/output/A/output_1.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        outputs.append(line.strip())

# Print the output of the user's script
print(output)
print('\n'.join(outputs) + '\n')