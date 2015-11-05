# Semantic-Data-Validation-using-Python
  Semantic data validation is for validating data of public procurement contract variables. Basically, this code is   
  checking inconsistancies in public procurement contract based on its properties. Properties such as data type, 
  price, tender date, contract lot date etc. 

# Data Validation Code Guide

1. Data Validation Code Structure

   Python main filename: data_validation_run.py
   
   Task: This imports files in component 1 and component 2 and print message in data_validation2.log file. 

   Structure of data_validation_run.py is based on following 2 main components:

   i)	Validation the contract variable data based on its 4 properties: 

        a)	Data Type

           Python filename: dataType_validation.py
        
           Task: It validates data type for key contract variables. For example, 
           city and country must be text data type; callForTendersPublicationDate must be date data 
           type etc.

        b)	Price

           Python filename: price_validation.py
           
           Task: It validates price properties for each contract.  For example, maxPrice must be greater 
                 than or equal to minPrice; netAmount must fall within maxPrice and minPrice etc.

        c)	Tender Date
        
           Python filename: TenderDate_validation.py
           
           Task: It validates date properties for each tender. For example, bidDeadlineDate must be later 
                 than callForTendersPublicationDate; contractAwardNoticePublicationDate must be later than    
                 callForTendersPublicationDate etc.

        d)	Lot Date
        
            Python filename: LotDate_validation.py
            
            Task: It validates date properties for each lot. For example, estimatedCompletionDate must 
                  be later than estimatedStartDate; estimatedStartDate must be later than the 
                  awardDecisionDate etc.

    ii)	Printing messages in data_validation2.log file 
    
        Python filename: data_validation.py
        
        Task: This print message in data_validation2.log file when rules based on above 4 properties 
              in component 1 do not validates contract data. A typical message for example would be like 
              following in case of contract has wrong minimum procurement contract price (minPrice):
              Invalid Contract (wrong price), STATE: False, maxPrice: 101, minPrice: 150 
              
              
  
2. Test of the Data Validation Code:
 
    Python filename: data_validation_run_test.py. This file is a copy of the data_validation_run.py with 
                     testing data included. It imports all files in component 1 and component 2.  
                     Also it prints the data validation messages in data_validation2.log file.

    2.1.	 Output
    
        Output will be the messages in data_validation2.log file about incorrectness in contract data if
        there is any.  In our test, it prints following messages:
        Invalid Contract (wrong price), STATE: False, maxPrice: 101, minPrice: 150
        Invalid Contract (wrong lot date), STATE: False, estimatedCompletionDate: 2014-08-08, 
        estimatedStartDate: 2014-09-08
        
        It’s because tested data in data_validation_run_test.py file has wrong maxPrice, minPrice,        
        estimatedCompletionDate, and estimatedStartDate.
