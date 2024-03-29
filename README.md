# ETAIDFS:新兴技术产业发展预测软件

# 摘要

**代码中带有非常详细的注释。(很强迫）O(∩_∩)O~~)**

前端采用bootstrap样式 + jquery控制

* 封装了ajax请求
* jquery动态生成页面元素

后端采用flask框架处理调用逻辑。

数据库为SQL Server。

# 目录结构
```
.
├── templates                                           前端页面html代码
|   ├── ExpertInformationManage.html                    ├── 专家信息管理页
|   ├── homepage_Adminastrator.html                     ├── 管理员主页
|   ├── homepage_Expert.html                            ├── 专家主页
|   ├── homepage_normalUser.html                        ├── 普通用户主页
|   ├── login.html                                      ├── 登录页面
|   ├── NewPage.html                                    ├── 新空白页，用来弹出其他内容
|   ├── register.html                                   ├── 注册页面
|   └── upload.html                                     └── 文件上传页面
|   
├── static                                              static（固定结构）                                       
│   ├── js                                              ├── javascript代码
|   |   ├── MainFunction                                |   ├── 主要js函数    
|   |   |   |── BreadNav.js                             |   |   |── 面包屑导航条逻辑
|   |   |   |── CommonFunction.js                       |   |   |── 通用函数,封装ajax请求
|   |   |   |── CountryInfo.js                          |   |   |── 国家信息获取
|   |   |   |── ExpertInformationManage.js              |   |   |── 专家信息管理
|   |   |   |── ExpertJudge.js                          |   |   |── 专家对行业进行判断
|   |   |   |── GetIntroduction.js                      |   |   |── 简介获取
|   |   |   |── index.js                                |   |   |── 页面初始化
|   |   |   |── login.js                                |   |   |── 登录函数
|   |   |   |── register.js                             |   |   |── 注册函数
|   |   |   |── Reset.js                                |   |   |── 页面重置
|   |   |   └── TotalInfo.js                            |   |   └── 一次性获取全部信息
|   |   └── ...                                         |   └── jquery+boostrap源码
|   |── css                                             |── css样式
|   |   |── signin.js                                   |   |── 登录                 
|   |   |── register.js                                 |   |── 注册
|   |   |── navbar.js                                   |   |── 导航条逻辑
|   |   |── dashboard.js                                |   |── 面板逻辑
|   |   └── ...                                         |   └── boostrap样式
|   └── font                                            └── 个性化字体
|
├── service                                             服务端代码
|   ├── config.py                                       ├── 全局配置
|   ├── Consts.py                                       ├── 常量配置
|   ├── DBsession.py                                    ├── 数据库session（SQL Server）
|   ├── ExpertJudge_InformationManager.py               ├── 专家标注与信息管理
|   ├── GetCommonData.py                                ├── 获取通用数据
|   ├── LoginAndRegister.py                             ├── 登录及注册
|   ├── Main.py                                         ├── 启动入口
|   ├── model.py                                        ├── 数据库定式
|   ├── module.py                                       ├── 模块封装  
|   ├── ShowGraphData.py                                ├── 展示图表数据
|   └── UploadFile.py                                   └── 上传文件
|                                                       |
└── documents                                           └── 文档
```