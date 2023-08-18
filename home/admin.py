from django.contrib import admin
from . models import dmd_chitieu, dmd_danhmucchi, dmd_nganhang, dmd_typenganhang

# custom header admin site
admin.site.site_header = 'Trình quản lý CDB Tech'

# Register your models here.
class ChiTieu(admin.ModelAdmin):
    search_fields = ['description']
    list_display = ['description', 'ct_sotien', 'ct_ngaychi']
    list_filter = ['ct_ngaychi']
    app_label = 'Chi tiêu'
    
admin.site.register(dmd_chitieu,ChiTieu)

class DanhMucChiTieu(admin.ModelAdmin):
    search_fields = ['tenhangmuc']
    list_display = ['tenhangmuc', 'slug', 'description', 'status', 'createat', 'updateat']
    list_filter = ['createat']
    prepopulated_fields = {'slug': ('tenhangmuc',)}
    app_label = 'Chi tiêu'
    

admin.site.register(dmd_danhmucchi,DanhMucChiTieu)

class DanhMucNganHang(admin.ModelAdmin):
    search_fields = ['tennganhang']
    list_display = ['tennganhang','description', 'tengiaodich', 'stk', 'status', 'createat']
    list_filter = ['createat']
    prepopulated_fields = {'slug': ('tennganhang',)}

admin.site.register(dmd_nganhang,DanhMucNganHang)

class LoaiTKNganHang(admin.ModelAdmin):
    search_fields = ['tenloai']
    list_display = ['tenloai','status', 'createat', 'updateat']
    list_filter = ['createat']
    
admin.site.register(dmd_typenganhang,LoaiTKNganHang)
