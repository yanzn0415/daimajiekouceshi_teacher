from Common import Request, Assert, read_excel
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:8080/'
head = {}
list_id = []
@allure.feature("商品模块")
class Test_login:
    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url+'admin/login',json={"username": "admin", "password": "123456"})
        resp_text = login_resp.text
        print(type(resp_text))
        resp_dict = login_resp.json()
        print(type(resp_dict))
        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head ={ 'Authorization' : tokenHead+token}
    @allure.story("获取商品分类")
    def test_get_sku(self):
        get_request = request.get_request(url=url + 'productCategory/list/0', params={'pageNum':'1','pageSize':'5'},headers=head)
        json = get_request.json()
        assertion.assert_code(get_request.status_code,200)
        assertion.assert_in_text(json['message'],'成功')
        json_data= json['data']
        data_list = json_data['list']
        icon=data_list[0]
        global list_id
        list_id = icon['id']
    @allure.story("删除商品分类")
    def test_del_sku(self):
        post_request = request.post_request(url=url + 'productCategory/delete/' +str(list_id),headers=head)
        json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(json['message'],'成功')
    @allure.story("添加商品分类")
    def test_add_sku(self):
        unit= {'description': "", 'icon': "", 'keywords': "", 'name': "周龙小骚骚", 'navStatus': 0, 'parentId': 0,
                 'productUnit': ""}
        post_request = request.post_request(url=url + 'productCategory/create', json=unit,headers=head)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(request_json['message'],'成功')
    @allure.story("添加商品分类1")
    @pytest.mark.parametrize('name',['test1','test2','test3'],ids=['第一个','第 二个','第三个'])
    def test_add_sku1(self,name):
        unit = {'description': "", 'icon': "", 'keywords': "", 'name':name , 'navStatus': 0, 'parentId': 0,
                'productUnit': ""}
        post_request = request.post_request(url=url + 'productCategory/create', json=unit, headers=head)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['message'], '成功')
















