from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type=int)
try:
    args = parser.parse_args()
    print(args)
except:
    print('wah')
for _ in range(args.time):
    print(".", end="", flush=True)
    sleep(1)
print("Done!")