from django import forms

from .models import Contract, ContractAction, ContractDetail

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['seller', 
                  'buyer', 
                  'listingAgent',
                  'buyingAgent',
                  'price',
                  'propertyAddress',
                  'contractDate',
                  ]
        labels = {'text': ''}

class ContractDetailForm(forms.ModelForm):
    class Meta:
        model = ContractDetail
        fields = [
                  'contractPDF',
                  'mortgage',
                  'mortgageAmount',
                  'escrowAmount',
                  'closedContract',
                  'comments',
                  ]
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