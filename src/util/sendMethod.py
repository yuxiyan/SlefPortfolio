import requests
import json


class SendMethod:

    def send_get(self, url, params, cookies):

        response = requests.get(url, params=params, headers={"user-Agent": "Xueqiu Android 12.6.1"},cookies=cookies).json()

        return response

    def send_post(self, url, data, cookies):

        response = requests.post(url, data=data, cookies=cookies, headers={"user-Agent": "Xueqiu Android 12.6.1"} ).json()
        return response

    def send_method(self, url, cookies, params, method):

        if method == 'GET':
            response = self.send_get(url, params, cookies)
        else:
            response = self.send_post(url, params, cookies)

        return response

    def get_token(self):

        url = r"https://api.xueqiu.com/provider/oauth/token"

        data = {"client_id": "JtXbaMn7eP",
                "client_secret": "txsDfr9FphRSPov5oQou74",
                "grant_type": "password",
                "telephone": "18222703032",
                "areacode": "86",
                "password": "yuxiyan12"
                }
        headers = {"user-Agent": "Xueqiu Android 12.6.1",
                   "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
                   "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   }

        r = requests.post(url, headers=headers, data=data)
        result = json.loads(r.text)
        access_token = result['access_token']
        uid = str(result["uid"])
        cookies = {'xq_a_token': access_token, 'u': uid}

        return cookies
