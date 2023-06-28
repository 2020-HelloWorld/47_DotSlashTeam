# Generated by Django 4.2.2 on 2023-06-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_cgpa'),
        ('attendance', '0002_alter_fam_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fam',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.faculty'),
        ),
        migrations.AlterField(
            model_name='fam',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fams', to='home.student'),
        ),
    ]