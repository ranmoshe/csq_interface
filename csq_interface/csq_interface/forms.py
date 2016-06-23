from django import forms


class DataConfigForm(forms.Form):
    datafile = forms.FileField(
        label='Select a data file'
    )

    configfile = forms.FileField(
        label='Select a config file'
    )

    def __init__(self, *args, **kwargs):
        super(DataConfigForm, self).__init__(*args, **kwargs)
        self.fields['datafile'].widget.attrs.update({'class': 'fileUpload btn btn-primary'})
        self.fields['configfile'].widget.attrs.update({'class': 'fileUpload btn btn-primary'})
