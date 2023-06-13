from django.shortcuts import render, redirect
from realestate_app.models import Action, Contract, Person, ContractDetail
from django.http import HttpResponse
from .models import Contract, Action
from .forms import ContractForm, ActionForm

# Create your views here.
"""When a URL request matches the pattern we just defined, Django looks for a function called index() in view.py.  Django then passes the request object to this view function.  """

def index(request):
    """The home page for realestate_app """
    # Generate counts for some of the main objects
    num_contracts = Contract.objects.all().count()
    num_actions = Action.objects.all().count()
    num_persons = Person.objects.all().count()
   
    context = {
        'num_contracts' : num_contracts,
        'num_actions' : num_actions,
        'num_persons' : num_persons,
    }

    return render(request, 'realestate_app/index.html', context = context )

def contracts(request):
    """Show all contracts that are not closed 
    closedYesNo == No 
    """
    contracts = Contract.objects.order_by('AddDate')
    context = {'contracts': contracts}
    return render(request, 'realestate_app/contracts.html', context)

def contract(request, contract_id):
    """ Show a single contract and all its ACTIONS   """
    contract = Contract.objects.get(id=contract_id)
    actions = contract.action_set.order_by('action')
    context = {'contract': contract, 'actions': actions}
    return render(request, 'realestate_app/contract.html', context)

def contractlist(request):
    """List all contracts"""
    contractlist = Contract.objects.order_by('AddDate')
    context = {'contractlist': contractlist}
    return render(request, 'realestate_app/contractlist.html', context)

def contractdetail(request):
    """ Detail about real estate contract """
    contractdetail = ContractDetail.objects.order_by('mortgage')
    context = {'contractdetail': contractdetail}
    return render(request, 'realestate_app/contractdetail.html', context)

def actions(request):
    """Show all actions"""
    actions = Action.objects.order_by('action')
    context = {'actions': actions}
    return render(request, 'realestate_app/actions.html', context)

def action(request, contractaction_id):
    """Show details for one action """
    action = Action.objects.order_by('action')
    context = {'action': action}
    return render(request, 'realestate_app/action/int:<id>.html' )

def persons(request ):
    """Show all persons involved in one contract """
    action = Person.objects.order_by('last_name')
    context = {'persons': persons}
    return render(request, 'realestate_app/persons.html' )

def person(request, person_id):
    """Show all information on one person """
    action = Person.objects.order_by('last_name')
    context = {'person': person}
    return render(request, 'realestate_app/persons/int<id>.html' )


def new_contract(request):
    """Add a new contract"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ContractForm()
    else:
        # POST data submitted; process data.
        form = ContractForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('realestate_app:contracts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'realestate_app/new_contract.html', context)    


def new_action(request, contract_id):
    """Add a new action for a particular contract"""
    contract = Contract.objects.get(id=contract_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = ActionForm()
    else:
        # POST data submitted, process data.
        form = ActionForm(data=request.POST)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.contract = contract   #contract_action?
            new_action.save()
            return redirect('realestate_app:contract', contract_id=contract_id)
        
    # Display a blank or invalid form.
    context = {'contract': contract, 
               'form': form
               }
    return render( request, 'realestate_app/new_action.html', context)

""" 
1. When the edit_action page receive a GET request, the edit_action() function
returns a form for editing the entry.
2. When the pages receives a POST request with revised action text, it saves the
modified text into the database.  
"""
def edit_action(request, action_id):
    """ Edit an existing action . """
    action = Action.objects.get(id=action_id)
    contract = action.contract

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ActionForm(instance=action)
    else:
        # POST data submitted; prcoess data.
        form = ActionForm(instance=action, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('realestate_app:contract', action_id=action.id)
        
        context = {'action':action, 'contract':contract, 'form':form}
        return render(request, 'realestate_app/edit_action.html', context)


def about(request):
    
    return HttpResponse('<h2> About Real Deal </h2>')   

