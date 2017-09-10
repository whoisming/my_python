import requests
import  time

def ming_http_test_status(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "网络异常"

if __name__ == '__main__':
    ming_url = 'http://www.baidu.com'
    start_time = time.time()
    for i in range(0,100):
        ming_http_test_status(ming_url)
        print("第{}爬取".format(i))
    run_time = time.time()
    print (run_time-start_time)
