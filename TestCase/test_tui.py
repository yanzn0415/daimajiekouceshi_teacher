from Common import Request, Assert, read_excel
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('./document/tuihuoyuanyin.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:8080/'
head = {}
list_id = 0
@allure.feature("订单模块")
class Test_login:
    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url+'admin/login',json={"username": "admin", "password": "123456"})
        resp_dict = login_resp.json()
        print(type(resp_dict))
        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head ={ 'Authorization' : tokenHead+token}
    @allure.story('查询订单退货原因')
    def test_tuile1(self):
        get_request = request.get_request(url=url + 'returnReason/list', params={'pageNum': '1', 'pageSize': '5'},
                                          headers=head)
        json = get_request.json()
        json_data= json['data']
        data_list = json_data['list']
        icon=data_list[0]
        global list_id
        list_id = icon['id']
        assertion.assert_code(get_request.status_code, 200)
        assertion.assert_in_text(json['message'], '成功')
    @allure.story("删除订单")
    def test_del_din(self):
        post_request = request.post_request(url=url + 'returnReason/delete?ids=' +str(list_id),headers=head)
        json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(json['message'],'成功')

    @allure.story("添加订单退货原因")
    @pytest.mark.parametrize('name,sort,status,msg',excel_list,ids=idsList)
    def test_add_dingdan(self,name,sort,status,msg):
        atime  = {"name": name, "sort": sort, "status": status, 'createTime': ''}
        post_request = request.post_request(url=url + 'returnReason/create', json=atime, headers=head)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['message'], msg)
