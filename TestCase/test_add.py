from Common import Request, Assert, read_excel
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('./document/youhui.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:8080/'
head = {}
list_id = 0
@allure.feature("营销模块")
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
    @allure.story('查询优惠卷')
    def test_sel(self):
        global head
        get_request = request.get_request(url=url + 'coupon/list/', params={'pageNum': '1', 'pageSize': '10'},headers=head)
        json = get_request.json()
        data = json['data']
        list = data['list']
        alist = list[0]
        global list_id
        list_id= alist['id']
        assertion.assert_code(get_request.status_code,200)
        assertion.assert_in_text(json['message'],'成功')
    @allure.story('删除优惠券')
    def test_del_yhq(self):
        del_resp = request.post_request(url=url + 'coupon/delete/' + str(list_id), headers=head)
        resp_json = del_resp.json()
        assertion.assert_code(del_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
    @allure.story("添加优惠卷")
    @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg',excel_list,ids=idsList)
    def test_add_sku1(self,name,amount,minPoint,publishCount,msg):
        alist = {"type":0,"name":name,"platform":0,"amount":amount,"perLimit":1,"minPoint":minPoint,"startTime":'',
                 "endTime":'',"useType":0,"note":'',"publishCount":publishCount,"productRelationList":[],
                 "productCategoryRelationList":[]}
        request_post_request = request.post_request(url=url + 'coupon/create', json=alist,headers=head)
        json = request_post_request.json()
        assertion.assert_code(request_post_request.status_code, 200)
        assertion.assert_in_text(json['message'],msg )


