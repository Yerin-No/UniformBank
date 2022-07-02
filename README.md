# UniformBank
- project/urls.py -> app/urls.py -> views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트
- 개발 순서: models.py, views.py, urls.py, templates
1. startproject UniformBank
    1. python -m pip install django~=3.2
    2. django-admin startproject UniformBank .
    3. python manage.py runserver