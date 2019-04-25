def formatTimeseries(files, delta=15, timeformat='%m/%d/%Y %I:%M %p', savefile = 'fixed.csv'):
    
    df = pd.read_csv(files[0])
    for i in range(1,len(files)):
        temp = pd.read_csv(files[i]) #example: files[i] == 'practice.csv'
        df.append(temp, ignore_index=True)
        
    time = list(df)[0]
    unit = list(df)[1]
    df2 = df.groupby(time, sort=False).first().reset_index()
    df2[time] = df2[time].apply(lambda x: datetime.strptime(x, timeformat))
    
    if (list(df2[time])[-1] - list(df2[time])[0] >= timedelta(days=365)):
        start = list(df2[time])[-1] - timedelta(days=364, hours=23, minutes=45)
    else:
        start = list(df2[time])[0]
    end = list(df2[time])[-1]
 
    def datetime_range(start, end, delta):
        current = start
        while current < end:
            yield current
            current += delta

    dummy = pd.DataFrame(data={time: [dt for dt in datetime_range(start, end, timedelta(minutes=delta))]})
    result = dummy.merge(df2,how='left', left_on=time, right_on=time).fillna(0)
    result.to_csv(savefile)
    return result
