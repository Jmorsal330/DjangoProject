# Generated by Django 4.2.8 on 2024-04-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_created_at_choice_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='choice',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='question',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Category 1'), ('2', 'Category 2'), ('3', 'Category 3'), ('4', 'Category 4'), ('5', 'Category 5')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]