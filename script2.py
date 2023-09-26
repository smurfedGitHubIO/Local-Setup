import subprocess
import time

start_time = time.time()
sample_out = subprocess.run(["g++.exe", "-std=c++17", "./tests/solns/A.cpp", "-o", "A"], capture_output=True, encoding="utf-8")
lst = []
with open('./tests/input/A/input_1.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lst.append(line.strip())
output = []
with open('./tests/output/A/output_1.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        output.append(line.strip())
test1_out = subprocess.run(["A"], capture_output=True, input=' '.join(lst), encoding="utf-8")
end_time = time.time()
print(test1_out.stdout == '\n'.join(output)+'\n')
print(end_time - start_time)
