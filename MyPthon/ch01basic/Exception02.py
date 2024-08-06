# Q. 입력한 사람의 이름이 걸그룹 '여자 친구'의 멤버가 맞는 지 체크하고, 적절한 예외 처리를 수행하시오.
# 프로그래머가 오류 상황을 직접 정의하여 예외를 발생시켜야 할 때도 있습니다.
# 예외를 직접 발생시키는 방법으로는 raise 문을 이용하는 방법이 있습니다.

def girlFriendCheck(findName):
    girlFriend = ['은하', '소원', '유주', '예린', '신비', '엄지']
    isMember = findName in girlFriend # True or False가 반환 된다.

    if isMember:
        message = '\'%s\'님은 여자 친구 멤버 입니다.' % findName
        print(message)
    else:
        message = '\'%s\'님은 여자 친구 멤버가 아닙니다.' % findName
        raise Exception(message) # throw와 같은 역할
# end def

name = 'dd'

try:
    girlFriendCheck(name)
except Exception as err:
    print('예외 발생 : {}'.format(err))