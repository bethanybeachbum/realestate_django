from django import forms

from .models import Contract, ContractAction

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['seller', 
                  'buyer', 
                  'listingAgent',
                  'buyingAgent',
                  'price',
                  'propertyAddress',
                  'contractPDF',
                  'contractDate',
                  'mortgage',
                  'mortgageAmount',
                  'escrowAmount',
                  'closedYesNo',
                  'comments',
                  'propertyAddress']
        labels = {'text': ''}
        
class ContractActionForm(forms.ModelForm):
    class Meta:
        model = ContractAction
        fields= [ 'action',
                  'actionPerson',
                  'actionCompany', 
                  'actionNextStep',
                   'actionFee',
                   'actionDueDate',
                ]
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}