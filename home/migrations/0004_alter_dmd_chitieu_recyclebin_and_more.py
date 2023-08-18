# Generated by Django 4.2.3 on 2023-08-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_dmd_danhmucchi_slug_alter_dmd_nganhang_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmd_chitieu',
            name='recyclebin',
            field=models.IntegerField(choices=[(0, 'Không'), (1, 'Thùng rác')], verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='dmd_chitieu',
            name='status',
            field=models.IntegerField(choices=[(1, 'Hoạt động'), (2, 'Tạm ngưng')], verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='dmd_danhmucchi',
            name='status',
            field=models.IntegerField(choices=[(1, 'Hoạt động'), (2, 'Tạm ngưng')], verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='dmd_typenganhang',
            name='status',
            field=models.IntegerField(choices=[(1, 'Hoạt động'), (2, 'Tạm ngưng')], verbose_name='Trạng thái'),
        ),
    ]