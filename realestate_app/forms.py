from django import forms

from .models import Contract, Action, ContractDetail

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
        
class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields= [ 'action',
                  'actionPerson',
                  'actionCompany', 
                  'actionNextStep',
                   'actionFee',
                   'actionDueDate',
                ]
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}