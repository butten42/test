import uuid

#num is the mun of coupons
def create_num(num, length=16):
    result=[]
    while num>0:
        uuid_id=uuid.uuid1()
        temp = str(uuid_id).replace('-','')[:length]
        if temp not in result:
            result.append(temp)
            num-=1
    return result
print (create_num(12))
print (create_num(10,10))





