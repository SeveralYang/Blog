from django.db import models


class User(models.Model):
    """
    用户类
    name            : 用户昵称 用于显示
    phone_number    : 用户注册所用手机号码
    avatar          : 用户头像 url
    mail            : 用户注册所用邮箱 
    """
    
    # id  自动生成
    name = models.CharField(verbose_name="nick name",max_length=32, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)
    mail = models.CharField(max_length=64,unique=True)
    avatar = models.CharField(max_length=256)  # url 头像  需要设置一个默认头像



class Title(models.Model):
    """
    用户头衔类,每一条数据代表一种title
        用于展示用于所具有的标识
        用核对用户是否具有某种权限
    """
    text = models.CharField(max_length=256)
    icon = models.CharField(max_length=256,default=None)

class User_title(models.Model):
    """
    关系类
    哪些用户具有哪些title
    """
    user_id = models.IntegerField()
    title_id = models.IntegerField()