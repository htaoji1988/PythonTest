#!/usr/bin/python
# -*- coding: utf-8 -*-


from qiniu import Auth, put_file, etag
import json
import sys

# 需要填写你的 Access Key 和 Secret Key
access_key = '0XWcsyZkEmUT2KONTunDpcC-NKqDE0HvD2yjm-O8'
secret_key = 'VdJbiUy3GVhq7rrn_35BTCsYmTHKryrv83Rja2Bi'

# 获取版本号
json_path = '/Users/tt/.jenkins/workspace/yq/src/version.json'


def get_version(jsonfile):
    config_data = open(jsonfile)
    config = json.load(config_data)
    config_data.close()
    return config['version']


env = get_version(json_path)

# 要上传的空间
bucket_name = 'fsdl'

# 上传到七牛后保存的文件名
key = 'eep/%s/%s/appTest.ipa' % (sys.argv[1], env)

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)


# 要上传文件的本地路径
localfile = '/Users/tt/Desktop/wwss/appTest/appTest.ipa'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)



