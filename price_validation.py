class price_validation:

    # STATE will be TRUE if rule validates for arguments value otherwise FALSE    
    STATE = None
    
    # It takes 3 arguments netAmount, maxPrice, and minPrice to validate procurement price
    def __init__(self, netAmount, maxPrice, minPrice):
        self.netAmount=netAmount
        self.maxPrice=maxPrice
        self.minPrice=minPrice
       
    # validation for maximum procurement contract price      
    def Procurement_Price_Max_Procurement_Price(self):
        'Rule: validating if maximum price (Schema ID: maxPrice) is greater than or equal to procurement price (Schema ID: netAmount)'
        if self.maxPrice is not None and self.netAmount is not None and self.maxPrice >= self.netAmount:
            price_validation.STATE=True
            return price_validation.STATE
            
        else:
            price_validation.STATE=False
            return price_validation.STATE
            
            
    # validation for minimum and maximum procurement contract price       
    def Max_Procurement_Price_Min_Procurement_Price(self):
        'Rule: validating if maxPrice is greater than or equal to minimum price (Schema ID: minPrice)'
        if self.maxPrice is not None and self.minPrice is not None and self.maxPrice >= self.minPrice:
            price_validation.STATE=True
            return price_validation.STATE
        else:
            price_validation.STATE=False
            return price_validation.STATE
             
    
    # validation for minimum procurement contract price
    def Procurement_Price_Min_Procurement_Price(self):
        'Rule: validating if minPrice is lesser than or equal to netAmount'
        if self.minPrice is not None and self.netAmount is not None and self.minPrice <= self.netAmount:
            price_validation.STATE=True
            return price_validation.STATE
        else:
            price_validation.STATE=False
            return price_validation.STATE
            
