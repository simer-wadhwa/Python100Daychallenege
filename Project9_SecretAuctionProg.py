
from extra_files import art




print(art.bit_logo)
print("Welcome to the secret Auction program")

bit_dict ={}

should_end = False

while not should_end:
    name = input("What ia your name?:")
    bid = int(input("What's your bid?: $"))
    bit_dict[name] = bid

    restart = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if restart.lower() == "no":
        should_end = True


maximum_bid = 0
for bidder in bit_dict:
    if bit_dict[bidder] > maximum_bid:
        maximum_bid = bit_dict[bidder]
        owmer_name = bidder

print(f"The maximaum bid is {maximum_bid} of {owmer_name}")
