print("Welcome to car rentals!")


inpt = 0
#Á meðan eitthvað annað en n er slegið mun forritið halda áfram að keyra
while inpt != "n":
    inpt = input("Would you like to continue (y/n)? ")
    #Forritið keyrir samt bara ef "y" er slegið inn
    if inpt == "y":
        #Hér spyr forritið eftir upplýsingum notandan um bílinn ásamt "customer code"
        customer_code = input("Customer code (b or d): ")
        number_of_days = int(input("Number of days: "))
        odometer_start = int(input("Odometer reading at the start: "))
        odometer_end = int(input("Odometer reading at the end: "))
        #-------------------------------------
        #Hér reiknar forritið heildar mílur sem keyrðar voru og sýnir
        miles_driven = odometer_end - odometer_start
        print("Miles driven:" , miles_driven)
        if customer_code == "b":
            #Ef customer code "b" er valin keyrir forritið út næstu línur þar sem útreiknað er:
            #grunngjald: $40 fyrir sérhvern dag
            base_charge = number_of_days * 40
            #mílugjald: $0.25 fyrir sérhverja mílu
            milage_charge = 0.25 * miles_driven


            total = milage_charge + base_charge
            print("Amount due:",round(total,1))
            

        elif customer_code == "d":
            #Ef customer code "d" er valin keyrir forritið út næstu línur þar sem útreiknað er:
            #grunngjald: $60 fyrir sérhvern dag
            base_charge = 60* number_of_days
            #mílugjald: $0.25 fyrir sérhverja mílu sem er umfram 100 mílur á dag
            #Þar byrjar það að taka frá "fríu" daganna 
            daily_discount = number_of_days * 100
            miles_after_discount = miles_driven - daily_discount
            #Og leggur svo saman með verðinu
            milage_charge = miles_after_discount * 0.25

            total = milage_charge + base_charge
            print("Amount due:",round(total,1))
    
    #Lúppan endar hérna
