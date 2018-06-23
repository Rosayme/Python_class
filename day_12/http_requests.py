import requests

class HttpRequests:
    def __init__(self,url,param=None):
        self.url = url
        self.param = param

    def get_post_request(self, method):
        try:
            if method.upper() == 'GET':
                response = requests.get(self.url, self.param)
            elif method.upper() == "POST":
                response = requests.post(self.url, self.param)
            else:
                print("请求的方法不存在")
            return response.json()
        except Exception as e:
            print("请求失败，出现的错误是%s" % e)
            #raise e

if __name__ == '__main__':
    url = "http://v.juhe.cn/laohuangli/d"
    param = {'date': '2018-06-23', 'key': '863a9a944d6a397a16f74c4202127b70'}
    method = 'get'
    t = HttpRequests(url, param)
    print(t.get_post_request(method))

