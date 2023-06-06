# Generated by Django 4.2.1 on 2023-06-06 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('kasb', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=100)),
                ('sana', models.DateField()),
                ('mavzu', models.CharField(max_length=100)),
                ('matn', models.TextField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asosiy.muallif')),
            ],
        ),
    ]