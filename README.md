### Django后端

#### 此项目是该项目配套后端


#### 需要安装依赖

``` bash
pip install Django
pip install pyjwt==2.4.0  
pip install pytz==2023.3.post1  
pip install pillow==9.4.0  
pip install pathlib==1.0.1  
pip install python-dotenv==0.21.0  
pip install djangorestframework==3.15.2  
pip install requests==2.31.0  
pip install pandas==2.0.3
```

#### 使用

需要在settings中修改数据库的配置信息

配置你自己的端口号等信息

 ``` bash
    python manage.py makemigrations
    python manage.py migrate
```

#### 功能
首页推荐

生成旅游攻略

用户登录注册

发帖，点赞，评论，关注，帖子详情

用户主页 ，更新个人信息，帖子管理



