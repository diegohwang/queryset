#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "queryset.settings")
import django
if django.VERSION >= (1,7):
    django.setup()

def main():
    from video.models import site, media
    media_list = []
    with open(r'media.txt') as media_file:
        for mf in media_file:
            title, url = mf.split('****')
            new_media = media(title=title, url=url)
            media_list.append(new_media)
    media.objects.bulk_create(media_list)
    
if __name__=="__main__":
    main()
    print 'Done!'        