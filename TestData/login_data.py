# 正确的用户名和密码
noraml_login = {'phone': '18684720553',
                'pwd': 'python'}

# 不输入手机号，输入位数不正确的手机号，不输入密码
wrong_login = [{'phone': '', 'pwd': 'python', 'expected': '请输入手机号'},
               {'phone': '1868472055', 'pwd': 'python', 'expected': '请输入正确的手机号'},
               {'phone': '186847205556', 'pwd': 'python', 'expected': '请输入正确的手机号'},
               {'phone': '18684720553', 'pwd': '', 'expected': '请输入密码'}]

wrong_pwd_user = [{'phone': '18684720553', 'pwd': 'python123', 'expected': '账户或密码错误'},
                  {'phone': '18684720552', 'pwd': 'python123', 'expected': '此账户没有授权，请联系管理员'}]
