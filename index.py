#!/usr/bin/env python3
"""
OfferPilot Django Backend Entry Point

使用方式:
    python3 index.py          # 启动开发服务器 (默认端口8000)
    python3 index.py 8080     # 启动开发服务器 (指定端口)
    python3 index.py migrate  # 运行数据库迁移
    python3 index.py shell    # 进入Django Shell
"""

import os
import sys
from pathlib import Path

# 使用PyMySQL作为MySQLdb的替代 (必须在Django导入之前)
import pymysql
pymysql.install_as_MySQLdb()
# 设置版本号以通过Django的版本检查
pymysql.version_info = (1, 4, 6, 'final', 0)

# 添加backend目录到Python路径
backend_dir = Path(__file__).resolve().parent / 'backend'
sys.path.insert(0, str(backend_dir))

# 设置Django设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offerpilot.settings')


def main():
    """主函数 - 处理不同的启动命令"""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入Django。请确保已安装Django并且虚拟环境已激活。\n"
            "运行: pip install -r requirements.txt"
        ) from exc

    # 获取命令行参数
    args = sys.argv[1:]

    # 如果没有参数，默认启动开发服务器
    if not args:
        print("=" * 60)
        print("🚀 正在启动 OfferPilot Django Backend...")
        print("=" * 60)
        execute_from_command_line(['manage.py', 'runserver'])

    # 如果第一个参数是数字，作为端口号启动服务器
    elif args[0].isdigit():
        port = args[0]
        print("=" * 60)
        print(f"🚀 正在启动 OfferPilot Django Backend (端口: {port})...")
        print("=" * 60)
        execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:{port}'])

    # 数据库迁移命令
    elif args[0] == 'migrate':
        print("=" * 60)
        print("📦 正在运行数据库迁移...")
        print("=" * 60)
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("\n✅ 数据库迁移完成！")

    # Django Shell
    elif args[0] == 'shell':
        print("=" * 60)
        print("🐚 进入 Django Shell...")
        print("=" * 60)
        execute_from_command_line(['manage.py', 'shell'])

    # 创建超级用户
    elif args[0] == 'createsuperuser':
        print("=" * 60)
        print("👤 创建超级用户...")
        print("=" * 60)
        execute_from_command_line(['manage.py', 'createsuperuser'])

    # 创建缓存表
    elif args[0] == 'createcache':
        print("=" * 60)
        print("💾 创建缓存表...")
        print("=" * 60)
        execute_from_command_line(['manage.py', 'createcachetable'])
        print("\n✅ 缓存表创建完成！")

    # 帮助信息
    elif args[0] in ['help', '-h', '--help']:
        print_help()

    # 其他Django命令直接传递
    else:
        execute_from_command_line(['manage.py'] + args)


def print_help():
    """打印帮助信息"""
    print("""
OfferPilot Django Backend - 入口脚本

使用方式:
    python3 index.py                    启动开发服务器 (默认端口8000)
    python3 index.py 8080               启动开发服务器 (指定端口8080)
    python3 index.py migrate            运行数据库迁移
    python3 index.py shell              进入Django Shell
    python3 index.py createsuperuser    创建超级用户
    python3 index.py createcache        创建数据库缓存表
    python3 index.py help               显示此帮助信息

其他Django命令:
    python3 index.py <django_command>   执行任意Django管理命令

示例:
    python3 index.py                    # 启动服务器
    python3 index.py 9000               # 在9000端口启动
    python3 index.py migrate            # 数据库迁移
    python3 index.py collectstatic      # 收集静态文件
    python3 index.py test               # 运行测试

快速开始:
    1. 安装依赖:        pip install -r requirements.txt
    2. 配置环境变量:    cp .env.example .env (并编辑)
    3. 创建数据库:      mysql -u root -p -e "CREATE DATABASE offerpilot"
    4. 运行迁移:        python3 index.py migrate
    5. 创建缓存表:      python3 index.py createcache
    6. 创建管理员:      python3 index.py createsuperuser
    7. 启动服务器:      python3 index.py

访问地址:
    开发服务器: http://localhost:8000
    管理后台:   http://localhost:8000/admin
    API文档:    http://localhost:8000/api
    """)


if __name__ == '__main__':
    main()
