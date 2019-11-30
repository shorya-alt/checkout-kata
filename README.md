checkout- kata:
Our checkout accepts items in any order, so that if we scan product B, then product
A, and then another product B, we’ll recognize the two B’s and price them at a
discounted price of Rs 45 instead of individual pricing of Rs 30, which brings the
Total order pricing to Rs 95.
Item Unit    Special Price
A     50       3 for 130
B     30       2 for 45
C     20
D     15

output :
INPUT        OUTPUT
“”             0
“A”           50
“AB”          80
“CDBA”       115
“AA”         100
“AAA”        130
“AAAA”       180
“AAAAA”      230
“AAAAAA”     260
“AAAB”       160
“AAABB”      175
“AAABBD”     190
“DABABA”     190

Following steps and logic are implemented:
step1: create a class in which all the individual price and discount price of the product taken.products
       are scan in the terms of 'A','B','C','D'. discount price is applied for 'A' and 'B' only.
         a_individualPrice = 50
         b_individualPrice = 30
         c_individualPrice = 20
         d_individualPrice = 15
         a_disc_price = 130
         b_disc_price = 45
step2: Products code are enter by user input.
step3: To get quantity of the each product code getquantity function is used:
       getquantityfunction:
       suppose user  give input as 'ABCDDBA':
       map function which contain lambda expression and user input product code
       lambda function take user input code and  check if  A present in  given input if present then return 1 else 0.
       same process are applied for B,C,D.sum function is used to count all the the product code mapped value.
       a_count = 2
       b_count = 2
       c_count = 1
       d_count = 2
       dict_count = {'A':2,'B':2,'C':1,'D':2}
step4: To get the total of of each product getprice function is used:
        if key == 'A':
         multiplier = 2//3 which give result '0'
         reminder = 2%3 which give result '2'
         a_individualPrice = 50
         a_disc_price = 130
         a_price = 0*130 + 2*50 = 100
        if key == 'B':
         multiplier = 2//2 which give result '1'
         reminder = 2%2 which give result '0'
         b_individualPrice = 30
         b_disc_price = 45
         b_price = 1*45 + 0* 30 = 45
        if key == 'C':
         c_individualPrice = 20
         c_price = 1*20 = 20
        if key == 'D':
         d_individualPrice = 15
         d_price = 2*15 = 30
step5: To get total bill of all products totalbill function is used.
        a_price = 100
        b_price = 45
        c_price = 20
        d_price = 30
        total = 195 output


