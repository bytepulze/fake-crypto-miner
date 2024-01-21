import colorama
from colorama import Fore
import os
import random
import secrets
import string
import time

#-------------------------------------------------------------------------------

os.system('clear')

print(Fore.YELLOW + 'ethfavcoin.xyz - fake crypto miner')


#-------------------------------------------------------------------------

time.sleep(1)

print(' ')

choice = input(Fore.WHITE + 'Crypto Name To Mine: ')

wallet = input(Fore.WHITE + f'{choice} Wallet Adress: ')

amount = input(Fore.WHITE + 'Amount Of Mining Attempts: ')
amount = int(amount)

print(Fore.RED + '-----------------------------------------------')

mined = 0
mined = int(mined)

profit = 0
profit = int(profit)

#---------------------------------------------------------------------------

for line in range(amount):
    
    time.sleep(0.5)
    mined = int(mined) + 1
    hash_profit = random.randint(3, 9) #This depends on your CPU power
    hash_profit = int(hash_profit)
    profit = int(profit) + hash_profit
    hash_id = ''.join(secrets.choice(string.ascii_letters + string.digits)
                      for i in range(12))
    print(Fore.GREEN + f'Mined: ${hash_profit}', '|', hash_id)
  
    if mined == amount:
        print(Fore.RED + '-----------------------------------------------')
        print(Fore.YELLOW + f'Successfully Mined: {amount} Hashes')
        print(' ')
        time.sleep(1)
        print(Fore.MAGENTA + f'Profit: ${profit}')
        time.sleep(1)
        print(Fore.GREEN + f'Sent: ${profit} To: {wallet}')
