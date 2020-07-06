from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_test_remove_onetoone_field_part2'),
    ]

    # Issue #58 test prep
    operations = [
        migrations.CreateModel(
            name='TestIndexesRetained',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField(db_index=True)),
                ('b', models.IntegerField(db_index=True)),
                ('c', models.IntegerField(db_index=True)),
            ],
        ),
    ]
