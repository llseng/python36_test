import jwt, datetime

payload = {
    'exp': datetime.datetime.utcnow() + datetime.timedelta( days=1 ),
    'userid': 10001
}

token = jwt.encode( payload, '123456', "HS256" )

print( token )

try:
    data = jwt.decode( token, '123456', 'HS256' )
    print( data )
except :
    raise Exception( '无效的令牌或令牌已过期' )
