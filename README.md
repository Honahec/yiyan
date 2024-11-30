# 一言 API

一个简单的"一言"API 服务，基于 Django REST framework 构建。可以随机返回一句话，支持添加、修改、删除句子。

## 功能特性

- ✨ RESTful API 设计
- 🎲 随机获取一句话
- ✍️ 支持内容和作者信息
- 🔄 完整的 CRUD 操作支持
- 📝 Django Admin 管理界面
- 🔒 CORS 跨域保护

## 技术栈

- Python 3.x
- Django 5.1
- Django REST framework
- Django CORS Headers

## 快速开始

1. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

2. 安装依赖

```bash
pip install django djangorestframework django-cors-headers
```

3. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

4. 创建超级用户

```bash
python manage.py createsuperuser
```

5. 启动服务器

```bash
python manage.py runserver <port>
```

服务器将在 `http://localhost:<port>` 启动

## API 接口

### 获取随机句子

```
GET /yiyan/get/
```

### 获取所有句子

```
GET /yiyan/sentences/
```

### 添加新句子

```
POST /yiyan/sentences/
```

### 获取特定句子

```
GET /yiyan/sentences/{id}/
```

### 更新句子

```
PUT /yiyan/sentences/{id}/
```

### 删除句子

```
DELETE /yiyan/sentences/{id}/
```

## 管理界面

访问 `/yiyan/admin/` 进入 Django 管理界面，可以直接管理句子内容。

## 开发说明

- 项目使用 SQLite 作为默认数据库
- 已配置 CORS，默认允许来自 `https://blog.honahec.cc` 的请求
- 已配置 ALLOWED_HOST，默认允许 `api.honahec.cc`
- 所有 API 路由都以 `/yiyan/` 为前缀

## 注意事项

- 生产环境部署时请修改 `settings.py` 中的 `SECRET_KEY`
- 关闭 `DEBUG` 模式
- 根据需要调整 ALLOWED_HOSTS 和 CORS 设置
