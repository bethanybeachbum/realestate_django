from django.shortcuts import render, redirect
from realestate_app.models import ContractAction, Contract, Person, Closing
from django.http import HttpResponse
from django.template import loader
from .forms import ContractForm, ContractActionForm


# Create your views here.
"""When a URL request matches the pattern we just defined, Django looks for a function called index() in view.py.  Django then passes the request object to this view function.  """


def index(request):
    """The home page for realestate_app """

    # Generate counts for some of the main objects
    num_contracts = Contract.objects.all().count()
    num_actions = ContractAction.objects.all().count()
    num_unclosed_contracts = Contract.objects.filter(closedYesNo__exact="No").count()
    num_persons = Person.objects.all().count()
    num_closed_contracts = Closing.objects.all().count()

    context = {
        'num_contracts' : num_contracts,
        'num_actions' : num_actions,
        'num_unclosed_contracts' : num_unclosed_contracts,
        'num_persons' : num_persons,
        'num_closed_contracts' : num_closed_contracts,
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
    """Show details of one contract 
    Case contract number is a specific one
    """
    context = {'contract': contract}
    return render(request, 'realestate_app/contract/int:<id>.html' )

def actions(request):
    """Show all actions"""
    actions = ContractAction.objects.order_by('AddDate')
    context = {'actions': actions}
    return render(request, 'realestate_app/actions.html', context)

def action(request, contractaction_id):
    """Show details for one action """
    action = ContractAction.objects.order_by('AddDate')
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

def closings(request):
    """Show closings """
    action = Closing.objects.order_by('createDate')
    context = {'closings': closings}
    return render(request, 'realestate_app/closings.html' )

def closing(request, closing_id):
    """Show one closing """
    action = Closing.objects.order_by('createDate')
    context = {'closing': closing}
    return render(request, 'realestate_app.closings/int<id>.html' )

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
    return render(request, 'realestate_app/new_contractaction.html', context)    

def new_action(request, contract_id):
    contract_action = ContractAction.objects.get(id=contract_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = ContractActionForm()
    else:
        # POST data submitted, process data.
        form = ContractActionForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.contract_action = contract_action
            new_entry.save()
            return redirect('realestate_app:contract', 
            id = id)
            # contract_id=contract_id)
        
    # Display a blank or invalid form.
    context = {'contract': contract, 
               'form': form
               }
    return render( request, 'realestate_app/new_contractaction.html', context)

def about(request):
    
    return HttpResponse('<h2> About Real Deal </h2>')   

