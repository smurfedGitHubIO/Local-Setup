import subprocess

sample_out = subprocess.run(["g++.exe", "-std=c++17", "sample.cpp", "-o", "test1"], capture_output=True, encoding="utf-8")
test1_out = subprocess.run(["test1"], capture_output=True, input="1 2 c", encoding="utf-8")
print(test1_out.stdout)
