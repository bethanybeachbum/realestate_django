from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Contract(models.Model):
    
    seller = models.CharField(max_length=30, help_text="Enter Seller's Name")
    buyer = models.CharField(max_length=30, help_text="Enter Buyer's Name")
    listingAgent = models.CharField(max_length=30, help_text="Enter Listing Agent")
    buyingAgent = models.CharField(max_length=30, help_text="Enter Buying Agent")
    price = models.PositiveBigIntegerField(help_text="Enter Price")
    contractDate = models.DateTimeField(default=timezone.now, help_text="Enter Date of Contract")
    propertyAddress = models.CharField(max_length=30, help_text="Enter Property Addresss")
    AddDate = models.DateField(auto_now_add=True, null=True, verbose_name="created at")
    
    class Meta:
        ordering = ["seller"]

    def __str__(self):
        """Return a string representation of the model."""
        return self.seller

class ContractDetail(models.Model):
    CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    contractPDF = models.FileField(upload_to='contracts/%Y/%m/%d',help_text="Attach Contract",blank=True, null=True)
    mortgage = models.CharField(max_length=30, default="Y", choices = CHOICES, help_text="Is there a mortgage?")
    mortgageAmount = models.PositiveBigIntegerField(default=0, help_text= "Enter Mortgage Amount")
    escrowAmount = models.PositiveBigIntegerField(help_text= "Enter Escrow Amount")
    closedContract = models.BooleanField(default=False)
    comments = models.TextField(help_text = "Enter pertinent information")
    updatedAt = models.DateField(auto_now=True, verbose_name="updated at")
    closeDate = models.DateField(null = True, help_text="Expected close date:")
    closingDocumentsPDF = models.FileField(upload_to='closingdocs/%Y/%m/%d', help_text = "Attach closing documents", blank=True, null=True)
    closedContractComments = models.TextField(help_text="Final thoughts?")

    class Meta:
        ordering = ["comments"]
        verbose_name = "Contract Details"

    def __str__(self):
        """Return a string representation of the model."""
        return self.propertyAddress
        

class Person(models.Model):
    contracts = models.ManyToManyField(Contract)
    first_name = models.CharField(max_length=30, help_text="First Name")
    last_name = models.CharField(max_length=30,  help_text="Last Name")  
    title = models.CharField(max_length=30, help_text="Title")
    company = models.CharField(max_length=30,  help_text="Company")
    email =  models.EmailField(max_length=254,  help_text="Email")
    phone = models.CharField(max_length=30,  help_text="Phone")
    street = models.CharField(max_length=30,  help_text="Street")
    city = models.CharField(max_length=30,  help_text="City")
    state = models.CharField(max_length=30,  help_text="State")
    zip = models.CharField(max_length=10,  help_text="Zip Code")
    role = models.CharField(max_length=10,  help_text="What is this person's role?")

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Person Database"
        verbose_name_plural = "people"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.first_name} {self.last_name}"

class ContractAction(models.Model):
    ROLES = [
    ("Inspection", "Inspection"), 
    ("Survey", "Survey"),
    ("TitleSearch", "titleSearch"),
    ("TermiteInspection", "TermiteInspection"),
    ("TitleInsurance", "TitleInsurance"),
    ("Lawyer", "Lawyer"), 
    ("MortgageLoan", "MortgageLoan"),
    ("MoldInspection", "MoldInspection"),
    ("RadonInspection", "RadonInspection"), 
    ("HandyMan", "HandyMan"), 
    ("Other_Action_1", "Other_Action_1"),
    ("Other_Action_2", "Other_Action_2"), 
    ("Other_Action_3", "Other_Action_3")
]
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=30, help_text= "What is the specific action to be accomplished?", choices = ROLES)
    actionPerson = models.CharField(max_length=30, help_text="Person assigned")
    actionCompany = models.CharField(max_length=30, help_text="Person's company")
    actionNextStep = models.CharField(max_length=30)
    actionFee = models.CharField(max_length=30, help_text="Fee")
    actionDueDate = models.DateField(null=True, default='', help_text="Date due")
    AddDate = models.DateTimeField(auto_now_add=True, null=True, verbose_name="created at")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="updated at")


    def __str__(self):
        """Return a string representation of the model."""
        return self.action
    




