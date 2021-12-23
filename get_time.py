import time

def get_time():
    return time.ctime(time.time()) + "\r\n"

def convert_usd_to_vnd(usd):
    return usd * 23000

amount = float(input("Enter amount: "))
print(f"{amount} USD = {convert_usd_to_vnd(amount):.2f} VND at {get_time()}")