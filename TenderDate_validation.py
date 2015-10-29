# This validates date properties of Tenders.

class TenderDate_validation:

    STATE=None

    # It takes arguments such as callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate, and parentContractAwardDate
    
    def __init__(self, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate, parentContractAwardDate):
        self.callForTendersPublicationDate=callForTendersPublicationDate
        self.bidDeadlineDate=bidDeadlineDate
        self.contractAwardNoticePublicationDate=contractAwardNoticePublicationDate
        self.parentContractAwardDate=parentContractAwardDate
       
        
    def Tender_Calling_Date_Contract_Award_Date(self):
        'Rule: validating if Contract_Award_Date (Schema ID: parentContractAwardDate)  is later than the Tender_Calling_Date (Schema ID: callForTendersPublicationDate)'
        if self.parentContractAwardDate is not None and self.callForTendersPublicationDate is not None and self.parentContractAwardDate > self.callForTendersPublicationDate:
            TenderDate_validation.STATE=True
            return TenderDate_validation.STATE
        else:
            TenderDate_validation.STATE=False
            return TenderDate_validation.STATE
            
            
    def Tender_Calling_Date_bidDeadlineDate(self):
        'Rule: validating if bidDeadlineDate (Schema ID: bidDeadlineDate) is later than the Tender_Calling_Date'    
        if self.bidDeadlineDate is not None and self.callForTendersPublicationDate is not None and self.bidDeadlineDate > self.callForTendersPublicationDate:
            TenderDate_validation.STATE=True
            return TenderDate_validation.STATE
        else:
            TenderDate_validation.STATE=False
            return TenderDate_validation.STATE
    
    
    def Tender_Calling_Date_Award_Notice_Date(self):
        'Rule: validating if Award_Notice_Date (Schema ID: contractAwardNoticePublicationDate) is later than the Tender_Calling_Date'
        if self.contractAwardNoticePublicationDate is not None and self.callForTendersPublicationDate is not None and self.contractAwardNoticePublicationDate > self.callForTendersPublicationDate:
            TenderDate_validation.STATE=True
            return TenderDate_validation.STATE
        else:
            TenderDate_validation.STATE=False
            return TenderDate_validation.STATE
                
