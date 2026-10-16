import csv


class ExchangeRates:
    """Reads the latest USD/CAD rate from a Bank of Canada CSV file."""

    RATE_COLUMN = "FXAUSDCAD"

    def __init__(self, filename):
        self.filename = filename
        self.usd_cad = self._load_latest_rate()

    def _load_latest_rate(self):
        with open(self.filename, newline="", encoding="utf-8-sig") as f:
            rows = [row for row in csv.reader(f) if row]

        # Bank of Canada files can have notes above the data,
        # so find the row that holds the column names.
        header_index = None
        for i, row in enumerate(rows):
            if self.RATE_COLUMN in row:
                header_index = i
                break
        if header_index is None:
            raise ValueError(f"Column {self.RATE_COLUMN} not found in {self.filename}")

        col = rows[header_index].index(self.RATE_COLUMN)

        # The last row holds the latest rates
        latest_row = rows[-1]
        return float(latest_row[col])

    def convert(self, amount, from_currency, to_currency):
        """Convert between USD and CAD using the latest USD/CAD rate."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad
        if from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_cad
        raise ValueError("Currencies must be USD or CAD.")


def main():
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")  # change to your file's name
    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ").strip().upper()
    to_currency = input("Convert to (USD or CAD): ").strip().upper()

    result = rates.convert(amount, from_currency, to_currency)

    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


if __name__ == "__main__":
    main()