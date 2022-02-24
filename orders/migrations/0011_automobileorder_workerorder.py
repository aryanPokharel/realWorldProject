# Generated by Django 2.1.5 on 2021-09-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order2_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobileOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('total_price', models.FloatField(default=0, null=True)),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('remarks', models.TextField(max_length=250, null=True)),
                ('automobile_name', models.CharField(default='noautomobile', max_length=200)),
                ('customer_name', models.CharField(default='noname', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('total_price', models.FloatField(default=0, null=True)),
                ('remarks', models.TextField(max_length=250, null=True)),
                ('worker_name', models.CharField(default='noworker', max_length=200)),
                ('customer_name', models.CharField(default='noname', max_length=200)),
            ],
        ),
    ]