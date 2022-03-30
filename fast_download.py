# 快速下载文件组件
import os
import requests

def main():
    url = input("请输入错误的URL: ")
    join_url = "https://cdn-1258575882.cos.ap-guangzhou.myqcloud.com/gameList/wuZiQi/hhfhdf_1.0.37/web-mobile/" + url
    file = requests.get(join_url)
    os.makedirs(os.path.dirname(os.path.abspath(url)))
    with open(os.path.abspath(url), "wb") as f:
        f.write(file.content)
    print("开始提交代码")
    os.system("git pull up master")
    os.system("git add .")
    os.system("git commit -m \"Enjoy~\"")
    os.system("git push")

if __name__ == "__main__":
    main()
