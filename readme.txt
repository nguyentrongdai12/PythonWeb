__init__.py: file cơ bản trong python để biến folder chứa nó thành pakage, import
setttings.py: đây là file cấu hình project. (VD: cấu hình database, đặt múi giờ, cài thêm thư viện, ...)
urls.py: đây là file giúp chúng ta tạo các đường dẫn urls của trang web để liên kết các webpage lại với nhau
wsgi.py: đây là file giúp chúng ta deploy project lên server

*** Chạy Server:
python manage.py runserver
python manage.py runserver <Tên Cổng>

*** Để tạo 1 Web App. Hãy gõ lệnh này sau trong CMD:
python manage.py startapp <Tên APP>

settings.py: Khai báo app tại Íntalled_apps

**** cập nhật cho phần settings
python manage.py migrate

*** viết 1 hàm xử lý ở file views.py trong app home.

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   response = HttpResponse()
   response.writelines('<h1>Xin chào</h1>')
   response.write('Đây là app home')
   return response

*** tạo tên trường tùy biến của model khi hiển thị bằng cú pháp
verbose_name='Tên trường'
Ví dụ: id_danhmucchi = models.IntegerField(verbose_name='Danh mục chi')
   

