from django.db import models

# Create your models here.

class Contract(models.Model):
    contract_num = models.BigIntegerField()
    seller = models.CharField(max_length=30)
    buyer = models.CharField(max_length=30)
    listingAgent = models.CharField(max_length=30)
    buyingAgent = models.CharField(max_length=30) 
    price = models.PositiveBigIntegerField()
    propertyAddress = models.CharField(max_length=30)
    contractPDF = models.FileField(upload_to='')
    contractDate = models.DateField(auto_now_add=True)
    mortgage_or_cash = models.CharField(max_length=30)
    mortgageAmount =models.PositiveBigIntegerField()
    escrowAmount = models.PositiveBigIntegerField()
    closedYesNo = models.CharField(max_length=30)
    comments = models.TextField()

class ContractPartners(models.Model):
    contract_num = models.BigIntegerField()
    listingAgentCompany = models.CharField(max_length=30)
    sellingAgentCompany = models.CharField(max_length=30)
    appraiser = models.CharField(max_length=30)
    appraisalCompany = models.CharField(max_length=30)
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




class Transaction(models.Model):
    contract_num = models.BigIntegerField()
    closeDate = models.DateField(auto_now_add=True)
    propertyAddress = models.CharField(max_length=30)
    closingDocumentsPDF = models.FileField(upload_to='')
    comments = models.TextField()

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email =  models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
