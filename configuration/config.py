import settings
# MySQL 配置
from configuration.configYaml import configManage

mysql_conf = {
    'host': configManage().getIp,
    'port':30006,
    'database': 'AnyRobot',
    'user': 'root',
    'password': 'eisoo.com',
    'charset': 'utf8'
}

header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8'
}
