from django import forms


class DataConfigForm(forms.Form):
    datafile = forms.FileField(
        label='Select a data file'
    )

    configfile = forms.FileField(
        label='Select a config file'
    )
