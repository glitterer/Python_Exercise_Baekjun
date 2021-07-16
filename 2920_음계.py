import sys
num_original = list(map(int, (sys.stdin.readline()).split()))  # 잘 알아두자!!!! sys로 여러 개의 값을 입력받는 방법이다.
# print(num)
import copy
numSortAsc = copy.copy(num_original)
numSortDesc = copy.copy(num_original)
numSortAsc.sort()
numSortDesc.sort(reverse=True)
if num_original == numSortAsc:
    print("ascending")
elif num_original == numSortDesc:
    print("descending")
else:
    print("mixed")
