import time
# 引入时间（防止报告被覆盖）
now = time.strftime('%Y-%m-%d_%H_%M_%S') #获取当前时间
file_path = 'test'+now+'.html'
print(now)


# 断言 测试用例的判断
# assertEqual(a,b)  a==b
# assertNotEqual(a,b)  a!=b
# assertTrue(x)  bool(x) is true
# assertFalse(x)  bool(x) is false
# assertIs(a,b)  a is b
# assertIsNot(a,b)  a is not b
# assertIsNone(x)  x is None
# assertIsNotNone(x)  x is not  None
# assertIn(a,b)  a in b                # 成员运算符
# assertNotIn(a,b)  a not in b
# assertIsInstance(a,b)  isinstance(a,b)
# assertNotIsInstance(a,b)  not isinstance(a,b)