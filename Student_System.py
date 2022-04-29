student_list = {}
import pandas as pd
student_dict = {
        '姓名': [],
        '学号': [],
        '性别': [],
        '寝室号': [],
        '年龄': [],
        '班级': [],
        '手机号': []
    }

def menu():
    print("\n"
          """学生信息系统
        1.添加学生信息    2.删除学生信息
        3.修改学生信息    4.显示学生信息
        5.退出       
        请输入要操作的数字：""")

def add_student():
    id = input("请输入学生的学号：")
    name = input("请输入学生的姓名：")
    sex = input("请输入学生的性别：")
    age = input("请输入学生的年龄：")
    phone = input("请输入学生的联系电话：")
    classroom = input("请输入学生的班级：")
    room = input("请输入学生的寝室号")

    student_dict['姓名'].append(name)
    student_dict['年龄'].append(age)
    student_dict['学号'].append(id)
    student_dict['性别'].append(sex)
    student_dict['寝室号'].append(room)
    student_dict['班级'].append(classroom)
    student_dict['手机号'].append(phone)
    pd.DataFrame(student_dict).to_excel(r'C:\Users\Administrator\Desktop\学生信息表.xlsx', index=False)

    student_info = {'name': name, 'sex': sex,'age':age, 'phone': phone,'classroom':classroom,'room':room}
    student_list[id] = student_info
    print("添加成功")
def delete_studentIno():
    id = input("请输入要删除的学生学号：")
    if id not in student_list.keys():
        print("未找到该学生")
        delete_studentIno()
    student_list.pop(id)
    print("您删除了该学生信息")
def update_student():
    id = input("请输入要修改的学生学号：")
    if id not in student_list.keys():
        print("未找到该学生！")
        return
    student_info = student_list[id]
    print("你当前修改学生的学号%s 姓名%s 性别%s 手机号%s 年龄%s 寝室号%s 班级%s"%(id,student_list[id]['name'],student_list[id]['sex'],student_list[id]['phone'],student_list[id]['age'],student_list[id]['room'],student_list[id]['classroom']))
    print("请输入要修改的内容编号")
    print("1:姓名")
    print("2:性别")
    print("3:手机号")
    print("4:年龄")
    print("5:寝室号")
    print("6:班级")
    print("7:全部信息")
    edit_news = input("请输入编号：")
    if edit_news == "1":
        newname = input("请输入更改后的学生姓名：")
        student_list[id]['name'] = newname
    elif edit_news == "2":
        newsex = input("请输入更改后的学生性别：")
        student_list[id]['sex'] = newsex
    elif edit_news == "3":
        newphone = input("请输入更改后的学生联系方式：")
        student_list[id]['phone'] = newphone
    elif edit_news == "4":
        newage = input("请输入更改后的学生年龄：")
        student_list[id]['age'] = newage
    elif edit_news == "5":
        newroom = input("请输入更改后学生的寝室号：")
        student_list[id]['room'] = newroom
    elif edit_news == "6":
        newclassroom = input("请输入更改后学生的班级号：")
        student_list[id]['classroom'] = newclassroom
    elif edit_news == "7":
        newname = input("请输入更改后的学生姓名：")
        student_list[id]['name'] = newname
        newsex = input("请输入更改后的学生性别：")
        student_list[id]['sex'] = newsex
        newphone = input("请输入更改后的学生联系方式：")
        student_list[id]['phone'] = newphone
        newage = input("请输入更改后的学生年龄：")
        student_list[id]['age'] = newage
        newroom = input("请输入更改后学生的寝室号：")
        student_list[id]['room'] = newroom
        newclassroom = input("请输入更改后学生的班级号：")
        student_list[id]['classroom'] = newclassroom

        print("修改成功")
    else:
        print("输入有误")

def show():
    for id, value in student_list.items():
        print("学号：%s 姓名：%s 性别：%s 手机号：%s 年龄：%s 寝室号：%s 班级：%s " % (id, value['name'], value['sex'], value['phone'], value['age'],value['room'],value['classroom']))
def main():
    while True:
        menu()
        user_input = input("请输入你要选择操作的数字：")
        if user_input == "1":
            add_student()
        elif user_input == "2":
            delete_studentIno()
        elif user_input == "3":
            update_student()
        elif user_input == "4":
            show()
        elif user_input == "5":
            quit_menu = input("您确认要退出系统吗？(yes or no):")
            if quit_menu == 'yes':
                break
        else:
            print("你的输入有错误")
main()
