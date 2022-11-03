# Generated by Django 4.1.2 on 2022-11-03 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentTVShows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='tvshow.tvshow')),
            ],
        ),
    ]
