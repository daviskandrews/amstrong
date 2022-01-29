def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    if(account_number in range(1000,2000)):
        if(account_balance>100000):
            if(salary>20000 and loan_type=="Car"):
                eligible_loan_amount=500000
                bank_emi_expected=36
                if(customer_emi_expected<=bank_emi_expected and loan_amount_expected <=eligible_loan_amount):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(salary>50000 and (loan_type=="Car" or loan_type=="House")):
                eligible_loan_amount=6000000
                bank_emi_expected=60
                if(customer_emi_expected<=bank_emi_expected and loan_amount_expected <=eligible_loan_amount):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(salary>75000 and (loan_type=="Car"  or  loan_type=="House" or loan_type=="Business")):
                eligible_loan_amount=7500000
                bank_emi_expected=84
                if(customer_emi_expected<=bank_emi_expected and loan_amount_expected <=eligible_loan_amount):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:",loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")
        
calculate_loan(1024,55000,100001,"House",120000,45)
calculate_loan(1005,90000,100000,"Business",120000,80) 
calculate_loan(1005,25000,255000,"Car",300000,30)



def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if((food_type=="N" or food_type=="V")and quantity_ordered>=1 and distance_in_kms>0):
        if(food_type=="V"):
            if(distance_in_kms<=3):
                bill_amount=120*quantity_ordered+0
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=120*quantity_ordered+((distance_in_kms-3)*3)
            else:
                bill_amount=120*quantity_ordered+((distance_in_kms-6)*6)+9
        else:
            if(distance_in_kms<=3):
                bill_amount=150*quantity_ordered+0
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=150*quantity_ordered+((distance_in_kms-3)*3)
            else:
                bill_amount=150*quantity_ordered+((distance_in_kms-6)*6)+9
    else:
        bill_amount=(-1)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("V",1,7)
print(bill_amount)




def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    five_needed = five if five <= no_of_five else no_of_five
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))

make_amount(28,8,5)


def sms_encoding(data):
    word=data.split()
    vowels="aeiouAEIOU"
    st=""
    for i in word:
        if(len(i)==1):
            st=st+i
        else:
            for j in i:
                if j not in set(vowels):
                    st=st+j
        st=st+" "
    return st[0:-1]
data="GOOD DAYS AND BAD DAYS"
print(sms_encoding(data))
