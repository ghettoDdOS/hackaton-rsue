# Generated by Django 3.2.4 on 2021-06-23 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('sub_title', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('format_type', models.CharField(max_length=255, verbose_name='Формат проведения')),
                ('date', models.CharField(max_length=255, verbose_name='Дата проведения')),
                ('registration', models.BooleanField(default=True, help_text='По умолчанию открыта', verbose_name='Открыть/закрыть регистрацию')),
                ('video_link', models.URLField(blank=True, help_text='Ссылка из iframe на youtube', null=True, verbose_name='Ссылка на трансляцию')),
            ],
            options={
                'verbose_name': 'Основные настройки',
                'verbose_name_plural': 'Основные настройки',
            },
        ),
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('date', models.DateField(verbose_name='Дата проведения')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('file', models.FileField(blank=True, null=True, upload_to='static/doc', verbose_name='Документ')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Порядок вывода')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Спонсор')),
                ('logo', models.ImageField(upload_to='static/image/footer-logo', verbose_name='Логотип')),
                ('link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Спонсор',
                'verbose_name_plural': 'Спонсоры',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=100, verbose_name='Название')),
                ('tasks', models.TextField(verbose_name='Задачи')),
                ('caseholder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='managment.sponsors', verbose_name='Спонсор')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
    ]
