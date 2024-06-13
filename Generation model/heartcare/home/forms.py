from django import forms

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

BIN_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
)

class InputForm(forms.Form):
    Age = forms.FloatField(label='Age')
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    ECG = forms.ChoiceField(choices=BIN_CHOICES, widget=forms.RadioSelect)
    CKMB = forms.ChoiceField(choices=BIN_CHOICES, widget=forms.RadioSelect)
    Trop_I = forms.ChoiceField(choices=BIN_CHOICES, widget=forms.RadioSelect)
    LAD = forms.FloatField(label='LAD')
    LCA = forms.FloatField(label='LCA')
    RCA = forms.FloatField(label='RCA')
    Systolic = forms.FloatField(label='Systolic')
    Diastolic = forms.FloatField(label='Diastolic')
    Chest_Pain = forms.ChoiceField(choices=BIN_CHOICES, widget=forms.RadioSelect)
    Diabetic = forms.ChoiceField(choices=BIN_CHOICES, widget=forms.RadioSelect)
    Cholestrol = forms.FloatField(label='Cholestrol')
    PHF = forms.ChoiceField(choices=BIN_CHOICES, widget=forms.RadioSelect)
    Add = forms.CharField(label='Add')