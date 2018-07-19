'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

import uuid


# 生成 num 个验证码，每个长度为lengths，可设置默认长度
def create_num(num, lengths=10):
    result = []
    while num > 0:
        uuid_id = uuid.uuid1()
        # 删去字符串中的'-',取出前lengths 个字符
        temp = str(uuid_id).replace('-', '')[:lengths]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result
    
print(create_num(200, 32))

#print(create_num(200))

