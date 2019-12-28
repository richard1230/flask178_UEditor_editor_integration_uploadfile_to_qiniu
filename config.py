#encoding: utf-8
import os

UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
# print(os.path.dirname(__file__))#打印出config目录

UEDITOR_UPLOAD_TO_QINIU = True

UEDITOR_QINIU_ACCESS_KEY ='6C0-gZV-pWuDoRiRU1tq14P5gW1wFbq0GEtq_zeP'
UEDITOR_QINIU_SECRET_KEY = 'AgPOGPd3MLamYt4U-5rhl8LRcxRxEf_ljrotu0Gn'
UEDITOR_QINIU_BUCKET_NAME = "richard1230"
UEDITOR_QINIU_DOMAIN = 'http://q35lhq667.bkt.clouddn.com/'
