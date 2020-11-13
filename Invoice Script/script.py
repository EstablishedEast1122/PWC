invoice = open("Invoice.txt", "r")
payments = open("Payments.txt", "r")


invoiceList = invoice.readlines()
paymentsList = payments.readlines()

diff = []

for i in invoiceList:
    if i not in paymentsList:
        diff.append(i)

print(diff)





