class Wages:
    # vars
    STATE_TAX_RATE: float = 0.035
    FED_TAX_RATE: float = 0.15

    # execution

    # Extract data from the user.
    employee = input("Employee name: \n")
    hours = input("Hours worked: \n")
    pay_rate = input("Pay rate: \n")

    # Compute the employee's taxes and wages.
    wages = float(hours) * float(pay_rate)
    stateTaxes = wages * STATE_TAX_RATE
    fedTaxes = wages * FED_TAX_RATE
    takeHome = wages - stateTaxes - fedTaxes

    # Print the results.
    print("PAY REPORT")
    print("Employee: ", employee)
    print("----------------------------------")
    print("Wages:       ", wages)
    print("State Taxes: ", stateTaxes)
    print("Fed Taxes:   ", fedTaxes)
    print("Pay:         ", takeHome)
