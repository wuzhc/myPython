from django.contrib import admin
from .models import Post

#admin中注册对应的模型
#注意上面的from .models import Post，使用到了python3的相对导入。
admin.site.register(Post)
