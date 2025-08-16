s = "hello Python"
count = {}

for i in s:
    if count.get(i) is None:
        count.update({i:1})
    else:
        j = count.get(i)
        j+=1
        count.update({i:j})
print(count)