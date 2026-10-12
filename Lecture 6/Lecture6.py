# # n = 5

# # def converter(usd_val):
# #     Inr_val = usd_val * 96.28
# #     print(usd_val, "Dollars converted to INR is:", Inr_val)
    
# # converter()
   
# #  RECURSION
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
    
# show(55)
# print("END")

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(999))







    