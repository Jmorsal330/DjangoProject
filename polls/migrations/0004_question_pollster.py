# Generated by Django 4.2.8 on 2024-04-21 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_remove_choice_updated_at_remove_question_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pollster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]