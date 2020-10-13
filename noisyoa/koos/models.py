from django.db import models
from model_utils.models import TimeStampedModel

from noisyoa.users.models import User


# Create your models here.
class Survey(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Koos(Survey):
    class Negative_frequencies(models.TextChoices):
        NEVER = "never", "Never"
        RARELY = "rarely", "Rarely"
        SOMETIMES = "sometimes", "Sometimes"
        OFTEN = "often", "Often"
        ALWAYS = "always", "Always"

    class Positive_frequencies(models.TextChoices):
        ALWAYS = "always", "Always"
        OFTEN = "often", "Often"
        SOMETIMES = "sometimes", "Sometimes"
        RARELY = "rarely", "Rarely"
        NEVER = "never", "Never"

    class Time_frequencies(models.TextChoices):
        NEVER = "never", "Never"
        MONTHLY = "monthly", "Monthly"
        WEEKLY = "weekly", "Weekly"
        DAILY = "daily", "Daily"
        ALWAYS = "always", "Always"

    class Severity(models.TextChoices):
        NONE = "none", "None"
        MILD = "mild", "Mild"
        MODERATE = "moderate", "Moderate"
        SEVERE = "severe", "Severe"
        EXTREME = "extreme", "Extreme"

    class Awareness(models.TextChoices):
        NEVER = "never", "Never"
        MONTHLY = "monthly", "Monthly"
        WEEKLY = "weekly", "Weekly"
        DAILY = "daily", "Daily"
        CONSTANTLY = "constantly", "Constantly"

    class Modifications(models.TextChoices):
        NOTATALL = "not at all", "Not at All"
        MILDLY = "mildly", "Mildly"
        MODERATELY = "moderately", "Moderately"
        SEVERELY = "severely", "Severely"
        TOTALLY = "totally", "Totally"

    class Confidence(models.TextChoices):
        NOTATALL = "not at all", "Not at All"
        MILDLY = "mildly", "Mildly"
        MODERATELY = "moderately", "Moderately"
        SEVERELY = "severely", "Severely"
        EXTREMELY = "extremely", "Extremely"

    class Difficulty(models.TextChoices):
        NONE = "none", "None"
        MILD = "mild", "Mild"
        MODERATELY = "moderately", "Moderately"
        SEVERE = "severe", "Severe"
        EXTREME = "extreme", "Extreme"

    """SYMPTOMS"""

    s1_symptoms = models.CharField(
        "Do you have swelling in your knee?",
        max_length=10,
        choices=Negative_frequencies.choices,
    )

    s2_symptoms = models.CharField(
        "Do you feel grinding, hear clicking or any other type of noise when your knee moves?",
        max_length=10,
        choices=Negative_frequencies.choices,
    )

    s3_symptoms = models.CharField(
        "Does your knee catch or hang up when moving?",
        max_length=10,
        choices=Negative_frequencies.choices,
    )

    s4_symptoms = models.CharField(
        "Can you straighten your knee fully?",
        max_length=10,
        choices=Positive_frequencies.choices,
    )

    s5_symptoms = models.CharField(
        "Can you bend your knee fully?",
        max_length=10,
        choices=Positive_frequencies.choices,
    )

    """STIFFNESS"""

    s6_stiffness = models.CharField(
        "How severe is your knee joint stiffness after first wakening in the morning?",
        max_length=10,
        choices=Severity.choices,
    )

    s7_stiffness = models.CharField(
        "How severe is your knee stiffness after sitting, lying or resting later in the day?",
        max_length=10,
        choices=Severity.choices,
    )

    """PAIN"""

    p1_pain = models.CharField(
        "How often do you experience knee pain?",
        max_length=10,
        choices=Time_frequencies.choices,
    )

    p2_pain = models.CharField(
        "What amount of knee pain have you experienced the last week during twisting/pivoting on your knee?",
        max_length=10,
        choices=Severity.choices,
    )

    p3_pain = models.CharField(
        "What amount of knee pain have you experienced the last week during straightening your knee fully?",
        max_length=10,
        choices=Severity.choices,
    )

    p4_pain = models.CharField(
        "What amount of knee pain have you experienced the last week during bending your knee fully?",
        max_length=10,
        choices=Severity.choices,
    )

    p5_pain = models.CharField(
        "What amount of knee pain have you experienced the last week walking on a flat surface?",
        max_length=10,
        choices=Severity.choices,
    )

    p6_pain = models.CharField(
        "What amount of knee pain have you experienced the last week going up or down stairs?",
        max_length=10,
        choices=Severity.choices,
    )

    p7_pain = models.CharField(
        "What amount of knee pain have you experienced the last week at night while in bed?",
        max_length=10,
        choices=Severity.choices,
    )

    p8_pain = models.CharField(
        "What amount of knee pain have you experienced the last week sitting or lying?",
        max_length=10,
        choices=Severity.choices,
    )

    p9_pain = models.CharField(
        "What amount of knee pain have you experienced the last week standing upright?",
        max_length=10,
        choices=Severity.choices,
    )

    """FUNCTION, DAILY LIVING"""

    a1_function = models.CharField(
        "Descending stairs", max_length=10, choices=Severity.choices
    )

    a2_function = models.CharField(
        "Ascending stairs", max_length=10, choices=Severity.choices
    )

    a3_function = models.CharField(
        "Rising from sitting", max_length=10, choices=Severity.choices
    )

    a4_function = models.CharField("Standing", max_length=10, choices=Severity.choices)

    a5_function = models.CharField(
        "Bending to the floor or picking up an object",
        max_length=10,
        choices=Severity.choices,
    )

    a6_function = models.CharField(
        "Walking on a flat surface", max_length=10, choices=Severity.choices
    )

    a7_function = models.CharField(
        "Getting in or out of a car", max_length=10, choices=Severity.choices
    )

    a8_function = models.CharField(
        "Goign shopping", max_length=10, choices=Severity.choices
    )

    a9_function = models.CharField(
        "Putting on socks or stockings", max_length=10, choices=Severity.choices
    )

    a10_function = models.CharField(
        "Rising from bed", max_length=10, choices=Severity.choices
    )

    a11_function = models.CharField(
        "Taking off socks or stockings", max_length=10, choices=Severity.choices
    )

    a12_function = models.CharField(
        "Lying in bed (turning over, maintaining knee position)",
        max_length=10,
        choices=Severity.choices,
    )

    a13_function = models.CharField(
        "Getting in or out of the bath", max_length=10, choices=Severity.choices
    )

    a14_function = models.CharField("Sitting", max_length=10, choices=Severity.choices)

    a15_function = models.CharField(
        "Getting on or off the toilet", max_length=10, choices=Severity.choices
    )

    a16_function = models.CharField(
        "Heavy domestic duties (moving heavy boxes, scrubbing floors, etc)",
        max_length=10,
        choices=Severity.choices,
    )

    a17_function = models.CharField(
        "Light domestic duties (cooking, dusting, etc)",
        max_length=10,
        choices=Severity.choices,
    )

    """FUNCTION, SPORTS AND RECREATIONAL ACTIVITIES"""

    sp1_exercise = models.CharField(
        "Squatting", max_length=10, choices=Severity.choices
    )

    sp2_exercise = models.CharField("Running", max_length=10, choices=Severity.choices)

    sp3_exercise = models.CharField("Jumping", max_length=10, choices=Severity.choices)

    sp4_exercise = models.CharField(
        "Twisting/pivoting on your injured knee",
        max_length=10,
        choices=Severity.choices,
    )

    sp5_exercise = models.CharField("Kneeling", max_length=10, choices=Severity.choices)

    """QUALITY OF LIFE"""

    q1_qol = models.CharField(
        "How often are you aware of your knee problem?",
        max_length=10,
        choices=Awareness.choices,
    )

    q2_qol = models.CharField(
        "Have you modified your life style to avoid potentially damaging activities to your knee?",
        max_length=10,
        choices=Modifications.choices,
    )

    q3_qol = models.CharField(
        "How much are you troubled with lack of confidence in your knee?",
        max_length=10,
        choices=Confidence.choices,
    )

    q4_qol = models.CharField(
        "In general, how much difficulty do you have with your knee?",
        max_length=10,
        choices=Difficulty.choices,
    )

    # koos_patient_id = User.patient_id

    # class Meta:
    # app_label = "noisyoa.koos"

    def __str__(self):
        return self.user.username + str("'s KOOS")


class Koos_ps(Survey):
    class Severity(models.TextChoices):
        NONE = "none", "None"
        MILD = "mild", "Mild"
        MODERATE = "moderate", "Moderate"
        SEVERE = "severe", "Severe"
        EXTREME = "extreme", "Extreme"

    """FUNCTION, DAILY LIVING"""

    a3_function = models.CharField(
        "Rising from sitting", max_length=10, choices=Severity.choices
    )

    a5_function = models.CharField(
        "Bending to the floor or picking up an object",
        max_length=10,
        choices=Severity.choices,
    )

    a9_function = models.CharField(
        "Putting on socks or stockings", max_length=10, choices=Severity.choices
    )

    a10_function = models.CharField(
        "Rising from bed", max_length=10, choices=Severity.choices
    )

    """FUNCTION, SPORTS AND RECREATIONAL ACTIVITIES"""

    sp1_exercise = models.CharField(
        "Squatting", max_length=10, choices=Severity.choices
    )

    sp4_exercise = models.CharField(
        "Twisting/pivoting on your injured knee",
        max_length=10,
        choices=Severity.choices,
    )

    sp5_exercise = models.CharField("Kneeling", max_length=10, choices=Severity.choices)

    def cum_calculator(self):
        def comp_score(field):
            score = 0
            if field == "none":
                score = 0
            if field == "mild":
                score = 1
            if field == "moderate":
                score = 2
            if field == "Severe":
                score = 3
            if field == "Extreme":
                score = 4
            return score

        cum_score = (
            self.comp_score(self.a3_function)
            + self.comp_score(self.a5_function)
            + self.comp_score(self.a9_function)
            + self.comp_score(self.a10_function)
            + self.comp_score(self.sp1_exercise)
            + self.comp_score(self.sp4_exercise)
            + self.comp_score(self.sp5_exercise)
        )

        return cum_score

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # total_score = str(self.cum_calculator())

    # koos_patient_id = User.patient_id

    # def __str__(self):
    # return str(self.cum_calculator())
