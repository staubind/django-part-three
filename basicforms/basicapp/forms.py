from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput
from django.core import validators

# creating our own validator - say that standard validators don't cover our case
# and that we don't want to use a clean_<field_name> function
def check_for_z(value): # value cues django to know it is a validator
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")
    # now we can pass this as a validator

# now what if you want something that cleans and validates everything?



class FormName(forms.Form):
    name = forms.CharField() # pass to char field: validators=[check_for_z] to do validation for z
    email = forms.EmailField()
    # verifying email
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    # hidden fields remain in html but are hidden from user
    # can be used for basic bot catching
    botcatcher = forms.CharField(required=False,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)]) 
    # set hiddeninput to hide it from typical human users
    # of course this assumes the bots aren't written in a more intelligent manner, where they ignore hidden fields

    # cleaning the botcatcher manually - django looks for clean_fieldname methods to use
    # we will end up using the built in validators more often than not.
    # instead of using teh def clean_botcatcher code snippet below,
    # we will import from django.core validators
    # def clean_botcatcher(self):
    #     # bind the cleaned field value to botcatcher
    #     botcatcher = self.cleaned_data['botcatcher']
    #     # if its length is more than 0 we have data, so...
    #     if len(botcatcher) > 0:
    #         # this actually gets displayed on the page, the validation error.
    #         # it tells you which field, if it was Hidden, and the name of the field
    #         raise forms.ValidationError("GOTCHA, BOT!")
    #     return botcatcher

    # to clean the entire form at once, just define a function clean:
    def clean(self):
        # allows us to grab all of the clean data at once
        all_clean_data = super().clean()
        # grab specific fields:
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Make sure emails match.")