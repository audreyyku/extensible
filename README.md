**Parameters:**
- list of files f = ["*.csv","*.csv","*.csv",...]
- time delta = 15, 30, 60 (minutes)
- time format = '%m/%d/%Y %I:%M %p' matches string patterns to create Datetime object

**Function:**
- appends files
- fix daylight savings (missing hour on 3/11/18 and additional hour on 11/4/18)
    - fills in 0s into missing hour slot
- removes duplicate dates
- saves new timeseries to CSV file
    

**Time format reference:**
- https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
- example 1

    '01/01/2018 12:15 AM'

    '%m/%d/%Y %I:%M %p'

- example 2

    '00:15,02/01/2018'

    '%H:%M,%m/%d/%Y'
    
- example 3

    '1/01/18  00:15:00 PM'

    '%-m/%-d/%y %I:%M:S %p'
    
Run command example: 
formatTimeseries(['practice.csv'], delta=15, timeformat='%m/%d/%Y %I:%M %p', savefile='practice1.csv').head()

