import types

types.DictType=dict
types.ListType=list

# 获取字典中的objkey对应的值，适用于字典嵌套
# dict:字典
# objkey:目标key
# default:找不到时返回的默认值
def dict_get(dict, objkey, default):
    tmp = dict

    for k, v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v) == types.DictType:
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
            else:
                if type(v) == types.ListType:
                    for i in range(len(v)):
                        if type(v[i]) == types.DictType:

                            ret = dict_get(v[i], objkey, default)

                            if ret is not default:
                                return ret

    return default



