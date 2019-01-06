from django.contrib import admin
# 将m数据表引入
from .models import *

# Register your models here.
class movieScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
class movieInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')
class movieAwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'awardname')
class moviePlayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'moviesite')
    list_filter = ('moviesite', )    # 可以按moviesite字段筛选
class commentInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'time' )



# 在后台中显示数据表
admin.site.register(MovieScore, movieScoreAdmin)
admin.site.register(MovieInfo, movieInfoAdmin)
admin.site.register(MovieAwards, movieAwardsAdmin)
admin.site.register(MoviePlay, moviePlayAdmin)
admin.site.register(CommentInfo, commentInfoAdmin)