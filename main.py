from DrissionPage import ChromiumPage

page1 = ChromiumPage()
page1.get('https://xk.nju.edu.cn/')
login_name = input("你的学号：")
login_pwd = input("你的密码：")
vcode = input("输入你看到的验证码：")

page1.ele('#loginName').input(login_name)
page1.ele('#loginPwd').input(login_pwd)
page1.ele('#verifyCode').input(vcode)

page1.ele('#studentLoginBtn').click()
page1.ele("确认").click()
page1.ele('#courseBtn').click()
page1.eles('.tab-first')[-1].click()

while True:
    page1.refresh()
    wanted_courses = page1.eles('.course-tr ')
    if not wanted_courses:
        print("收藏列表为空，请重新检查")
        break
    for wanted_course in wanted_courses:
        print(wanted_course('.kcmc course-cell').text, wanted_course('.jsmc course-cell').text, wanted_course('.yxrs course-cell').text)
        statue = wanted_course('.yxrs course-cell').text
        if '已满' in statue:
            print("已满，尝试刷新")
        else:
            while True:
                wanted_course.child(8).ele('选择').click()
                page1.ele('.cv-sure cvBtnFlag').wait.displayed()
                page1.ele('.cv-sure cvBtnFlag').click()
                dialog = page1.ele('#cvDialog').child(2).child(1)
                if dialog.ele('失败'):
                    dialog.next().click()
                    print("选课失败")
                    break
                else:
                    dialog.next().click()
                    print(f"{wanted_course.texts()}选课成功") 
                    break

    
