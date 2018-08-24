# Generated by Django 2.0.3 on 2018-08-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='life_Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useId', models.CharField(max_length=5, verbose_name='用户ID')),
                ('positionsId', models.CharField(max_length=5, verbose_name='地址ID')),
                ('firstLevel', models.CharField(max_length=20, verbose_name='一级目录')),
                ('secondLevel', models.CharField(max_length=50, verbose_name='二级目录')),
                ('title', models.CharField(max_length=100, verbose_name='商家名称')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
            options={
                'verbose_name': '生活服务',
                'verbose_name_plural': '生活服务',
                'db_table': 'life_Services',
            },
        ),
        migrations.CreateModel(
            name='medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useId', models.CharField(max_length=5, verbose_name='用户ID')),
                ('positionsId', models.CharField(max_length=5, verbose_name='地址ID')),
                ('firstLevel', models.CharField(max_length=20, verbose_name='一级目录')),
                ('secondLevel', models.CharField(max_length=50, verbose_name='二级目录')),
                ('title', models.CharField(max_length=100, verbose_name='商家名称')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
            options={
                'verbose_name': '医疗',
                'verbose_name_plural': '医疗',
                'db_table': 'medical',
            },
        ),
    ]
