from django import forms 
from .models import LeaveApplication, LeaveList
from django.conf import settings


class LeaveApplicationForm(forms.ModelForm):
    reason = forms.CharField(
        min_length=20, max_length=255, required=True, widget=forms.TextInput(
            attrs = {
                'type': 'text',
                'class': 'employeeInput'
            }
        ))
    from_date = forms.DateField(
        widget = forms.DateInput(
            attrs = {
                'class':"form-control employeeInput",
                'type':"date"
            }
        )
    )
    to_date = forms.DateField(
        widget = forms.DateInput(
            attrs = {
                'class':"form-control employeeInput",
                'type':"date"
            }
        )
    )
    class Meta:
        model = LeaveApplication
        fields = [
            'reason',
            'from_date',
            'to_date'
        ]

class LeaveListForm(forms.ModelForm):
    from_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    to_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = LeaveList
        fields = [
            'user',
            'reason',
            'from_date',
            'to_date',
            'leave_status'
        ]