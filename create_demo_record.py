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
    
    def get_slice(self):
        all_site = site.objects.all()
        slice_site = all_site[0:2]
        for s in slice_site:
            print s
        
if __name__ == "__main__":
    qso = QuerySetOperation()
#     qso.create_site1()
#     qso.create_site2()
#     qso.create_site3()
#     qso.create_site4()
#     qso.get_all()
    qso.get_slice()