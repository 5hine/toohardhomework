def add_card():
    stu_id = input("请输入您的学号：")
    name = input("请输入您的名字：")
    tel = input("请输入您的电话：")
    sex = input("请输入您的性别：")
    list1 = [stu_id, name, tel, sex]
    dict3[stu_id] = list1
    select_card(stu_id)


def del_card():
    stu_id = input("请输入您要删除的学号：")
    if stu_id in dict3:
        del dict3
        print("%s，您的名单已删除")
    else:
        print("您的学号未找到,请确认")
        del_card()


def update_card():
    stu_id = input("请输入您要修改的学号：")
    if stu_id in dict3:
        ctrl_num = int(input("请选择你需要修改的信息（1：姓名，2：电话，3：性别）"))
        update_info = input("请输入修改信息：")
        dict3[stu_id][ctrl_num] = update_info
        select_card(stu_id)
    else:
        print("您的学号未找到,请确认")
        update_card()


def select_card(stu_id=""):
    if stu_id == "":
        stu_id = input("请输入您要查询的学号：")

    if stu_id in dict3:
        for (i1, i2) in zip(["学号:", "姓名:", "电话:", "性别:"], dict3[stu_id]):
            i1 += i2
            print(i1, end="    ")
        print()
    else:
        print("您的学号未找到,请确认")
        select_card()


def exit_sys():
    print("感谢您的使用，再见！")
    exit()


def control():
    c_num = input("请输入您的选择：")
    dict2 = {
        "1": add_card,
        "2": del_card,
        "3": update_card,
        "4": select_card,
        "5": exit_sys,
    }
    if c_num in dict2:
        return dict2[c_num]
    else:
        print("您输入的选择有误，请重新输入")
        control()


dict3 = {"0000": ["0000", "administrator", "12345", "male"]}
while True:
    print("欢迎进入名片管理器")
    print("1. 添加名单")
    print("2. 删除名单")
    print("3. 修改名单")
    print("4. 查询名单")
    print("5. 退出系统")
    func = control()
    func()
