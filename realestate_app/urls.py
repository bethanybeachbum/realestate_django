"""Defines URL patterns for realestate_app"""

# Import the path function needed when mapping URLs to views
from django.urls import path, include

# Import views model.  Dot tells Pyton to import from same dir
from . import views
app_name = 'realestate_app'

    
"""  
1. The first argument is a string that helps Django route the current request properly.
Django receives the requested URL and tries to route the the request to a view.
It does this by searching all the URL patterns we've defined to find one that matches 
the current request.
Django ignores the base URL for the project (http://localhost:8000/), so the empty string 
matches the base URL.
2. The second arg in path() specifies which function to call in view.py
3. The third arg provides the name 'index' for this URL pattern so we can refer to it in other
code sections. We can provide this name rather than writing out the URL to refer to home page. """
    
urlpatterns = [
   
    # Home page  
    # /realestate_app
    path('', views.index, name='index'),

    # About page
    path('about/', views.about, name='about'),

    # /realestate_app/contracts
    path('contracts/', views.contracts, name='contracts'),

    # /realestate_app/contract/<id>
    path('contracts/<int:id>', views.contracts, name='contract'),

    # /realestate_app/actions
    path('actions/', views.actions, name='actions'),

    # /realestate_app/actions/<id>
    path('actions/<int:contractAction_id>', views.action, name='action'),

    # /realestate_app/persons
    path('persons/', views.persons, name='persons'),

    # /realestate_app/persons/<id>
    path('persons/<int:person_id>', views.person, name='person'),

    # /realestate_app/closings
    path('closings/', views.closings, name='closings'),

    # /realestate_app/closings/<id>
    path('closings/<int:closing_id>', views.closing, name='closing'),

    # FORMS
    # Page for adding new contract
    # this URL pattern sends requests to the view function new_topic()
    path('new_contract/', views.new_contract, name='new_contract' ),
   
    # Page for adding new action
    path('new_action/<int:contract_id>/', views.new_action, name='new_action' ),

 
   
]

 
