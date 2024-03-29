# Generated by Django 5.0.1 on 2024-01-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(db_index=True, max_length=255, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('descripion', models.TextField(max_length=1000, null=True)),
                ('plan_doc', models.FileField(upload_to='media/')),
            ],
        ),
    ]
