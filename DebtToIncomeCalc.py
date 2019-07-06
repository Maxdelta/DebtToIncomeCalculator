def dti(debt, income):
   # print(f" Dividing {debt} / {income}")
    return debt / income
    

def debt(mortgage, credit_cards, car_payment):
   # print(f" Adding {mortgage} + {credit_cards} + {car_payment}")
    return mortgage + credit_cards + car_payment

def income(residual_income, job_income):
   # print(f" Adding {residual_income} + {job_income}")
    return residual_income + job_income
  
#this sets the prompt 
prompt =('>') 
 
 


#this prompts the user to add in debts. should add in personal loans. 
print("How much is your current mortgage payment?")
mortgage = int(input(prompt))

print("How much do you pay per month in credit card debt?")
credit_cards = int(input(prompt))

print("How much is your car payments?")
car_payment = int(input(prompt))


#this prompts the user to add in income sources 
print("what is your passive income per month?")
residual_income = int(input(prompt))
print("What do you gross per month from your job?")
job_income = int(input(prompt))

#prints out the debts and income calculated 
print(f"Your debts per month: ${debt(mortgage, credit_cards, car_payment)}")
print(f"Your income per month: ${income(residual_income, job_income)}")

#this calculates the debt to income ratio 
debt_to_income = debt(mortgage, credit_cards, car_payment) / income(residual_income, job_income)
print(f"Your Debt to income ratio is:", {debt_to_income})

