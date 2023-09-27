from flask import Flask, render_template, request
import subprocess
numprobs = {'A': 2, 'B': 3, 'C': 5}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    prob = request.form.get('problem')
    lang = request.form.get('language')
    correct = 0
    if lang == 'cpp':
        subprocess.run(["g++.exe", "-std=c++17", "sample.cpp", "-o", "sample"], encoding="utf-8")
        for i in range(numprobs[prob]):
            inputs = []
            outputs = []
            with open(f'./tests/input/{prob}/input_{i+1}.txt') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    inputs.append(line.strip())
            with open(f'./tests/output/{prob}/output_{i+1}.txt') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    outputs.append(line.strip())
            test_out = subprocess.run(['sample'], capture_output=True, input=' '.join(inputs), encoding="utf-8")
            correct += (test_out.stdout == '\n'.join(outputs)+'\n')
    else:
        command = ["python", "sample.py"]
        for i in range(numprobs[prob]):
            outputs = []
            with open(f'./tests/input/{prob}/input_{i+1}.txt', "r") as input_file:
                output = subprocess.check_output(command, stdin=input_file, universal_newlines=True)

            with open(f'./tests/output/{prob}/output_{i+1}.txt') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    outputs.append(line.strip())
            correct += (output == '\n'.join(outputs)+'\n')

    return render_template('answers.html', correct=correct, numprobs=numprobs[prob])

if __name__ == '__main__':
    app.run(debug=True)