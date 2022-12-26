def index(string, sub):
    start = 0
    end = 0
    while start < len(string):
        if string[start+end] != sub[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(sub):
            return 0
    return -1

string = input()
output = ""
for i in string:
    if index(output, i) == -1:
        output = output+i
    else:
        output = output.replace(i, "")
print(output[0])



