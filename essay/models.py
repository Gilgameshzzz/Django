from django.db import models


# Create your models here.
# 博客类(博客标题，博客内容， 发表时间，标签，分类)
class Blog(models.Model):
	title = models.CharField('标题', max_length=200)
	author = models.CharField('作者', max_length=30)
	content = models.TextField('博客内容')
	create_time = models.DateTimeField('发布时间', auto_now_add=True)


# 评论类（评论人，评论时间，评论内容，博客（评论人为账号，评论人邮箱为密码））
class Comment(models.Model):
	blog = models.ForeignKey(Blog, verbose_name='博客')
	name = models.CharField('昵称', max_length=20)
	content = models.CharField('评论内容', max_length=300)
	created = models.DateTimeField('发布时间', auto_now_add=True)


# 分类 类
class Classify(models.Model):
	name = models.CharField('分类名称', max_length=30)


# 标签类
class Tag(models.Model):
	name = models.CharField('标签名称', max_length=20)


# 后台账号
class Users(models.Model):
	username = models.CharField(
		max_length=10,
		unique=True,
		verbose_name='姓名')
	password = models.CharField(max_length=255, verbose_name='密码')
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建是时间')
	operate_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

	class Meta:
		db_table = 'users'


class UserTicket(models.Model):
	user = models.ForeignKey(Users)
	ticket = models.CharField(max_length=30)
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建是时间')

	class Meta:
		db_table = 'user_ticekt'