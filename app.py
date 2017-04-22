import ystockquote

# Add input validation for allocation somewhere
# Add input validation for port functions (so it only accepts portfolio objects)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class portfolio(object):
    """A portfolio made up of securities. Portfolios have the
    following properties:

    Attributes:
        name: A string representing the portfolio's name.
        security: A security object
    """

    def __init__(self, name, portfoliovalue=0.0):
        """Return a portfolio object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.group = []
        self.portfoliovalue = portfoliovalue

    def add_security(self, securityname):
        self.group.append(security(securityname))

    def update_portfolio_value(self):
        value = 0
        for item in self.group:
            value += item.marketvalue
        self.portfoliovalue = value

class security(object):

    def __init__(self, name, shares=0.0, allocation=0.0, marketvalue=0.0):
        """Return a security object which is named *name*.""" 
        self.name = name
        self.shares = shares
        self.allocation = allocation
        self.marketvalue = marketvalue

    def set_shares(self, shares):
        """Set the portfolio's shares."""
        self.shares = shares

    def set_allocation(self, allocation):
        '''Set the portfolio's allocation'''
        self.allocation = allocation

    def get_price(self):
        '''Get and set the price of the security'''
        self.price = float(ystockquote.get_price(self.name))

    def get_marketvalue(self):
        self.marketvalue = self.shares * self.price

# Get price per share type in port
def get_port_security_price(port):
    port_share_price = {}
    for item in port.group:
        port_share_price[item.name] = item.price
    return port_share_price

# Get current allocation percentage for each type of security. Probably dont need to loop beacause we already have the data in port object?
def get_port_allocation(port):
    port_share_allocation = {}
    for item in port.group:
        port_share_allocation[item.name] = item.allocation
    return port_share_allocation

# For amount of capital, buy number of share returns
def buy_shares(port,capital):
    shares_to_buy = {}
    for item in port.group:
        shares_to_buy[item.name] = ((float(item.allocation) * int(capital)) // float(item.price))
    return shares_to_buy

# For amount of capital, how much cash will be left over per security type
def leftover_cash(port,capital):
    remaining_cash = {}
    for item in port.group:
        remaining_cash[item.name] = ((float(item.allocation) * int(capital)) % float(item.price))
    return remaining_cash

# For security type and number of shares, cognizant of total port value
# Also, should this reutrn a portfolio object?
def rebalance_target_allocation(port):
    proprosed_allocation = {}
    for item in port.group:
        proprosed_allocation[item.name] = ((port.portfoliovalue * float(item.allocation) // float(item.price)))
    return proprosed_allocation

# Callback rebalance_proposed allocation and diff it between current TODO
def rebalance_action(port):
    difference = {}
    proposal = rebalance_target_allocation(port)
    for item in port.group:
        #print item.name + ":" + str(item.shares)
        #print item.name + ":" + str(proposal[item.name])
        difference[item.name] = (proposal[item.name] - item.shares)
    return difference

# Format string for currency, with commas, etc. 
def format_money(str): 
        return '${:,.2f}'.format(str)
