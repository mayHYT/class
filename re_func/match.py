import  re

'''
matchobj = re.match("abc", "abcdefgabc")
print(matchobj)


safestr = "全能神 全能神 全能神 全能神"
safestrlast=re.subn("全能神","宇宙真理", safestr)

print(type(safestrlast))
print(safestrlast)
print(safestrlast[0])
print(safestrlast[1])

# .  除了换行之外任何字符  \n
# \  转义字符 \r \t
#  \d  数字
# \D   非数字
# \s  空白字符
# \S  非空白字符
# \w  单词字符 大小写字母数字
# \W  非单词字符
regex=re.compile(r"\W", re.IGNORECASE)
print(regex.match("+"))


print(re.match(r"^(\d+)(0*)$", "8848000").groups())#正则默认贪婪
print(re.match(r"^(\d+?)(0*)$", "8848000").groups())#加上？为非贪婪

'''

'''
mystr1="<title>helloworld</title>"
res=re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", mystr1)
print(res)

res1=re.match("<([a-zA-Z]*)>\w*</\\1>", mystr1)
print(res1)
'''

mystr="<title>百度一下 你就知道</title>"
