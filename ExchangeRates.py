class ExchangeRates:
    # Similar to the bond experiment we did in class, the class exchange rate runs data and has prior knowledge on how to convert money 
    def __init__(self, file_path):
        with open(file_path) as file:
    #file_path opens the CSV with the exchange rates 
            lines = file.readlines()
        last_row = lines[-1].split(",")
    #The most recent USD/CAD rate is second-to-last in the row not last because the final column is empty
        self.rate = float(last_row[-2])
    def convert(self, amount, from_currency, to_currency):
    #USD to CAD multiplies by the rate and CAD to USD divides by the rate since the rate is CAD per 1 USD!
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate
        else:
            return amount # same currency, no conversion needed
        
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
#the lines below asks the user for the amount and the two currencies (CAD and USD) so the amount is converted to a number with floating point
amount = float(input("Enter the amount: "))
from_currency = input("Convert from (USD or CAD): ")
to_currency = input("Convert to (USD or CAD): ")

result = rates.convert(amount, from_currency, to_currency)
print(f"${amount:,.2f} {from_currency} is equal to ${result:,.2f} {to_currency}")