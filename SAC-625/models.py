# models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    income = models.IntegerField()
    otp_authentication = models.BooleanField(default=False)

class BajajAllianzGroupSampoornaJeevanSuraksha(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    sum_assured = models.IntegerField()
    min_sum_assured = models.IntegerField()
    max_sum_assured = models.IntegerField()
    min_age_limit = models.IntegerField()
    max_age_limit = models.IntegerField()
    policy_tenure = models.IntegerField()
    sum_assured_50K = models.BooleanField(default=False)
    sum_assured_1lac = models.BooleanField(default=False)
    sum_assured_1_5lac = models.BooleanField(default=False)
    sum_assured_2lac = models.BooleanField(default=False)
    policy_tenure_12 = models.BooleanField(default=False)
    policy_tenure_15 = models.BooleanField(default=False)
    policy_tenure_18 = models.BooleanField(default=False)
    policy_tenure_24 = models.BooleanField(default=False)
    spouse_coverage = models.BooleanField(default=False)