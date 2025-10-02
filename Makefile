.PHONY: help install migrate run test clean

help:
	@echo "OfferPilot Django Backend - 可用命令:"
	@echo "  make install    - 安装依赖"
	@echo "  make migrate    - 运行数据库迁移"
	@echo "  make run        - 运行开发服务器"
	@echo "  make test       - 运行测试"
	@echo "  make clean      - 清理临时文件"
	@echo "  make superuser  - 创建超级用户"

install:
	pip install -r requirements.txt

migrate:
	cd backend && python manage.py makemigrations && python manage.py migrate

run:
	cd backend && python manage.py runserver

test:
	cd backend && python manage.py test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete

superuser:
	cd backend && python manage.py createsuperuser
