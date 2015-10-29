from dataType_validation import dataType_validation
from LotDate_validation import LotDate_validation
from price_validation import price_validation
from TenderDate_validation import TenderDate_validation
import logging

# data validation messages will be printed in data_validation2 log file
logger = logging.getLogger()
hdlr = logging.FileHandler('data_validation2.log')
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

'''
(city, country, bidderLimit, netAmount, netAmountEur, unitPrice, unitNumber, 
                 minPrice, maxPrice, contract_no, lotNumber, bidsCount, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate,
                 parentContractAwardDate, estimatedStartDate, estimatedCompletionDate, awardDecisionDate,
                 completionDate, cancellationDate, signatureDate, paymentD)
'''

class data_validation:
      def __init__(self, city, country, bidderLimit, netAmount, netAmountEur, unitPrice, unitNumber, 
                 minPrice, maxPrice, lotNumber, bidsCount, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate,
                 parentContractAwardDate, estimatedStartDate, estimatedCompletionDate, awardDecisionDate,
                 completionDate, cancellationDate, signatureDate, paymentD):
        
        self.data = dataType_validation(city, country, bidderLimit, netAmount, netAmountEur, unitPrice, unitNumber, 
                 minPrice, maxPrice, lotNumber, bidsCount, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate,
                 parentContractAwardDate, estimatedStartDate, estimatedCompletionDate, awardDecisionDate,
                 completionDate, cancellationDate, signatureDate, paymentD)
        self.tender = TenderDate_validation(callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate, parentContractAwardDate) 
        self.lot = LotDate_validation(awardDecisionDate, cancellationDate, estimatedStartDate, estimatedCompletionDate, completionDate)
        self.price = price_validation(netAmount, maxPrice, minPrice)
        
      def check_contract(self):
            passed_cnt = 0 # number of checkers passed
            
            # checking for data types of key variables in contract
            if not self.data.dataType_check():
                logging.error("Invalid Contract (wrong datatype), STATE: %s, city: %s, country: %s, callForTendersPublicationDate: %s, bidDeadlineDate: %s, contractAwardNoticePublicationDate: %s, parentContractAwardDate: %s, \
                    estimatedStartDate: %s, awardDecisionDate: %s, cancellationDate: %s, estimatedCompletionDate: %s, completionDate: %s, \
                    netAmount: %s, maxPrice: %s, minPrice: %s" %(self.data.STATE, self.data.city, self.data.country, self.tender.callForTendersPublicationDate, self.tender.bidDeadlineDate, self.tender.contractAwardNoticePublicationDate, self.tender.parentContractAwardDate,
                    self.lot.estimatedStartDate, self.lot.awardDecisionDate, self.lot.cancellationDate, self.lot.estimatedCompletionDate, self.lot.completionDate,
                    self.price.netAmount, self.price.maxPrice, self.price.minPrice))
            else:
                  passed_cnt += 1

            # checking for contract price
            if not self.price.Procurement_Price_Max_Procurement_Price():
                  logging.error("Invalid Contract (wrong price), STATE: %s, maxPrice: %s, netAmount: %s" %(self.price.STATE, self.price.maxPrice, self.price.netAmount))
            elif not self.price.Max_Procurement_Price_Min_Procurement_Price():
                  logging.error("Invalid Contract (wrong price), STATE: %s, maxPrice: %s, minPrice: %s" %(self.price.STATE, self.price.maxPrice, self.price.minPrice))
            else:
                  passed_cnt += 1

            # checking for lot date
            if not self.lot.estimatedStartDate_estimatedCompletionDate():
                  logging.error("Invalid Contract (wrong lot date), STATE: %s, estimatedCompletionDate: %s, estimatedStartDate: %s" %(self.lot.STATE, self.lot.estimatedCompletionDate, self.lot.estimatedStartDate))
            elif not self.lot.estimatedStartDate_awardDecisionDate():
                  logging.error("Invalid Contract (wrong lot date), STATE: %s, awardDecisionDate: %s, estimatedStartDate: %s" %(self.lot.STATE, self.lot.awardDecisionDate, self.lot.estimatedStartDate))
            elif not self.lot.estimatedStartDate_completionDate():
                  logging.error("Invalid Contract (wrong lot date), STATE: %s, completionDate: %s, estimatedStartDate: %s" %(self.lot.STATE, self.lot.completionDate, self.lot.estimatedStartDate))
            elif not self.lot.cancellationDate_awardDecisionDate():
                  logging.error("Invalid Contract (wrong lot date), STATE: %s, cancellationDate: %s, awardDecisionDate: %s" %(self.lot.STATE, self.lot.cancellationDate, self.lot.awardDecisionDate))
            else:
                  passed_cnt += 1

            # checking for tender date
            if not self.tender.Tender_Calling_Date_Contract_Award_Date():
                  logging.error("Invalid Contract (wrong tender date), STATE: %s, parentContractAwardDate: %s, callForTendersPublicationDate: %s" %(self.tender.STATE, self.tender.parentContractAwardDate, self.tender.callForTendersPublicationDate))
            elif not self.tender.Tender_Calling_Date_bidDeadlineDate():
                  logging.error("Invalid Contract (wrong tender date), STATE: %s, bidDeadlineDate: %s, callForTendersPublicationDate: %s" %(self.tender.STATE, self.tender.bidDeadlineDate, self.tender.callForTendersPublicationDate))
            elif not self.tender.Tender_Calling_Date_Award_Notice_Date():
                  logging.error("Invalid Contract (wrong tender date), STATE: %s, contractAwardNoticePublicationDate: %s, callForTendersPublicationDate: %s" %(self.tender.STATE, self.tender.contractAwardNoticePublicationDate, self.tender.callForTendersPublicationDate))
            else:
                  passed_cnt += 1

            return passed_cnt == 4 # if all 4 passed return T (TRUE), else F (FALSE)
