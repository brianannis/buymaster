print( '\n'
"""|----------------------------------------------------------|
|       ____              __  ___           __             |
|      / __ )__  ____  __/  |/  /___ ______/ /____  _____  |
|     / __  / / / / / / / /|_/ / __ `/ ___/ __/ _ \/ ___/  |
|    / /_/ / /_/ / /_/ / /  / / /_/ (__  ) /_/  __/ /      |
|   /_____/\__,_/\__, /_/  /_/\__,_/____/\__/\___/_/       |
|               /____/                                     |
|----------------------------------------------------------|"""
	)
from app import *
capital = 1000

myport = portfolio('TD Dank')

print(bcolors.OKGREEN + 'Portfolio name: ' + myport.name + bcolors.ENDC)

# Provision portfolio
myport.add_security('VTI')
myport.add_security('VXUS')
myport.add_security('BND')
myport.add_security('BNDX')

# Provision portfolio
for sec in myport.group:
	if sec.name == 'VTI':
		sec.set_shares(18)
		sec.set_allocation(0.54)
		sec.get_price()
		sec.get_marketvalue()
	if sec.name == 'VXUS':
		sec.set_shares(27)
		sec.set_allocation(0.36)
		sec.get_price()
		sec.get_marketvalue()
	if sec.name == 'BND':
		sec.set_shares(0)
		sec.set_allocation(0.07)
		sec.get_price()
		sec.get_marketvalue()
	if sec.name == 'BNDX':
		sec.set_shares(0)
		sec.set_allocation(0.03)
		sec.get_price()
		sec.get_marketvalue()

# Update portfolio value
myport.update_portfolio_value()

# Ensure provisioning process with the below
for sec in myport.group:
    print 'Security: %s Shares: %s Allocation: %s Price: %s Market Value: %s ' % (sec.name,str(sec.shares),str(sec.allocation),str(sec.price),format_money(sec.marketvalue))

print('\n')
print(bcolors.OKGREEN + "Portoflio Total Value: " + bcolors.ENDC)
print format_money(myport.portfoliovalue)

print('\n')
print(bcolors.OKGREEN + "Query functions: uses portfolio" + bcolors.ENDC)
print("Get portfolio security price")
print get_port_security_price(myport)
print("Get portfolio allocation")
print get_port_allocation(myport)

print('\n')
print(bcolors.OKGREEN + "Buy functions: uses capital" + bcolors.ENDC)
print("Proposed whole shares to buy")
print buy_shares(myport,capital)
print("Left over cash")
print leftover_cash(myport,capital)

print('\n')
print(bcolors.OKGREEN + "Rebalance functions: uses portfolio" + bcolors.ENDC)
print("Target share allocation")
print rebalance_target_allocation(myport)
print("Rebalance reccomended action")
print rebalance_action(myport)
