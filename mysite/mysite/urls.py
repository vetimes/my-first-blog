from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),  # 블로그로 끝나는 url을 그 뒤는 blog폴더의 url파일에 나머지를 맡긴다
]
