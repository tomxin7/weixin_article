![image.png](https://cdn.nlark.com/yuque/0/2022/png/209614/1662132218207-2d4506e5-208d-4282-9fa8-0671feb3ba94.png#clientId=ube99fa9d-0b5e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=245&id=u1dcd86e0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=294&originWidth=726&originalType=binary&ratio=1&rotation=0&showTitle=false&size=131643&status=done&style=none&taskId=u113ed595-95a7-4e47-a992-d92dc6c5019&title=&width=604.9999759594609)
# 前言
> 公司周年庆，行政的同事想让我帮个忙，把微信公众号的文章都导在一个文档里面，方便统计和检索。在网上找了一圈，大部分工具处于不可用状态，或者需要收费，于是花了一个多小时写了Python脚本，125行代码，轻松导出所有文章。

# 环境要求
Python：3.6+
# 导出方式
**1、导出准备**
需要登录公众号后台，遍历发表记录列表，获取到微信临时阅读地址，抓取详情页内容。
![360截图20220902230215905.png](https://cdn.nlark.com/yuque/0/2022/png/209614/1662130946772-b15faf6d-f97b-4f9b-be23-61eb45c0a1d6.png#clientId=uf31251d5-d560-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=u6dfc4002&margin=%5Bobject%20Object%5D&name=360%E6%88%AA%E5%9B%BE20220902230215905.png&originHeight=901&originWidth=1921&originalType=binary&ratio=1&rotation=0&showTitle=false&size=148185&status=done&style=none&taskId=u39e1af28-827d-4c79-8dbd-6623d95326e&title=)

**2、导出过程**
![360截图20220902225937289.png](https://cdn.nlark.com/yuque/0/2022/png/209614/1662130880358-06a9de13-4daf-49b5-a406-3d2eff35cd4f.png#clientId=uf31251d5-d560-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=ucc68a9bb&margin=%5Bobject%20Object%5D&name=360%E6%88%AA%E5%9B%BE20220902225937289.png&originHeight=1048&originWidth=1929&originalType=binary&ratio=1&rotation=0&showTitle=false&size=227958&status=done&style=none&taskId=uf2424e7e-7829-41a7-a340-f15b4b67c12&title=)
任务完成后会在根目录下生成一个html文件，直接使用浏览器打开即可
![image.png](https://cdn.nlark.com/yuque/0/2022/png/209614/1662131051596-3781a307-5020-4b50-adaa-a198750e5c97.png#clientId=uf31251d5-d560-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=75&id=WsaxQ&margin=%5Bobject%20Object%5D&name=image.png&originHeight=90&originWidth=357&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4342&status=done&style=none&taskId=u6536f774-ceda-4a2e-8e9d-e5bd2d66d9f&title=&width=297.4999881784126)

**3、导出效果**
可以直接用浏览器打开，也可以导入入word文档或者数据库中进行数据的检索
![360截图20220902230757751.png](https://cdn.nlark.com/yuque/0/2022/png/209614/1662131312525-02ec1558-e73e-464b-84d0-ed0a604bbc73.png#clientId=uc7046a69-8699-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=udec60911&margin=%5Bobject%20Object%5D&name=360%E6%88%AA%E5%9B%BE20220902230757751.png&originHeight=1025&originWidth=1908&originalType=binary&ratio=1&rotation=0&showTitle=false&size=137302&status=done&style=none&taskId=u27ecbb24-acbf-4c4d-a458-6ed87e0ebba&title=)
