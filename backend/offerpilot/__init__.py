"""
OfferPilot Django Backend Initialization
"""

import pymysql

# 使用PyMySQL作为MySQLdb的替代
pymysql.install_as_MySQLdb()
# 设置版本号以通过Django的版本检查
pymysql.version_info = (1, 4, 6, 'final', 0)
