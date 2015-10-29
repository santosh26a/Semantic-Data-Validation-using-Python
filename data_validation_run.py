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

if __name__ == "__main__":
      data_validation_run = data_validation(city, country, bidderLimit, netAmount, netAmountEur, unitPrice, unitNumber, 
                 minPrice, maxPrice, lotNumber, bidsCount, callForTendersPublicationDate, bidDeadlineDate, contractAwardNoticePublicationDate,
                 parentContractAwardDate, estimatedStartDate, estimatedCompletionDate, awardDecisionDate,
                 completionDate, cancellationDate, signatureDate, paymentD)
      logging.warning('Checked, state: ' + str(data_validation_run.check_contract()))
      
