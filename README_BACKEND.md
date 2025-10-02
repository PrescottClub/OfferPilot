# OfferPilot Django Backend

这是OfferPilot微信小程序的Django后端API服务。

---

## 📁 完整项目结构

```
OfferPilot/
├── index.py                          # 🚀 项目启动入口文件
├── requirements.txt                  # Python依赖包列表
├── .env.example                      # 环境变量配置示例
├── .gitignore                        # Git忽略文件配置
├── Makefile                          # 快捷命令脚本
├── README_BACKEND.md                 # 后端文档（本文件）
│
├── backend/                          # Django后端主目录
│   ├── manage.py                     # Django管理脚本
│   │
│   ├── offerpilot/                   # Django项目配置目录
│   │   ├── __init__.py
│   │   ├── settings.py               # 项目配置文件
│   │   ├── urls.py                   # 主路由配置
│   │   ├── wsgi.py                   # WSGI服务器配置
│   │   └── asgi.py                   # ASGI服务器配置
│   │
│   ├── users/                        # 用户管理应用
│   │   ├── __init__.py
│   │   ├── apps.py                   # 应用配置
│   │   ├── models.py                 # 数据模型（User自定义用户模型）
│   │   ├── serializers.py            # DRF序列化器
│   │   ├── views.py                  # 视图集（UserViewSet）
│   │   ├── urls.py                   # 路由配置
│   │   ├── admin.py                  # 管理后台配置
│   │   └── migrations/               # 数据库迁移文件
│   │
│   ├── chat/                         # AI对话应用
│   │   ├── __init__.py
│   │   ├── apps.py                   # 应用配置
│   │   ├── models.py                 # 数据模型（Conversation, Message）
│   │   ├── serializers.py            # DRF序列化器
│   │   ├── views.py                  # 视图集（ConversationViewSet, MessageViewSet）
│   │   ├── urls.py                   # 路由配置
│   │   ├── admin.py                  # 管理后台配置
│   │   └── migrations/               # 数据库迁移文件
│   │
│   ├── tools/                        # 工具与大学数据应用
│   │   ├── __init__.py
│   │   ├── apps.py                   # 应用配置
│   │   ├── models.py                 # 数据模型（Tool, University, Major）
│   │   ├── serializers.py            # DRF序列化器
│   │   ├── views.py                  # 视图集（ToolViewSet, UniversityViewSet, MajorViewSet）
│   │   ├── urls.py                   # 路由配置
│   │   ├── admin.py                  # 管理后台配置
│   │   └── migrations/               # 数据库迁移文件
│   │
│   ├── profile/                      # 用户档案应用
│   │   ├── __init__.py
│   │   ├── apps.py                   # 应用配置
│   │   ├── models.py                 # 数据模型（UserProfile, Application）
│   │   ├── serializers.py            # DRF序列化器
│   │   ├── views.py                  # 视图集（UserProfileViewSet, ApplicationViewSet）
│   │   ├── urls.py                   # 路由配置
│   │   ├── admin.py                  # 管理后台配置
│   │   └── migrations/               # 数据库迁移文件
│   │
│   ├── wechat/                       # 微信集成应用
│   │   ├── __init__.py
│   │   ├── apps.py                   # 应用配置
│   │   ├── models.py                 # 数据模型（预留）
│   │   ├── views.py                  # API视图（WeChatLoginView, WeChatUserInfoView）
│   │   ├── urls.py                   # 路由配置
│   │   └── admin.py                  # 管理后台配置
│   │
│   ├── logs/                         # 日志目录
│   │   └── .gitkeep
│   ├── static/                       # 静态文件目录
│   │   └── .gitkeep
│   └── media/                        # 媒体文件目录
│       └── .gitkeep
│
└── pages/                            # 微信小程序前端（已存在）
    ├── tools/
    ├── chat/
    └── profile/
```

---

## 🗄️ 数据库模型设计

### 1. **users.User** - 用户模型
```python
- id (BigInt, PK)
- username (String, Unique)
- wechat_openid (String, Unique, Nullable)     # 微信OpenID
- wechat_unionid (String, Unique, Nullable)    # 微信UnionID
- avatar (ImageField, Nullable)                # 用户头像
- nickname (String)                            # 昵称
- phone (String)                               # 手机号
- email (String)                               # 邮箱
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

### 2. **chat.Conversation** - 对话会话
```python
- id (BigInt, PK)
- user (ForeignKey -> User)                    # 所属用户
- title (String)                               # 对话标题
- is_active (Boolean)                          # 是否激活
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

### 3. **chat.Message** - 对话消息
```python
- id (BigInt, PK)
- conversation (ForeignKey -> Conversation)    # 所属会话
- role (String)                                # 角色：user/assistant/system
- content (Text)                               # 消息内容
- metadata (JSON)                              # 元数据
- created_at (DateTime)                        # 创建时间
```

### 4. **tools.Tool** - 工具
```python
- id (BigInt, PK)
- name (String)                                # 工具名称
- description (Text)                           # 工具描述
- icon (ImageField)                            # 图标
- category (String)                            # 分类：ielts/document/qa/visa等
- is_active (Boolean)                          # 是否启用
- order (Integer)                              # 排序
- url (String)                                 # 跳转链接
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

### 5. **tools.University** - 大学
```python
- id (BigInt, PK)
- name (String)                                # 大学中文名称
- name_en (String)                             # 大学英文名称
- region (String)                              # 地区：uk/us/au/ca等
- country (String)                             # 国家
- city (String)                                # 城市
- ranking (Integer)                            # 排名
- website (URL)                                # 官网
- description (Text)                           # 简介
- logo (ImageField)                            # 校徽
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

### 6. **tools.Major** - 专业
```python
- id (BigInt, PK)
- university (ForeignKey -> University)        # 所属大学
- name (String)                                # 专业中文名称
- name_en (String)                             # 专业英文名称
- degree_type (String)                         # 学位类型
- duration (String)                            # 学制
- tuition (Decimal)                            # 学费
- currency (String)                            # 货币
- requirements (Text)                          # 申请要求
- description (Text)                           # 专业描述
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

### 7. **profile.UserProfile** - 用户档案
```python
- id (BigInt, PK)
- user (OneToOne -> User)                      # 所属用户
- target_regions (JSON)                        # 目标地区列表
- target_universities (JSON)                   # 目标大学列表
- target_majors (JSON)                         # 目标专业列表
- ielts_score (Decimal)                        # 雅思成绩
- toefl_score (Integer)                        # 托福成绩
- gre_score (Integer)                          # GRE成绩
- gmat_score (Integer)                         # GMAT成绩
- gpa (Decimal)                                # GPA
- undergraduate_school (String)                # 本科学校
- major (String)                               # 本科专业
- graduation_year (Integer)                    # 毕业年份
- work_experience (Text)                       # 工作经验
- research_experience (Text)                   # 科研经历
- extracurricular (Text)                       # 课外活动
- awards (Text)                                # 获奖情况
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

### 8. **profile.Application** - 申请记录
```python
- id (BigInt, PK)
- user (ForeignKey -> User)                    # 所属用户
- university_name (String)                     # 大学名称
- major_name (String)                          # 专业名称
- degree_type (String)                         # 学位类型
- status (String)                              # 申请状态：preparing/submitted/offer等
- application_date (Date)                      # 申请日期
- deadline (Date)                              # 截止日期
- result_date (Date)                           # 结果日期
- notes (Text)                                 # 备注
- created_at (DateTime)                        # 创建时间
- updated_at (DateTime)                        # 更新时间
```

---

## 🔌 API接口文档

### 基础URL
```
开发环境: http://localhost:8000/api
生产环境: https://your-domain.com/api
```

### 用户相关 (`/api/users/`)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/api/users/me/` | 获取当前用户信息 | 需登录 |
| PUT/PATCH | `/api/users/update_profile/` | 更新用户信息 | 需登录 |

### 对话相关 (`/api/chat/`)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/api/chat/conversations/` | 获取对话列表 | 需登录 |
| POST | `/api/chat/conversations/` | 创建新对话 | 需登录 |
| GET | `/api/chat/conversations/{id}/` | 获取对话详情 | 需登录 |
| PUT/PATCH | `/api/chat/conversations/{id}/` | 更新对话 | 需登录 |
| DELETE | `/api/chat/conversations/{id}/` | 删除对话 | 需登录 |
| POST | `/api/chat/conversations/{id}/send_message/` | 发送消息 | 需登录 |
| DELETE | `/api/chat/conversations/{id}/clear_messages/` | 清空对话 | 需登录 |

### 工具相关 (`/api/tools/`)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/api/tools/list/` | 获取工具列表 | 公开 |
| GET | `/api/tools/list/?search=关键词` | 搜索工具 | 公开 |
| GET | `/api/tools/list/?category=ielts` | 按分类筛选 | 公开 |
| GET | `/api/tools/universities/` | 获取大学列表 | 公开 |
| GET | `/api/tools/universities/{id}/` | 获取大学详情（含专业） | 公开 |
| GET | `/api/tools/universities/?search=关键词` | 搜索大学 | 公开 |
| GET | `/api/tools/universities/?region=uk` | 按地区筛选 | 公开 |
| GET | `/api/tools/majors/` | 获取专业列表 | 公开 |
| GET | `/api/tools/majors/?university={id}` | 按大学筛选专业 | 公开 |

### 档案相关 (`/api/profile/`)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/api/profile/info/me/` | 获取用户档案 | 需登录 |
| PUT/PATCH | `/api/profile/info/update_profile/` | 更新用户档案 | 需登录 |
| GET | `/api/profile/applications/` | 获取申请记录列表 | 需登录 |
| POST | `/api/profile/applications/` | 创建申请记录 | 需登录 |
| GET | `/api/profile/applications/{id}/` | 获取申请记录详情 | 需登录 |
| PUT/PATCH | `/api/profile/applications/{id}/` | 更新申请记录 | 需登录 |
| DELETE | `/api/profile/applications/{id}/` | 删除申请记录 | 需登录 |
| GET | `/api/profile/applications/statistics/` | 获取申请统计 | 需登录 |

### 微信相关 (`/api/wechat/`)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| POST | `/api/wechat/login/` | 微信小程序登录 | 公开 |
| POST | `/api/wechat/userinfo/` | 更新微信用户信息 | 公开 |

---

## 🚀 快速开始

### 方式一：使用 index.py 启动（推荐）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入数据库等配置

# 3. 创建数据库
mysql -u root -p
CREATE DATABASE offerpilot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit;

# 4. 运行数据库迁移
python3 index.py migrate

# 5. 创建缓存表
python3 index.py createcache

# 6. 创建管理员账户
python3 index.py createsuperuser

# 7. 启动服务器
python3 index.py          # 默认8000端口
python3 index.py 9000     # 指定9000端口
```

### 方式二：使用传统方式启动

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
cp .env.example .env

# 3. 创建数据库（同上）

# 4. 进入backend目录
cd backend

# 5. 运行迁移
python manage.py makemigrations
python manage.py migrate

# 6. 创建缓存表
python manage.py createcachetable

# 7. 创建超级用户
python manage.py createsuperuser

# 8. 运行服务器
python manage.py runserver
```

### 方式三：使用 Makefile

```bash
make install      # 安装依赖
make migrate      # 运行迁移
make superuser    # 创建超级用户
make run          # 启动服务器
make clean        # 清理临时文件
```

---

## ⚙️ 环境配置

### .env 配置文件示例

```env
# Django Settings
DJANGO_SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (MySQL)
DB_NAME=offerpilot
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306

# WeChat Mini Program
WECHAT_APP_ID=wxf3c2565e0e00d81a
WECHAT_APP_SECRET=your-wechat-app-secret

# CORS
CORS_ALLOWED_ORIGINS=https://servicewechat.com
```

---

## 📦 依赖包说明

| 包名 | 版本 | 用途 |
|------|------|------|
| Django | 3.2.8 | Web框架核心 |
| djangorestframework | 3.12.4 | REST API支持 |
| django-cors-headers | 3.10.0 | 跨域请求支持（微信小程序） |
| PyMySQL | 1.0.2 | MySQL数据库驱动 |
| python-dotenv | 0.19.1 | 环境变量管理 |
| pytz | 2021.3 | 时区支持 |
| sqlparse | 0.4.2 | SQL解析 |
| asgiref | 3.4.1 | ASGI规范实现 |

---

## 🔧 常用命令

### 使用 index.py

```bash
python3 index.py                    # 启动开发服务器（8000端口）
python3 index.py 9000               # 启动服务器（9000端口）
python3 index.py migrate            # 运行数据库迁移
python3 index.py shell              # 进入Django Shell
python3 index.py createsuperuser    # 创建超级用户
python3 index.py createcache        # 创建缓存表
python3 index.py help               # 查看帮助
```

### 使用 manage.py（需先进入backend目录）

```bash
cd backend
python manage.py runserver          # 启动服务器
python manage.py makemigrations     # 生成迁移文件
python manage.py migrate            # 应用迁移
python manage.py createsuperuser    # 创建管理员
python manage.py shell              # Django Shell
python manage.py test               # 运行测试
python manage.py collectstatic      # 收集静态文件
```

---

## 🌐 访问地址

- **开发服务器**: http://localhost:8000
- **管理后台**: http://localhost:8000/admin
- **API根路径**: http://localhost:8000/api
- **用户API**: http://localhost:8000/api/users/
- **对话API**: http://localhost:8000/api/chat/
- **工具API**: http://localhost:8000/api/tools/
- **档案API**: http://localhost:8000/api/profile/
- **微信API**: http://localhost:8000/api/wechat/

---

## 🛠️ 开发注意事项

1. **API格式**: 所有接口返回JSON格式
2. **认证方式**: 使用Session认证（可扩展Token认证）
3. **API规范**: 遵循RESTful设计原则
4. **时区设置**: 使用亚洲/上海时区
5. **分页**: 默认每页20条记录
6. **CORS**: 已配置支持微信小程序跨域请求
7. **数据库**: 使用MySQL，字符集utf8mb4
8. **缓存**: 使用数据库缓存（需创建缓存表）

---

## 🚢 生产环境部署

### 部署检查清单

- [ ] 设置 `DEBUG=False`
- [ ] 配置 `ALLOWED_HOSTS`（添加域名）
- [ ] 生成并配置强密码的 `SECRET_KEY`
- [ ] 配置MySQL生产数据库
- [ ] 配置HTTPS证书
- [ ] 配置Nginx反向代理
- [ ] 配置静态文件服务
- [ ] 配置媒体文件存储
- [ ] 设置日志记录
- [ ] 配置微信小程序生产AppSecret

### 推荐部署架构

```
Nginx (反向代理)
  ↓
uWSGI/Gunicorn (WSGI服务器)
  ↓
Django Application
  ↓
MySQL Database
```

---

## 📝 TODO 清单

- [ ] 完善AI服务集成（接入ChatGPT/Claude等）
- [ ] 实现JWT Token认证
- [ ] 添加单元测试和集成测试
- [ ] 添加API文档（Swagger/OpenAPI）
- [ ] 实现数据导入导出功能
- [ ] 添加限流和防刷机制
- [ ] 优化数据库查询性能
- [ ] 添加日志监控系统

---

## 📄 许可证

待定

---

## 📞 技术支持

如有问题，请提交Issue或联系开发团队。
