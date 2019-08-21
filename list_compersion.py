thislist=[iter for iter in range(5)]
print(thislist)
print(iter)

countrylist=["India","America","England","Germany","Brazil","Vietnam"]
firstletter=[country[0] for country in countrylist]
print(firstletter)


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
month_odds=[iter for index, iter in enumerate(months) if (index%2 == 0)]
print(month_odds)
