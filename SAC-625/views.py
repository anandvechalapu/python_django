# views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def validate_policy(request):
    # minimum and maximum sum assured
    min_sum_assured = 0
    max_sum_assured = 50000

    # minimum and maximum age limits as defined for each product and master level.
    min_age_limit = 0
    max_age_limit = 80

    # annual income below 40K not eligible for insurance coverage 
    min_annual_income = 40000

    # Sum assured ranges of 50K, 1lac, 1.5 lac, and 2 lac to the Bandhan Bank sales personnel for selection.
    sum_assured_choices = [50000, 100000, 150000, 200000]

    # Policy tenure ranges of 12, 15, 18, and 24 months to the Bandhan Bank sales personnel for selection. 
    policy_tenure_choices = [12, 15, 18, 24]

    # If a member is not eligible for insurance coverage, their spouse will also not receive coverage.
    spouse_eligibility = False

    # The system should not provide insurance coverage to the member if the OTP authentication is not received from the Bandhan Bank sales personnel.
    otp_authentication_required = True

    context = {'min_sum_assured': min_sum_assured, 'max_sum_assured': max_sum_assured,
               'min_age_limit': min_age_limit, 'max_age_limit': max_age_limit,
               'min_annual_income': min_annual_income, 'sum_assured_choices': sum_assured_choices,
               'policy_tenure_choices': policy_tenure_choices, 'spouse_eligibility': spouse_eligibility,
               'otp_authentication_required': otp_authentication_required}

    return render(request, 'validate_policy.html', context)