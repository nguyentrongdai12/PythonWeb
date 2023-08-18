from django.db import models
from django.urls import reverse

# Create your models here.

# model bảng loại tài khoản ngân hàng
class dmd_typenganhang(models.Model):
    id_type = models.AutoField(primary_key=True, verbose_name='ID loại')
    tenloai = models.CharField(max_length=50, verbose_name='Loại tài khoản')
    status = models.IntegerField(verbose_name='Trạng thái', choices=((1, 'Hoạt động'), (2, 'Tạm ngưng')))
    createat = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    updateat = models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')

    def __str__(self):
        return self.tenloai
    
    class Meta:
        verbose_name = 'Loại tài khoản ngân hàng'
        verbose_name_plural = 'Loại tài khoản ngân hàng'


# model bảng ngân hàng
class dmd_nganhang(models.Model):
    id_nganhang = models.AutoField(primary_key=True, verbose_name='ID Ngân hàng')
    tennganhang = models.CharField(max_length=100, verbose_name='Tên ngân hàng')
    slug = models.SlugField(default="", null=False)
    description = models.CharField(max_length=100, verbose_name='Diễn giải')
    tengiaodich = models.CharField(max_length=200, verbose_name='Tên giao dịch')
    stk = models.CharField(max_length=50, verbose_name='Số tài khoản', unique=True)
    id_type = models.ForeignKey(dmd_typenganhang, on_delete=models.CASCADE, verbose_name='Loại tài khoản')
    status = models.IntegerField(verbose_name='Trạng thái', choices=((1, 'Hoạt động'), (2, 'Tạm ngưng')))
    createat = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    updateat = models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')

    def __str__(self):
        return self.tennganhang   


    class Meta:
        verbose_name = 'Danh mục Ngân hàng'
        verbose_name_plural = 'Danh mục Ngân hàng'

# model bảng danhmucchi
class dmd_danhmucchi(models.Model):
    id_danhmucchi = models.AutoField(primary_key=True, verbose_name='ID')
    tenhangmuc = models.CharField(max_length=100, verbose_name='Tên hạng mục')
    slug = models.SlugField(default="", null=False)
    description = models.CharField(max_length=100, verbose_name='Diễn giải')
    status = models.IntegerField(verbose_name='Trạng thái', choices=((1, 'Hoạt động'), (2, 'Tạm ngưng')))
    sort = models.IntegerField(verbose_name='Soft')
    createat = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    updateat = models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')
        
    def __str__(self):
        return self.tenhangmuc
    
    
    class Meta:
        verbose_name = 'Danh mục chi'
        verbose_name_plural = 'Danh mục chi'
    
# model bảng dmd_chitieu
class dmd_chitieu(models.Model):
    id_chitieu = models.AutoField(primary_key=True, verbose_name='ID')
    ct_sotien = models.DecimalField(verbose_name='Số tiền', max_digits=10, decimal_places=0, default=0)
    id_danhmucchi = models.ForeignKey(dmd_danhmucchi, on_delete=models.CASCADE, verbose_name='ID danh mục chi')
    description = models.TextField(verbose_name='Diễn giải')
    id_nganhang = models.ForeignKey(dmd_nganhang, on_delete=models.CASCADE, verbose_name='ID Ngân hàng')
    ct_ngaychi = models.DateTimeField(auto_now_add=True, verbose_name='Ngày chi')
    status = models.IntegerField(verbose_name='Trạng thái', choices=((1, 'Hoạt động'), (2, 'Tạm ngưng')))
    recyclebin = models.IntegerField(verbose_name='Trạng thái', choices=((0, 'Không'), (1, 'Thùng rác')))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Ngày cập nhật')
          
    class Meta:
        verbose_name = 'Danh sách chi tiêu'
        verbose_name_plural = 'Danh sách chi tiêu'
        
