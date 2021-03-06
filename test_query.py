#!/usr/bin/python
# -*- coding:utf-8 -*-

from queryset.wsgi import *
from video.models import site, media

class QuerySetOperation():
    
#1. 创建对象(4种方法)

    #1.1
    def create_site1(self):
	print '创建方法1'
        site.objects.create(site_name='BT天堂', site_code='bttiantang', site_id=1)
        
    #1.2
    def create_site2(self):
	print '创建方法2'
        new_site = site(site_name='高清mp4吧', site_code='mp4ba', site_id=2)
        new_site.save()
        
    #1.3
    def create_site3(self):
	print '创建方法3'
        new_site = site()
        new_site.site_name = '海盗窝'
        new_site.site_code = 'hdwo'
        new_site.site_id = 3
        new_site.save()
        
    #1.4 首先尝试获取，不存在就创建，可以防止重复(返回值元组(object, True/False))
    def create_site4(self):
	print '创建方法4'
        site.objects.get_or_create(site_name='优酷', site_code='youku', site_id=4)
        
#2. 获取对象(过滤)
    #2.1 查询所有
    def get_all(self):
        all_site = site.objects.all()
        #获取数量
	print type(all_site)
        print all_site.count()
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
	print type(st)
        
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
    
#3 排序
    #3.1 从小到大
    def sort_asc(self):
        sites = site.objects.all().order_by('site_id')
        for s in sites:
            print 'the site_id %d is %s' % (s.site_id, s.site_name)
    #3.2 从大到小
    def sort_desc(self):
        sites = site.objects.all().order_by('-site_id')
        for s in sites:
            print 'the site_id %d is %s' % (s.site_id, s.site_name)

#4 更新
    def update(self):
        st = site.objects.filter(site_name='优酷')
        st.update(site_name='爱奇艺', site_code='iqiyi')
    
#5 删除
    def delete_site(self):
        st = site.objects.all()
        print st.count()
        st.delete()
        print st.count()

    def delete_media(self):
	m = media.objects.all()
	print m.count()
	m.delete()
	print m.count()
    
    def goc1(self):
	st = site.objects.get_or_create(site_name='搜狐', site_code='sohu', defaults={'site_id':6})
	print st

    def uoc1(self):
	st = site.objects.update_or_create(site_name='乐视', site_code='letv', site_id=5, defaults={'site_name':u'搜狐', 'site_code':'sohu', 'site_id':5})
	print st

    def uoc2(self):
	st = site.objects.update_or_create(site_name='搜狐', site_code='sohu', site_id=5, defaults={'site_name':u'乐视', 'site_code':'letv', 'site_id':5})
	print st

    def uoc3(self):
	st = site.objects.update_or_create(site_name='搜狐1', site_code='sohu1', site_id=6, defaults=None)
	print st

if __name__ == "__main__":
    qso = QuerySetOperation()
    #qso.create_site1()
    #qso.create_site2()
    #qso.create_site3()
    #qso.create_site4()
    #qso.get_all()
    #qso.get_one()
    #qso.update()
    qso.delete_site()
    #qso.uoc1()
    #qso.uoc2()
    #qso.uoc3()
    #qso.delete_media()
    #qso.goc1()
