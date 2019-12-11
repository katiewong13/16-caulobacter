def add_growth_identifier(df):
    '''Initialize data frame with growth identifier automatically set to grow.'''
    grow = []

    i = 0
    while i < len(df1):
        grow.append("Growing")
        i += 1

    df.insert(3, 'growth identifier', grow)
    
def add_division(area, df):
    '''Add growth identifiers to data frame.'''
    thresh = 0.5
    i = 1
    division = []
    while i < len(area):
        if abs(area[i] - area[i-1]) > thresh:
            division.append(i-1)
        i += 1
        
    for div in division:
        df.loc[(div, 'growth identifier')] = 'Division'
    return division

def time_diff(division): 
    '''Calculate time between divisions, and place in dataframe.'''
    i = 0  
    dt = []
    while i < len(division) - 1:
        time1 = df.loc[(division[i], 'time (min)')]
        #print("1:", time1)
        time2 = df.loc[(division[i+1], 'time (min)')]
        #print("2:", time2)
        time_diff = time2 - time1
        #print(time_diff)
        dt.append(time_diff)
        i += 1
    df_dt = pd.DataFrame(data = {'Time between divisions (in min)' : dt})
    return



