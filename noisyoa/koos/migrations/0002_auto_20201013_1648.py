# Generated by Django 3.0.10 on 2020-10-13 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('koos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='koos_ps',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='koos',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='a10_function',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Rising from bed'),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='a3_function',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Rising from sitting'),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='a5_function',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Bending to the floor or picking up an object'),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='a9_function',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Putting on socks or stockings'),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='sp1_exercise',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Squatting'),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='sp4_exercise',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Twisting/pivoting on your injured knee'),
        ),
        migrations.AlterField(
            model_name='koos_ps',
            name='sp5_exercise',
            field=models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Kneeling'),
        ),
    ]
