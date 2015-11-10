# encoding: utf-8
from django import forms

class BookForm(forms.Form):
    ISBN=forms.CharField(max_length=100,label='ISBN')
    Title=forms.CharField(max_length=100,label=u'图书名称')
    Author=forms.CharField(max_length=100,label=u'作者')
    Publisher=forms.CharField(max_length=100,label=u'出版社')
    PublishDate=forms.DateField(label=u'出版日期')
    Price=forms.IntegerField(label=u'售价')
    
class AuthorForm(forms.Form):
    Name=forms.CharField(max_length=100,label=u'姓名')
    Age=forms.CharField(max_length=100,label=u'年龄')
    Country=forms.CharField(max_length=100,label=u'国籍')
    
class UpdateForm(forms.Form):
    Title=forms.CharField(max_length=100,label=u'图书名称')
    Author=forms.CharField(max_length=100,label=u'作者')
    Publisher=forms.CharField(max_length=100,label=u'出版社')
    PublishDate=forms.DateField(label=u'出版日期')
    Price=forms.IntegerField(label=u'售价')