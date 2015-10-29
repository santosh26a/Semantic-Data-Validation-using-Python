from dataType_validation import dataType_validation
from LotDate_validation import LotDate_validation
from price_validation import price_validation
from TenderDate_validation import TenderDate_validation
from data_validation import data_validation
from datetime import date
import logging

logger = logging.getLogger()
hdlr = logging.FileHandler('data_validation.log')
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

'''
data_validation_run = data_validation(city, country, bidderLimit, netAmount, netAmountEur, unitPrice, unitNumber, 
                 minPrice, maxPrice, lotNumber, bidsCount, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate,
                 parentContractAwardDate, estimatedStartDate, estimatedCompletionDate, awardDecisionDate,
                 completionDate, cancellationDate, signatureDate, paymentD)
'''

if __name__ == "__main__":
      data_validation_run = data_validation("London", "UK", 66, 3, 4, 78, 
        1487, 150, 101, 7787, 9, date(2013, 7, 8), date(2013, 8, 8),
        date(2014, 7, 8), date(2014, 7, 8), date(2014, 9, 8), date(2014, 8, 8),
        date(2014, 5, 8), date(2014, 10, 8), date(2014, 11, 8), date(2014, 12, 8), date(2014, 12, 9))
      logging.warning('Checked, state: ' + str(data_validation_run.check_contract()))
      
