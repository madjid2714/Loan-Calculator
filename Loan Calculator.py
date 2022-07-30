import math
import argparse
parser = argparse.ArgumentParser(description="TDifferentiate payment")
parser.add_argument("-t", "--type" , choices=["annuity", "diff"],)
parser.add_argument("-p1", "--payment")
parser.add_argument("-p2", "--periods")
parser.add_argument("-p3", "--principal")
parser.add_argument("-i", "--interest")
args = parser.parse_args()
formule = [args.type, args.interest, args.payment, args.periods, args.principal]
if len(formule) < 4 :
   print("Incorrect parameters.")
else:
    if args.type == "diff":
        if args.interest and args.periods and args.principal != None and args.payment== None:
            if float(args.interest) >= 0 and int(args.periods) >= 0 and int(args.principal) >= 0:
                i = float(args.interest) / (12 * 100)
                op = 0
                for index in range(1, int(args.periods)+1):
                    dm = math.ceil((int(args.principal) / int(args.periods)) + i * (int(args.principal) - (int(args.principal) * (index - 1)) / int(args.periods)))
                    op += dm 
                    print(f"Month {index}: payment is {dm}")
                ov = op - int(args.principal)
                print(f"Overpayment : {ov}")
                
        else:
            print("Incorrect parameters.")



    elif args.type == "annuity":
        if args.interest and args.payment and args.principal != None and args.periods == None:
            if float(args.interest) >= 0 and int(args.payment) >= 0 and int(args.principal) >= 0:
                i = float(args.interest) / (12 * 100)
                base = 1 + i
                x =  ( int(args.payment) / (int(args.payment) - i * int(args.principal)))
                n = math.log(x, base)

                number_months = math.ceil(n)
                years, months = divmod(number_months, 12)
                if months == 0:
                    print(f"It will take {years} years to repay this loan!")
                else:
                    
                    print(f"It will take {years} years and {months} months to repay this loan!")

                ov = int(args.payment) * number_months - int(args.principal)
                print(f"Overpayment : {ov}")

        elif args.interest and args.periods and args.payment != None and args.principal == None:
            if float(args.interest) >= 0 and int(args.periods) >= 0 and float(args.payment) >= 0 :
                i = float(args.interest) / (12 * 100)

                p = math.floor(float(args.payment) / (( i * ((1 + i)**(int(args.periods))) )/( ((1+i)**(int(args.periods))) -1 )))

                print(f"Your loan principal = {p}! ")

                ov = int(args.payment) * int(args.periods) - int(p)
                print(f"Overpayment : {ov}")
        elif args.interest and args.periods and args.principal != None and args.payment == None:
            print("im here")
            if float(args.interest) >= 0 and int(args.periods) >= 0 and int(args.principal) >= 0 :
                i = float(args.interest) / (12 * 100)
                a = math.ceil(float(args.principal) * ( i * ((1 + i)**(int(args.periods))) )/( ((1+i)**(int(args.periods))) -1 ))
                print(f"Your annuity payment = {a}! ")

                ov =  int(a) * int(args.periods) - int(args.principal)
                print(f"Overpayment : {ov}")


        else:
            print("Incorrect parameters.")

    else:
        print("Incorrect parameters.")
    

