from django import forms

choices=INTEGER_CHOICES = [('', '')]

# class CurrencyForm(forms.Form):
#     source_currency_value = forms.DecimalField(label='Amount')
#     source_currency_code = forms.CharField(label='From', widget = forms.Select(choices=INTEGER_CHOICES))
#     target_currency_code = forms.CharField(label='To', widget = forms.Select(choices=INTEGER_CHOICES))


#     def __init__(self, tuple_country_code, *args, **kwargs):
#         # required to set the initial form drop down with choices
#         self.tuple_country_code = tuple_country_code
#         super(CurrencyForm,self).__init__(*args, **kwargs)

#         self.fields['source_currency_code'].widget.choices = self.tuple_country_code
#         self.fields['target_currency_code'].widget.choices = self.tuple_country_code
class CurrencyForm(forms.Form):
    source_currency_code = forms.ChoiceField(label="From Currency", widget = forms.Select(choices=INTEGER_CHOICES))
    target_currency_code = forms.ChoiceField(label="To Currency", widget = forms.Select(choices=INTEGER_CHOICES))
    source_currency_value = forms.FloatField(label="Amount")

    def init(self, *args, **kwargs):
        super(CurrencyForm, self).init(*args, **kwargs)
        supported_currencies = self.get_currencies_from_database()
        self.fields['source_currency_code'].choices = [
            (code, code) for code in supported_currencies
        ]
        self.fields['target_currency_code'].widget.choices = self.fields['source_currency_code'].widget.choices

    def get_currencies_from_database(self):
        return ['USD', 'EUR', 'GBP', 'RUB', 'BYN']