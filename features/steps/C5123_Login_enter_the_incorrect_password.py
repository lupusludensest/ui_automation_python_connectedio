from behave import *

@then('Enter valid, and the correct email address in the line "Email address" {email}')
def entr_vld_wrng_eml(context, email):
    """
    Enter valid, and the correct email address in the line "Email address" vadim@mailinator.com
    """
    context.app.main_page.entr_vld_wrng_eml(email)

@then('Enter the valid but incorrect password in the line "Password" {pswd}')
def entr_vld_crct_pswd(context, pswd):
    """
    Enter the valid but incorrect password in the line "Password" manicpiano731_wrong
    """
    context.app.main_page.entr_vld_crct_pswd(pswd)
