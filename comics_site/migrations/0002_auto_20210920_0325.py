# Generated by Django 3.2.7 on 2021-09-19 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comics_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comics',
            options={'verbose_name': 'Комикс', 'verbose_name_plural': 'Комиксы'},
        ),
        migrations.AddField(
            model_name='comics',
            name='photo',
            field=models.ImageField(blank=True, height_field=100, upload_to='img', width_field=100),
        ),
        migrations.AlterField(
            model_name='comics',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics_site.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='comics',
            name='comment',
            field=models.TextField(blank=True, max_length=200, verbose_name='Комментарий'),
        ),
    ]
