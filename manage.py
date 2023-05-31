#!/usr/bin/env python

import sys

def validate_criteria(sum_assured, age, income, policy_tenure, otp):
    # Check if sum assured is within the range
    if sum_assured < 50_000 or sum_assured > 2_000_000:
        print("Sum assured is not within the range defined for the policy")
        return False

    # Check if age is within the range
    if age < 18 or age > 65:
        print("Age is not within the range defined for the policy")
        return False

    # Check if income is greater than 40K
    if income < 40_000:
        print("Income is not sufficient as per eligibility criteria")
        return False

    # Check if the policy tenure is within the range
    if policy_tenure not in [12, 15, 18, 24]:
        print("Policy tenure is not within the range defined for the policy")
        return False

    # Check OTP authentication
    if otp is None:
        print("OTP authentication failed")
        return False

    return True

def main(args):
    # Get the input from the user
    sum_assured = int(input("Enter sum assured: "))
    age = int(input("Enter age: "))
    income = int(input("Enter annual income: "))
    policy_tenure = int(input("Enter policy tenure: "))
    otp = input("Enter OTP: ")

    # Validate the criteria
    valid = validate_criteria(sum_assured, age, income, policy_tenure, otp)

    if valid:
        print("The Bajaj Allianz Group Sampoorna Jeevan Suraksha policy is issued")
    else:
        print("The Bajaj Allianz Group Sampoorna Jeevan Suraksha policy is not issued")

if __name__ == "__main__":
    main(sys.argv)