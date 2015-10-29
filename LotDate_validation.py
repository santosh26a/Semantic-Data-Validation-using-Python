# It validates date properties for Lots

class LotDate_validation:
    
    STATE=None
    
    def __init__(self, awardDecisionDate, cancellationDate, estimatedStartDate, estimatedCompletionDate, completionDate):
        self.estimatedStartDate=estimatedStartDate
        self.awardDecisionDate=awardDecisionDate
        self.cancellationDate=cancellationDate
        self.estimatedCompletionDate=estimatedCompletionDate
        self.completionDate=completionDate
        
        
    def estimatedStartDate_estimatedCompletionDate(self):
        'Rule: validating if estimatedCompletionDate is later than the estimatedStartDate'
        if self.estimatedCompletionDate is not None and self.estimatedStartDate is not None and self.estimatedCompletionDate > self.estimatedStartDate:
            LotDate_validation.STATE=True
            return LotDate_validation.STATE
        else:
            LotDate_validation.STATE=False
            return LotDate_validation.STATE
        
        
    def estimatedStartDate_awardDecisionDate(self):
        'Rule: validating if awardDecisionDate is earlier than the estimatedStartDate'
        if self.awardDecisionDate is not None and self.estimatedStartDate is not None and self.awardDecisionDate < self.estimatedStartDate:
            LotDate_validation.STATE=True
            return LotDate_validation.STATE
        else:
            LotDate_validation.STATE=False
            return LotDate_validation.STATE
        
    
    def estimatedStartDate_completionDate(self):
        'Rule: validating if completionDate is later than the estimatedStartDate'
        if self.completionDate is not None and self.estimatedStartDate is not None and self.completionDate > self.estimatedStartDate:
            LotDate_validation.STATE=True
            return LotDate_validation.STATE
        else:
            LotDate_validation.STATE=False
            return LotDate_validation.STATE

    
    def cancellationDate_awardDecisionDate(self):
        'Rule: validating if cancellationDate is later than or equal to awardDecisionDate'
        if self.cancellationDate is not None and self.awardDecisionDate is not None and self.cancellationDate >= self.awardDecisionDate:
            LotDate_validation.STATE=True
            return LotDate_validation.STATE
        else:
            LotDate_validation.STATE=False
            return LotDate_validation.STATE
        
            
          
