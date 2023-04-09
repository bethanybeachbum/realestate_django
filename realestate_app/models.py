from django.db import models

# Create your models here.

class Contract(models.Model):
    contract_num = "AUTO ASSIGNED"
    seller = models.CharField(max_length=30)
    buyer = models.CharField(max_length=30)
    listingAgent = models.CharField(max_length=30)
    buyingAgent = models.CharField(max_length=30) 
    price = 
    propertyAddress = models.CharField(max_length=30)
    contractPDF = 
    contractDate = 
    mortgage_or_cash = 
    mortgageAmount =
    escrowAmount = 
    closedYesNo = 

class ContractPartners(models.Model):
    contract_num = "FROM CONTRACT.CONTRACT_NUM"
    listingAgentCompany,
	sellingAgentCompany,
    appraiser = 
	appraisalCompany,
    inspector = 
	inspectionCompany, 
    surveyor = 
	surveyCompany,
    titleSearchContact = 
	titleSearchCompany, 
    termiteInspector = 
	termitePestInspectionCompany,
    titleInsuranceContact = 
	titleInsuranceCompany
    lawyer = 
    lawFirm
    mortgageLoanOfficer = 
    mortgageCompany


class Transaction(models.Model):
    contract_num = "FROM CONTRACT.CONTRACT_NUM"
    closeDate =
    propertyAddress = models.CharField(max_length=30)
    closingDocumentsPDF =

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email =  
    phone = 
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
