# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from .models import Reg

class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    #整体配置
    site_title = 'xadmin_django后台系统'
    # site_footer = ‘’xxx'
    menu_style = 'default'    #菜单收起

# class EmailVerifyRecordAdmin(object):
#     #后台列表显示列
#     list_display = ['code', 'email', 'send_type', 'send_time']
#     #后台列表查询条件
#     search_fields = ['code', 'email', 'send_type']
#     #后天列表通过时间查询
#     list_filter = ['code', 'email', 'send_type', 'send_time']


class RegAdmin(object):
    list_display = ['id', 'username', 'mobile', 'code', 'password', 'add_time']

xadmin.site.register(Reg, RegAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)