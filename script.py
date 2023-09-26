import subprocess
import time

numprobs = {'A': 2, 'B': 3, 'C': 5}

prob = 'A'
start_time = time.time()
sample_out = subprocess.run(["g++.exe", "-std=c++17", "./tests/solns/A.cpp", "-o", "A"], capture_output=True, encoding="utf-8")
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
    test_out = subprocess.run([f'{prob}'], capture_output=True, input=' '.join(inputs), encoding="utf-8")

    correct += (test_out.stdout == '\n'.join(outputs)+'\n')
end_time = time.time()
print(correct == numprobs[prob])
print(end_time - start_time)
