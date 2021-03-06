# Generated by Django 2.1.5 on 2019-03-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('food', models.CharField(choices=[('^_^', '^_^'), ('breakfast', 'BREAKFAST'), ('lunch', 'LUNCH'), ('dinner', 'DINNER'), ('snacks', 'SNACKS')], default='^_^', max_length=9)),
                ('description', models.TextField()),
                ('calorie', models.PositiveIntegerField(default=0, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
