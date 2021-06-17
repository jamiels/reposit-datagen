import random as r, csv

issuers =('Adventure Lending','ABC Lending','Global Lending')
property_types=('Multi-family','Single-family','Retail','Office')
age_ranges = ('20-25','26-30','30-40','40-50','50-60')
currency = 'USD'
asset_type = "Mortgage Token"

with open('mortgage_data.csv', mode='w+') as mortgage_data:
    w = csv.writer(mortgage_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for n in range(10):
        asset_id = "MT" + str(r.randint(1000000,9999999))
        issuer = issuers[r.randint(0,len(issuers)-1)]
        address = str(r.randint(1000,9999)) + ' REposit St. San Francisco, CA 94401'
        tax_id = '1-45-83-0453-' + str(r.randint(1000,9999)) + '-' + str(r.randint(1000,9999))
        appraised_value = str(r.randint(2000000,15000000))
        market_value = round(int(appraised_value) * 1.25)
        ltv = round(r.uniform(.7,.9),2)
        loan_amount = (1-ltv) * market_value
        property_type = property_types[r.randint(0,len(property_types)-1)]
        age_range = age_ranges[r.randint(0,len(age_ranges)-1)]
        fico = str(r.randint(600,800))
        dti = str(round(r.uniform(.1,.6),2))
        loan_amount = round(ltv * market_value,2)
        unpaid_amount = round(r.uniform(.1,.9) * loan_amount,2)
        rate = str(round(r.uniform(.01,.06),4))
        term = str(r.randint(20,30) * 12)

        w.writerow([asset_id,asset_type,issuer,currency,address,tax_id,appraised_value, market_value,ltv,property_type,age_range,fico,dti,loan_amount,unpaid_amount,rate,term])
