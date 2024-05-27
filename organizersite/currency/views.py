from django.shortcuts import render
from django.http import HttpResponse
from currency import forms
import requests
import json
from django.contrib.auth.decorators import login_required

# # Create your views here.

# def convert_currency(request):
#     ''' convert the given amount to target country amount'''
    
#     # calling API using requests lib
#     api_request = requests.get("http://data.fixer.io/api/latest?access_key=40eac7a32ba84e0369830d99248246b7")
#     currency_dict = json.loads(api_request.text)

#     currency_rates_dict = currency_dict['rates']
#     list_of_country_currency_code = [x for x in currency_rates_dict.keys()]
#     tuple_of_country_codes = [tuple([x,x]) for x in list_of_country_currency_code]
    
#     # initialize form with country currency code
#     currency_form = forms.CurrencyForm(tuple_of_country_codes,request.POST or None)

#     converted_currency = ""
#     if request.method == "POST":
#         # check sanitation
#         if currency_form.is_valid():

#             # values from the html input fields
#             source_currency_code = currency_form.cleaned_data['source_currency_code']
#             target_currency_code = currency_form.cleaned_data['target_currency_code']
#             input_currency_value = currency_form.cleaned_data['source_currency_value']

#             # get live amount of selected country 
#             from_country_base_value = currency_rates_dict[source_currency_code]
#             to_country_base_value = currency_rates_dict[target_currency_code]
            
#             # logic to calculate the converted_currency
#             converted_currency = (to_country_base_value / from_country_base_value) * float(input_currency_value)

#             return render(request, 'currency-index.html', {'currency_form':currency_form, 'converted_currency':converted_currency})

#     # form initialization
#     context = {
#         'currency_form': currency_form,
#         'converted_currency':converted_currency
#     }
#     return render(request, 'currency/currency-index.html', context)

CURRENCY_API_KEY = 'cur_live_Xhx9MoYu5SqEqtFiDvXYKha4BKijFzUEU6TvHhQ6'
@login_required(login_url='login')
def convert_currency(request):
    ''' convert the given amount to target country amount'''
    converted_currency = ""
    currency_form = forms.CurrencyForm(request.POST or None)
    if request.method == "POST":
        currency_form = forms.CurrencyForm(request.POST or None)
        if currency_form.is_valid():
            source_currency_code = currency_form.cleaned_data['source_currency_code']
            target_currency_code = currency_form.cleaned_data['target_currency_code']
            input_currency_value = currency_form.cleaned_data['source_currency_value']
            api_url = f'https://api.currencyapi.com/v3/convert?value={input_currency_value}&from={source_currency_code}&to={target_currency_code}&apikey={CURRENCY_API_KEY}'
            api_request = requests.get(api_url)
            if api_request.status_code == 200:
                data = api_request.json()
                converted_currency = data['result'][0]['converted_value']
            else:
                converted_currency = "Error: API request failed."
    context = {
        'currency_form': currency_form,
        'converted_currency': converted_currency
    }
    return render(request, 'currency-index.html', context)