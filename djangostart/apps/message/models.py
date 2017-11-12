from django.db import models

# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name="用户名") # verbose 类似于注释
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.CharField(max_length=500, verbose_name="留言信息")

    class Meta: # 元数据类型，「任何不适字段的数据」
        verbose_name = "用户留言信息"
