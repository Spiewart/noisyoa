# Generated by Django 3.0.10 on 2020-10-13 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Koos_ps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('a3_function', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Rising from sitting')),
                ('a5_function', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Bending to the floor or picking up an object')),
                ('a9_function', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Putting on socks or stockings')),
                ('a10_function', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Rising from bed')),
                ('sp1_exercise', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Squatting')),
                ('sp4_exercise', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Twisting/pivoting on your injured knee')),
                ('sp5_exercise', models.IntegerField(choices=[('0', 'None'), ('1', 'Mild'), ('2', 'Moderate'), ('3', 'Severe'), ('4', 'Extreme')], verbose_name='Kneeling')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Koos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('s1_symptoms', models.CharField(choices=[('never', 'Never'), ('rarely', 'Rarely'), ('sometimes', 'Sometimes'), ('often', 'Often'), ('always', 'Always')], max_length=10, verbose_name='Do you have swelling in your knee?')),
                ('s2_symptoms', models.CharField(choices=[('never', 'Never'), ('rarely', 'Rarely'), ('sometimes', 'Sometimes'), ('often', 'Often'), ('always', 'Always')], max_length=10, verbose_name='Do you feel grinding, hear clicking or any other type of noise when your knee moves?')),
                ('s3_symptoms', models.CharField(choices=[('never', 'Never'), ('rarely', 'Rarely'), ('sometimes', 'Sometimes'), ('often', 'Often'), ('always', 'Always')], max_length=10, verbose_name='Does your knee catch or hang up when moving?')),
                ('s4_symptoms', models.CharField(choices=[('always', 'Always'), ('often', 'Often'), ('sometimes', 'Sometimes'), ('rarely', 'Rarely'), ('never', 'Never')], max_length=10, verbose_name='Can you straighten your knee fully?')),
                ('s5_symptoms', models.CharField(choices=[('always', 'Always'), ('often', 'Often'), ('sometimes', 'Sometimes'), ('rarely', 'Rarely'), ('never', 'Never')], max_length=10, verbose_name='Can you bend your knee fully?')),
                ('s6_stiffness', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='How severe is your knee joint stiffness after first wakening in the morning?')),
                ('s7_stiffness', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='How severe is your knee stiffness after sitting, lying or resting later in the day?')),
                ('p1_pain', models.CharField(choices=[('never', 'Never'), ('monthly', 'Monthly'), ('weekly', 'Weekly'), ('daily', 'Daily'), ('always', 'Always')], max_length=10, verbose_name='How often do you experience knee pain?')),
                ('p2_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week during twisting/pivoting on your knee?')),
                ('p3_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week during straightening your knee fully?')),
                ('p4_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week during bending your knee fully?')),
                ('p5_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week walking on a flat surface?')),
                ('p6_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week going up or down stairs?')),
                ('p7_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week at night while in bed?')),
                ('p8_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week sitting or lying?')),
                ('p9_pain', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='What amount of knee pain have you experienced the last week standing upright?')),
                ('a1_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Descending stairs')),
                ('a2_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Ascending stairs')),
                ('a3_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Rising from sitting')),
                ('a4_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Standing')),
                ('a5_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Bending to the floor or picking up an object')),
                ('a6_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Walking on a flat surface')),
                ('a7_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Getting in or out of a car')),
                ('a8_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Goign shopping')),
                ('a9_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Putting on socks or stockings')),
                ('a10_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Rising from bed')),
                ('a11_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Taking off socks or stockings')),
                ('a12_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Lying in bed (turning over, maintaining knee position)')),
                ('a13_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Getting in or out of the bath')),
                ('a14_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Sitting')),
                ('a15_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Getting on or off the toilet')),
                ('a16_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Heavy domestic duties (moving heavy boxes, scrubbing floors, etc)')),
                ('a17_function', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Light domestic duties (cooking, dusting, etc)')),
                ('sp1_exercise', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Squatting')),
                ('sp2_exercise', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Running')),
                ('sp3_exercise', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Jumping')),
                ('sp4_exercise', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Twisting/pivoting on your injured knee')),
                ('sp5_exercise', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='Kneeling')),
                ('q1_qol', models.CharField(choices=[('never', 'Never'), ('monthly', 'Monthly'), ('weekly', 'Weekly'), ('daily', 'Daily'), ('constantly', 'Constantly')], max_length=10, verbose_name='How often are you aware of your knee problem?')),
                ('q2_qol', models.CharField(choices=[('not at all', 'Not at All'), ('mildly', 'Mildly'), ('moderately', 'Moderately'), ('severely', 'Severely'), ('totally', 'Totally')], max_length=10, verbose_name='Have you modified your life style to avoid potentially damaging activities to your knee?')),
                ('q3_qol', models.CharField(choices=[('not at all', 'Not at All'), ('mildly', 'Mildly'), ('moderately', 'Moderately'), ('severely', 'Severely'), ('extremely', 'Extremely')], max_length=10, verbose_name='How much are you troubled with lack of confidence in your knee?')),
                ('q4_qol', models.CharField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderately', 'Moderately'), ('severe', 'Severe'), ('extreme', 'Extreme')], max_length=10, verbose_name='In general, how much difficulty do you have with your knee?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
