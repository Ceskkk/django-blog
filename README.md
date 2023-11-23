## Technologies versions

1. Python 3.11.6
2. PostgreSQL 15.3
3. Django 4.2.6
4. Node 18.16.0

## Use this template

1. Create virtual environment and activate

```
python -m venv venv
venv/scripts/activate
```

2. Clone the repository and enter to the directory

```
git clone https://github.com/Ceskkk/blog
cd blog
```

3. Change all 'blog' registers for 'your_proj_name'

4. Install dependencies

```
pip install -r requirements.txt
```

5. Create database

```
CREATE USER 'your_proj_name'_user;
CREATE DATABASE blog_ddbb WITH OWNER 'your_proj_name'_user;
ALTER USER blog_user WITH ENCRYPTED PASSWORD 'your_password';
```

6. Set environment variables

```
SECRET_KEY=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

EMAIL_HOST=
EMAIL_USER=
EMAIL_PASSWORD=
EMAIL_PORT=
```

7. Make and migrate database

```
python manage.py makemigrations
python manage.py migrate
```

8. Install node dependencies

```
npm i
```

9. Build project

```
npm run build
```

10. Run server

```
python manage.py runserver
```