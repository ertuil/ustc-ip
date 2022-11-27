import requests
import json
import time

global_ip_url = "http://myip.ipip.net"
ustc_ip_url = "https://ip.ustc.edu.cn/myip.php"

s = requests.Session()


def get_ustc_ip(s: requests.Session):
    r = s.get(ustc_ip_url)
    t = r.text
    j = json.loads(t)
    return j["myip"]


def get_global_ip(s: requests.Session):
    r = s.get(global_ip_url)
    t = r.text
    sub = t.split(" ")
    return sub[1][3:]


def main():
    try:
        global_ip = get_global_ip(s)
    except Exception:
        global_ip = "failed"

    try:
        ustc_ip = get_ustc_ip(s)
    except Exception:
        ustc_ip = "failed"

    localtime = time.asctime(time.localtime(time.time()))
    msg = f"[{localtime}] global ip: {global_ip}, ustc ip: {ustc_ip}"
    requests.post("https://tg.ltcp98.top", data={"secret": "a2234129", "message": msg})


main()