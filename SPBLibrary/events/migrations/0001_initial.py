# Generated by Django 3.2 on 2023-05-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='events/<django.db.models.fields.CharField>')),
                ('date', models.DateTimeField()),
                ('organizations', models.ManyToManyField(related_name='events', to='organizations.Organization')),
            ],
        ),
    ]