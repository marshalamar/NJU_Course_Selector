from DrissionPage import ChromiumPage

class Utils:
    @staticmethod
    def click_confirm(page):
        if page.ele('.jqx-rc-all jqx-window jqx-popup jqx-widget jqx-widget-content'):
            page.ele("确认").click()

    @staticmethod
    def handle_course_selection_result(page, course, result):
        page.ele('.cv-sure cvBtnFlag').wait.displayed()
        page.ele('.cv-sure cvBtnFlag').click()
        dialog = page.ele('#cvDialog').child(2).child(1)
        if result == "失败":
            dialog.next().click()
            print("选课失败")
        else:
            dialog.next().click()
            print(f"{course.texts()}选课成功")

class LoginModule:
    def __init__(self, page):
        self.page = page

    def login(self, username, password, captcha):
        self.page.ele('#loginName').input(username)
        self.page.ele('#loginPwd').input(password)
        self.page.ele('#verifyCode').input(captcha)
        self.page.ele('#studentLoginBtn').click()

        Utils.click_confirm(self.page)

class CourseSelectionModule:
    def __init__(self, page):
        self.page = page

    def select_courses(self):
        self.page.ele('#courseBtn').click()
        self.page.eles('.tab-first')[-1].click()

        while True:
            self.page.refresh()
            wanted_courses = self.page.eles('.course-tr ')
            if not wanted_courses:
                print("收藏列表为空，请重新检查")
                break

            for wanted_course in wanted_courses:
                print(wanted_course('.kcmc course-cell').text, wanted_course('.jsmc course-cell').text, wanted_course('.yxrs course-cell').text)
                statue = wanted_course('.yxrs course-cell').text
                if '已满' in statue:
                    print("已满，尝试刷新")
                else:
                    self.select_course(wanted_course)

    def select_course(self, course):
        while True:
            course.child(8).ele('选择').click(by_js=True)
            result = self.get_course_selection_result(course)
            Utils.handle_course_selection_result(self.page, course, result)
            break

    def get_course_selection_result(self, course):
        dialog = self.page.ele('#cvDialog').child(2).child(1)
        if "失败" in dialog.texts():
            return "失败"
        else:
            return "成功"

if __name__ == "__main__":
    page = ChromiumPage()
    page.get('https://xk.nju.edu.cn/')
    login_name = input("你的学号：")
    login_pwd = input("你的密码：")
    vcode = input("输入你看到的验证码：")

    login_module = LoginModule(page)
    login_module.login(login_name, login_pwd, vcode)

    course_selection_module = CourseSelectionModule(page)
    course_selection_module.select_courses()
