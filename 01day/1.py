while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "shine" and password == "123456":
        print("欢迎进入%s的世界" % username)
        break
    else:
        print("您的用户名或密码有误，请重新输入：")
