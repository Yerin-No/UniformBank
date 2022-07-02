# UniformBank
- project/urls.py -> app/urls.py -> views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트
- 개발 순서: models.py, views.py, urls.py, templates
1. startproject UniformBank
    1. python -m pip install django~=3.2
    2. django-admin startproject UniformBank .
    3. python manage.py runserver
2. startapp uniform
   1. python manage.py startapp uniform
   2.add 'uniform', to INSTALLED_APPS in settings.py
3. uniform/models UniformBank
   1. python manage.py makemigrations uniform
      1. models -> DB로 옮기기 위한 py
   2. python manage.py migrate
      1. DB 테이블 만들기
   3. uniform/admin Uniform
      1. python manage.py createsuperuser
      2. uniform/models Uniform \_\_str\_\_()
   