# Generated by Django 4.2.3 on 2023-08-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_dmd_chitieu_recyclebin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmd_nganhang',
            name='stk',
            field=models.CharField(max_length=50, unique=True, verbose_name='Số tài khoản'),
        ),
    ]
