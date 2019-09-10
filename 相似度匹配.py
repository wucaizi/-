import difflib

#判断相似度的方法，用到了difflib库
def get_equal_rate_1(str1, str2):
   return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

#执行方法进行验证


if __name__ == '__main__':
   a = '上海我爱你'
   b = '上海市我恨你'
   print(get_equal_rate_1(a, b))