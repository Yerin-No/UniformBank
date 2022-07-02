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
   4. uniform/views UniformListView
   5. urls, uniform/urls uniform:list
   6. templates uniform_list.html
   7. uniform/views UniformCreateView
   8. uniform/size uniform:add
   9. templates uniform_create.html
   10. uniform/views UniformDetailView
   11. uniform/urls uniform:detail
   12. templates uniform_detail.html
   13. uniform/views UniformUpdateView
   14. uniform/urls uniform:edit 
   15. templates uniform_update.html
   16. get_absolute_url() in Bookmark
   17. uniform/views UniformDeleteView
   18. uniform/urls uniform:delete
   19. templates uniform_confirm_delete.html
4. 기능 완성
   1. templates/base.html, extends 'base.html', block title, content
         