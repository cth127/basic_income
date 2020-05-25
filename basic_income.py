import numpy as np

# variables
society = [0, 25, 50, 75, 100]
tax_rate = [0.1, 0.1, 0.1, 0.1, 0.1]
growth_rate = 0.1

# social function
def unequal_growth(growth_rate) :
    uneq = list()
    for i in range(5) :
        uneq.append(growth_rate / 15 * (i + 1))
    return uneq


def economic_growth(society, uneq_growth_rate) :
    for i in range(5) :
        society[i] = society[i] * (1 + uneq_growth_rate[i])
    return society

def redistribute(society, tax_rate) :
    fund = 0
    for i in range(5) :
        fund += society[i] * tax_rate[i]
        society[i] -= society[i] * tax_rate[i]
    for j in range(5) :
        society[j] += fund / 5
    return society

def gini_coef(society) :
    pie = np.sum(society)
    a = pie / 5
    b = pie / 5 * 2
    c = pie / 5 * 3
    d = pie / 5 * 4
    e = pie / 5 * 5
    a_coef = (a - society[0]) / pie * 1/5 * 1/2
    b_coef = (a - society[0] + b - society[1]) / pie * 1/5 * 1/2
    c_coef = (b - society[0] + c - society[1]) / pie * 1 / 5 * 1 / 2
    d_coef = (c - society[0] + d - society[1]) / pie * 1 / 5 * 1 / 2
    e_coef = (d - society[0] + e - society[1]) / pie * 1 / 5 * 1 / 2
    gini = 1 - (a_coef + b_coef + c_coef + d_coef + e_coef)
    return gini

# each k means 1 year
uneq_growth_rate = unequal_growth(growth_rate)
for k in range(5) :
    society = economic_growth(society, uneq_growth_rate)
    society = redistribute(society, tax_rate)
    gini = gini_coef(society)
    print(gini)
