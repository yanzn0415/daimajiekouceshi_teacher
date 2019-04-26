from Common import Request, Assert, read_excel,Tools
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
# excel_list = read_excel.read_excel_list('./document/test.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:1811/'
head = {}
phone = Tools.phone_num()
pwd = Tools.random_123(3)+Tools.random_str_abc(3)
newpwd = Tools.random_123(3)+Tools.random_str_abc(3)
rePwd=pwd
userName = Tools.random_str_abc(5)+Tools.random_123(2)


@allure.feature("用户模块")
class Test_sku:
    @allure.story("注册")
    def test_zhuce(self):
        post_request = request.post_request(url=url + 'user/signup',
                                            json={"phone": phone, "pwd": pwd, "rePwd": rePwd,
                                                  "userName": userName})
        json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(json['respBase'], '成功')
    @allure.story("登录")
    def test_login(self):
        post_request = request.post_request(url=url + 'user/login', json={"pwd": pwd, "userName": userName})
        json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(json['respDesc'],'成功')
    @allure.story("修改密码")
    def test_xiugai(self):
        request_post_request = request.post_request(url=url + 'user/changepwd',
                                                    json={"newPwd": newpwd, "oldPwd": pwd, "reNewPwd": newpwd,
                                                          "userName": userName})
        request_json = request_post_request.json()
        assertion.assert_code(request_post_request.status_code,200)
        assertion.assert_in_text(request_json['respDesc'],'成功')




