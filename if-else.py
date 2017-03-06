number = input()
if len(number) > 3:
    print('you input a string length more than 3')
else:
    print('you input a string length small than 3')

# if elif else

# if 不仅可以判断boolean类型的值，数字，字符串，list都能判断
# 只要不为空就为True， 为空就为False
arrays = [1, 2, 3]
if arrays:
    print('arrays is not empty')