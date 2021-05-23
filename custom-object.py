# python object representing a purchase for a given amount
class Purchase(object):
    def _init_(self, amount):
        self.amount = amount
        
    def calculatetax(self, taxPercent):
        return self.amount * taxPercent/100.0
        
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0
        
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)
        
# create purchase object given an amount
purchase = Purchase(100.0)

taxPercent = 7.5
tipPercent = 20.0

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

print ('Tax: ', tax)
print ('Tip: ', tip)
print ('Total:', purcase.calculateTotal(taxPercent, tipPercent))
