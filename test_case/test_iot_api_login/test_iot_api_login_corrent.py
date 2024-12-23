import json
import  requests
from config  import apiconfig
import allure
@allure.title('通过ID获取名字')
def test_api_getidbyname():
    # url='http://192.168.20.212:5500/api/system/tenant/get-id-by-name?name=CDB-IOT'
    data='CDB-IOT'
    url=apiconfig.host+apiconfig.getidbynameurl+"?name={name}".format(name=data)
    header =apiconfig.header
    r=requests.get(headers=eval(header),url=url).json()
    result=r['data']
    return result
@allure.description('获取到tenanid')
def test_api_tenantId():
    url=apiconfig.host+apiconfig.tenantIdurl+"?tenantId={tenantId}".format(tenantId=test_api_getidbyname())
    header =json.loads(apiconfig.header)
    Tenantid=test_api_getidbyname()
    new_dict={"Authorization":"Bearer 34d96bd3c45e4b1286af25c0ce6935f1","Tenant-Id":"{}".format(Tenantid)}
    new_header=header.update(new_dict)
    r = requests.get(headers=eval(str(header)), url=url)
    print(r.text)
def test_api_usernametendid():
    # url='http://192.168.20.212:5500/api/system/auth/login-failures?username=CDBAdmin&tenantId=2'
    Tenantid1 = test_api_getidbyname()
    url=apiconfig.host+apiconfig.usernametendiD+'?username={username}&tenantId={tenantId}'.format(username='CDBAdmin',tenantId=Tenantid1)
    header = json.loads(apiconfig.header)
    Tenantid = test_api_getidbyname()
    new_dict = {"Authorization": "Bearer 34d96bd3c45e4b1286af25c0ce6935f1", "Tenant-Id": "{}".format(Tenantid)}
    new_header = header.update(new_dict)
    r = requests.get(headers=eval(str(header)), url=url)
    print(r.text)
def test_api_login():
    url=apiconfig.host+apiconfig.userlogiapi
    header = json.loads(apiconfig.header)
    Tenantid = test_api_getidbyname()
    new_dict = {"Authorization": "Bearer 34d96bd3c45e4b1286af25c0ce6935f1", "Tenant-Id": "{}".format(Tenantid)}
    new_header = header.update(new_dict)
    data='{"password":"CDBAdmin.123","username":"CDBAdmin"}'
    r=requests.post(headers=eval(str(header)),url=url,data=data)
    print(r.text)
if __name__=="__main__":
   op=test_api_getidbyname()
   print(op)

