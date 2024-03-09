# Generated by Django 5.0 on 2024-03-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cabletray',
            fields=[
                ('date_added', models.DateField(auto_now_add=True)),
                ('unit', models.CharField(choices=[('111', '111'), ('515', '515')], default='111', max_length=50)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('tag', models.CharField(max_length=50)),
                ('tray_type', models.CharField(choices=[('BST', 'BST'), ('MST', 'MST'), ('MPT', 'MPT'), ('BPT', 'BPT')], max_length=3)),
                ('size', models.CharField(choices=[(600, 600), (150, 150), (50, 50), (100, 100), (450, 450), (300, 300)], max_length=1)),
                ('from_col', models.CharField(blank=True, max_length=100)),
                ('to_col', models.CharField(blank=True, max_length=100)),
                ('from_ele', models.CharField(blank=True, max_length=100)),
                ('to_ele', models.CharField(blank=True, max_length=100)),
                ('length_completed', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('area', models.CharField(max_length=8)),
                ('tray_size_code', models.CharField(max_length=2)),
                ('ISMC_100', models.DecimalField(decimal_places=5, default=0.0, max_digits=10)),
                ('ISA_50', models.DecimalField(decimal_places=5, default=0.0, max_digits=10)),
                ('ISA_40', models.DecimalField(decimal_places=5, default=0.0, max_digits=10)),
            ],
        ),
    ]