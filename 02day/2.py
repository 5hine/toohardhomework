str1 = "hello worldh"
str2 = []    # 记录 匹配过的字母
str3 = str1[::-1]
for i in str1:
    count = 1
    a = str1.index(i)
    if i in str2 or i == " ":
        continue
    for j in str3[:len(str1)-1-a]:  # 不取最后一个
        if j == i:
            count += 1
            str2.append(j)
    print("%s:%d" % (i, count))
print("%s"%str1)
