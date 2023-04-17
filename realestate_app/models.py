from django.db import models

# Create your models here.

class Contract(models.Model):
    seller = models.CharField(max_length=30, help_text="Enter Seller's Name")
    buyer = models.CharField(max_length=30, help_text="Enter Buyer's Name")
    listingAgent = models.CharField(max_length=30, help_text="Enter Listing Agent")
    buyingAgent = models.CharField(max_length=30, help_text="Enter Buying Agent")
    price = models.PositiveBigIntegerField(help_text="Enter Price")
    propertyAddress = models.CharField(max_length=30, help_text="Enter Property Addresss")
    contractPDF = models.FileField(upload_to='', help_text="Attach Contract",blank=True, null=True)
    contractDate = models.DateField(auto_now_add=True, help_text="Enter Date of Contract")
    mortgage_or_cash = models.CharField(max_length=30, help_text="Enter Mortgage or Cash")
    mortgageAmount = models.PositiveBigIntegerField( help_text= "Enter Mortgage Amount")
    escrowAmount = models.PositiveBigIntegerField(help_text= "Enter Escrow Amount")
    closedYesNo = models.CharField(max_length=30, help_text= "Has the contract closed? Enter 'Yes' or No' " )
    comments = models.TextField(help_text = "Enter pertinent information")

    class Meta:
        ordering = ["propertyAddress"]

    def __str__(self):
        """Return a string representation of the model."""
        return self.propertyAddress

class Closing(models.Model):
    finalClosing = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    closeDate = models.DateField(auto_now_add=True, help_text = "Enter Close Date")
    propertyAddress = models.CharField(max_length=30, help_text = "Enter Property Address")
    closingDocumentsPDF = models.FileField(upload_to='', help_text = "Attach closing documents", blank=True, null=True)
    comments = models.TextField(help_text = "Enter Pertinent Documents")

    def __str__(self):
        """Return a string representation of the model."""
        return self.closeDate

class Person(models.Model):
    # keyPerson = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
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
    actionDueDate = models.DateField(auto_now_add=True)


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
