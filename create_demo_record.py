#!/usr/bin/python
# -*- coding:utf-8 -*-

from queryset.wsgi import *
from video.models import site, media

class QuerySetOperation():
    
#1. 创建对象(4种方法)

    #1.1
    def create_site1(self):
        site.objects.create(site_name='高清mp4吧', site_code='mp4ba', site_id=1)
        
    #1.2
    def create_site2(self):
        new_site = site(site_name='海盗窝', site_code='hdwo', site_id=2)
        new_site.save()
        
    #1.3
    def create_site3(self):
        new_site = site()
        new_site.site_name = '优酷'
        new_site.site_code = 'youku'
        new_site.site_id = 3
        new_site.save()
        
    #1.4 首先尝试获取，不存在就创建，可以防止重复(返回值(object, True/False))
    def create_site4(self):
        site.objects.get_or_create(site_name='乐视', site_code='letv', site_id=4)
        
#2. 获取对象(过滤)
    #2.1 查询所有
    def get_all(self):
        all_site = site.objects.all()
        #QuerySet是可以迭代的
        for s in all_site:
            print 'the site_id %d is %s' % (s.site_id, s.site_name)
    
    #2.2 切片查询(不支持负索引)
    def get_slice(self):
        all_site = site.objects.all()
        slice_site = all_site[0:2]
        for s in slice_site:
            print s
    
    #2.3 条件唯一查询
    def get_one(self):
        #site_name为'优酷'的含义多条时，会报错
        st = site.objects.get(site_name='优酷')
        print st
        
    #2.4 条件过滤
    #2.4.1 等于
    def filter_equal(self):
        st = site.objects.filter(site_code='youku')
        #st = site.objects.filter(site_code_exact='youku')
        print st
    #2.4.2 忽略大小写的等于
    def filter_equal_iexact(self):
        st = site.objects.filter(site_code__ieact='YouKu')
        print st
    #2.4.3 包含
    def filter_contains(self):
        st = site.objects.filter(site_code__contains='ku')
        print st
    #2.4.4 忽略大小写的包含
    def filter_icontain(self):
        st = site.objects.filter(site_code__contains='KU')
        print st
    #2.4.5 正则表达式过滤
    def filter_regex(self):
        st = site.objects.filter(site_code__regex='^you')
        print st
    #2.4.6 忽略正则表达式过滤
    def filter_iregex(self):
        st = site.objects.filter(site_code__iregex='^YoU')
        print st
    #2.4.7 排除
    def exclude(self):
        st = site.objects.exclude(site_code__exact='youku')
        print st
        
if __name__ == "__main__":
    qso = QuerySetOperation()
#     qso.create_site1()
#     qso.create_site2()
#     qso.create_site3()
#     qso.create_site4()
#     qso.get_all()
    qso.get_slice()