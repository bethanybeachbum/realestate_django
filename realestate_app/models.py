from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Contract(models.Model):
    CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    seller = models.CharField(max_length=30, help_text="Enter Seller's Name")
    buyer = models.CharField(max_length=30, help_text="Enter Buyer's Name")
    listingAgent = models.CharField(max_length=30, help_text="Enter Listing Agent")
    buyingAgent = models.CharField(max_length=30, help_text="Enter Buying Agent")
    price = models.PositiveBigIntegerField(help_text="Enter Price")
    propertyAddress = models.CharField(max_length=30, help_text="Enter Property Addresss")
    contractPDF = models.FileField(upload_to='', help_text="Attach Contract",blank=True, null=True)
    contractDate = models.DateTimeField(default=timezone.now, help_text="Enter Date of Contract")
    # contractDate = models.DateField(auto_now=True, null=True, help_text="Enter Date of Contract")
    mortgage = models.CharField(max_length=30, default="Y", choices = CHOICES, help_text="Is there a mortgage?")
    mortgageAmount = models.PositiveBigIntegerField(default=0, help_text= "Enter Mortgage Amount")
    escrowAmount = models.PositiveBigIntegerField(help_text= "Enter Escrow Amount")
    closedYesNo = models.CharField(max_length=30, default = "No", choices = CHOICES, help_text= "Has the contract closed?" )
    comments = models.TextField(help_text = "Enter pertinent information")
    AddDate = models.DateField(auto_now_add=True, null=True, verbose_name="created at")
    updatedAt = models.DateField(auto_now=True, verbose_name="updated at")

    class Meta:
        ordering = ["propertyAddress"]

    def __str__(self):
        """Return a string representation of the model."""
        return self.propertyAddress

class Closing(models.Model):
    finalClosing = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    createDate = models.DateField(auto_now_add=True, null=True, verbose_name="created at")
    closeDate = models.DateField(null = True)
    closingDocumentsPDF = models.FileField(upload_to='', help_text = "Attach closing documents", blank=True, null=True)
    comments = models.TextField(help_text = "Enter Pertinent Documents")

    class Meta:
        verbose_name = "Final Closing"

    def __str__(self):
        """Return a string representation of the model."""
        return self.comments
        

class Person(models.Model):
    contracts = models.ManyToManyField(Contract)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email =  models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, null=True)
    zip = models.CharField(max_length=10)
    role = models.CharField(max_length=10)

    def __str__(self):
        """Return a string representation of the model."""
        return self.first_name

class ContractAction(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=30)
    actionPerson = models.CharField(max_length=30)
    actionCompany = models.CharField(max_length=30)
    actionNextStep = models.CharField(max_length=30)
    actionFee = models.CharField(max_length=30)
    actionDueDate = models.DateField(null=True, default='',)
    AddDate = models.DateTimeField(auto_now_add=True, null=True, verbose_name="created at")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="updated at")

    # start_date = models.DateField(null = True)
    # end_date = models.DateField(null = True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.action
    




"""
    inspector = models.CharField(max_length=30)
    inspectionCompany = models.CharField(max_length=30)
    surveyor = models.CharField(max_length=30)
    surveyCompany = models.CharField(max_length=30)
    titleSearchContact = models.CharField(max_length=30)
    titleSearchCompany = models.CharField(max_length=30)
    termiteInspector = models.CharField(max_length=30)
    termitePestInspectionCompany = models.CharField(max_length=30)
    titleInsuranceContact = models.CharField(max_length=30)
    titleInsuranceCompany = models.CharField(max_length=30)
    lawyer = models.CharField(max_length=30)
    lawFirm =models.CharField(max_length=30)
    mortgageLoanOfficer = models.CharField(max_length=30)
    mortgageCompany = models.CharField(max_length=30)
    moldInspector = models.CharField(max_length=30)
    moldCompany = models.CharField(max_length=30)
    radonInspector = models.CharField(max_length=30)
    radonCompany = models.CharField(max_length=30)
    handyMan = models.CharField(max_length=30)
    handyManCompany = models.CharField(max_length=30)
    other1_person = models.CharField(max_length=30)
    other1_Company = models.CharField(max_length=30)
    other2_person = models.CharField(max_length=30)
    other2_Company = models.CharField(max_length=30)
    other2_person = models.CharField(max_length=30)
    other2_Company = models.CharField(max_length=30)

    """
