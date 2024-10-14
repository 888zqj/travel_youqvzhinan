import pandas as pd
import os
import django

# 设置Django环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webServer.settings")
django.setup()

from Server01.models import Attraction

# 读取CSV文件
df = pd.read_csv("D:\全国各景点全.csv")  # 请确保路径正确

# 导入数据
for _, row in df.iterrows():
    Attraction.objects.create(
        # name=row['name'],
        # city=row['city'],
        # description=row['description']

        # city=row['city'],
        # name=row['name'],
        # location=row['location'],
        # distance = row['distance'],
        # coordinate = row['coordinate'],
        # # 坐标
        # comment_num = row['comment_num'],
        # comment_score = row['comment_score'],
        # hot_comment_score = row['hot_comment_score'],
        # picture = row['picture'],
        # free_or_not = row['free_or_not'],
        # price = row['price'],
        # pre_price = row['pre_price'],
        # # 原价
        # class_information = row['class_information'],
        # tag = row['tag'],
        # five_a_or_not = row['five_a_or_not']

        city=row['城市'],
        name=row['景点名'],
        location=row['地点'],
        distance=row['距离'],
        coordinate=row['坐标'],
        # 坐标
        comment_num=row['评论数'],
        comment_score=row['评论分'],
        hot_comment_score=row['热评分'],
        picture=row['封面'],
        free_or_not=row['是否免费'],
        price=row['价格'],
        pre_price=row['原价'],
        # 原价
        class_information=row['类别信息'],
        tag=row['标签'],
        five_a_or_not=row['是否5A']
    )