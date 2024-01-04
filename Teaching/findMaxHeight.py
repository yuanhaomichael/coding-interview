def sort_height(arr):
  tallest_student = 0
  max_height = arr[0]

  for i in range(len(arr)):
    # step A: 衡量眼前这个同学的身高
    current_student = arr[i]

    # step B: 如果现在这个同学的身高比max_height大的话，让tallest_student=现在同学的名字
    if current_student > max_height:
      tallest_student = i
    
    # step C: 更新max_height
    max_height = max(max_height, current_student)

  return ["tallest student number:", tallest_student, "his or her height", max_height]


## testing ## 
test1 = [169, 155, 170, 172, 180, 134, 155, 123, 172, 158]
test2 = [190, 100, 120]
test3 = [100, 199]

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("testnum", help="which test")
args = parser.parse_args()

result = sort_height(eval(args.testnum))
print(result)