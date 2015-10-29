# It validates data type properties of all variable in contract

from datetime import date

class dataType_validation:
    
    STATE = None

    def __init__(self, city, country, bidderLimit, netAmount, netAmountEur, unitPrice, unitNumber, 
                 minPrice, maxPrice, lotNumber, bidsCount, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate,
                 parentContractAwardDate, estimatedStartDate, estimatedCompletionDate, awardDecisionDate,
                 completionDate, cancellationDate, signatureDate, paymentD):
        self.city=city
        self.country=country
        self.bidderLimit=bidderLimit
        self.netAmount=netAmount
        self.netAmountEur=netAmountEur
        self.unitPrice=unitPrice
        self.unitNumber=unitNumber
        self.minPrice=minPrice
        self.maxPrice=maxPrice
        self.lotNumber=lotNumber
        self.bidsCount=bidsCount
        self.callForTendersPublicationDate=callForTendersPublicationDate
        self.bidDeadlineDate=bidDeadlineDate
        self.contractAwardNoticePublicationDate=contractAwardNoticePublicationDate
        self.parentContractAwardDate=parentContractAwardDate
        self.estimatedStartDate=estimatedStartDate
        self.estimatedCompletionDate=estimatedCompletionDate
        self.awardDecisionDate=awardDecisionDate
        self.completionDate=completionDate
        self.cancellationDate=cancellationDate
        self.signatureDate=signatureDate
        self.paymentD=paymentD

    #checking data types for the contracts variable    
    def dataType_check(self):
        
        self.STATE = True
        
        for x in (self.bidderLimit, self.unitNumber, self.lotNumber, self.bidsCount):
            if x is not None and type(x) is not int:
                self.STATE = False
                
        for x in (self.netAmount, self.netAmountEur, self.unitPrice, self.minPrice, self.maxPrice):
            if x is not None and type(x) is not int and type(x) is not float:
                self.STATE = False
        if (type(self.city) is not str) or (type(self.country) is not str):
            self.STATE = False
        if (not self.city.isalpha()) or (not self.country.isalpha()):
            self.STATE = False
            
        for x in (self.callForTendersPublicationDate, self.bidDeadlineDate, self.contractAwardNoticePublicationDate, self.parentContractAwardDate, self.estimatedStartDate, 
                    self.estimatedCompletionDate, self.awardDecisionDate, 
                    self.completionDate, self.cancellationDate, 
                    self.signatureDate, self.paymentD):
            if x is not None and type(x) is not date:
                self.STATE = False
        return self.STATE
