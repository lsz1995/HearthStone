import requests

def get_proxy():


    return requests.get("http://119.23.72.247:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://http://119.23.72.247/delete/?proxy={}".format(proxy))

# your spider code

def getHtml(url,headers,cookies):
    # ....
    retry_count = 5
    proxy = get_proxy()

    while retry_count > 0:
        try:
            html = requests.get(url, headers=headers, cookies=cookies,proxies={"http": "http://{}".format(proxy)}).text  #
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None
if __name__ == '__main__':

    proxy = get_proxy()
    print(proxy)