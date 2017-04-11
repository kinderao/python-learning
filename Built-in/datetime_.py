#  datetime是python处理时间和日期的标准库

#  获取当期时间和日期
from datetime import datetime
now = datetime.now()
print(now)   # 2017-04-03 21:50:12.220508
#  注意datetime是模块，datetime模块还包含一个datetime类
# datetime.now() 返回当前日期和时间  其类型是datetime


#  获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)   # 2015-04-19 12:20:00


#  datetime转换为timestamp
print(dt.timestamp())   # 1429417200.0

#  timestamp转换为datetime
print(datetime.fromtimestamp(1429417200.0))  # 2015-04-19 12:20:00


#  str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)   # 2015-06-01 18:19:59

#  datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))   # Mon, Apr 03 21:59


#   datetime加减
from datetime import timedelta

print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=1, hours=2))


# 本地时间转换为utc时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


#  时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)