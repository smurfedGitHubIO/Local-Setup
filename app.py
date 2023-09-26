from flask import Flask, render_template, request
import subprocess
import time
numprobs = {'A': 2, 'B': 3, 'C': 3}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    prob = request.form.get('choice')
    # return f'{prob}'
    subprocess.run(["g++.exe", "-std=c++17", "sample.cpp", "-o", "sample"], encoding="utf-8")
    correct = 0
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
        print('\n'.join(outputs)+'\n')
        print(' '.join(inputs))
        print(test_out.stdout)
        correct += (test_out.stdout == '\n'.join(outputs)+'\n')

    return f'Correct Answers: {correct}/{numprobs[prob]}'

if __name__ == '__main__':
    app.run(debug=True)