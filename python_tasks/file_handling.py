import os

fp = open('sales.txt', 'w')
fp.write("Hi This is Mckiney from glasscow")

print(os.listdir())
fp.close()

#
with open(r'C:\python project\python_tasks\sales.txt', 'w') as fp:
    fp.write('This is first line')
    pass
