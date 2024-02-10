import os
import sys

HOME = os.environ["HOME"]
manifest_path=os.path.join(HOME,'python-for-coding-test/school/sample.txt')

sys.stdin = open(manifest_path,'r')

T = int(input())

for test_case in range(1, T + 1):
    line=list(map(int,input().split()))
    
    print(line)
    for n in line :
        print(n)