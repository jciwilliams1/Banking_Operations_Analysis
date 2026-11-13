Select *
From
(Select LAT.Genre,
    Sales_and_Collections.Event,
    sum(Sales_and_Collections.Net_Sales) as Net_Sales
    From Sales_and_Collections Left Join LAT on LAT.Act=SALES_AND_COLLECTIONS.Event
    Where LAT.Genre = 'Bluegrass/Folk'
    Group By LAT.Genre,Sales_and_Collections.Event
    Order By 3 desc
    Limit 1) Bluegrass_Folk


UNION

Select *
From
(Select LAT.Genre,
    Sales_and_Collections.Event,
    sum(Sales_and_Collections.Net_Sales) as Net_Sales
    From Sales_and_Collections Left Join LAT on LAT.Act=SALES_AND_COLLECTIONS.Event
    Where LAT.Genre = 'Broadway'
    Group By LAT.Genre,Sales_and_Collections.Event
    Order By 3 desc
    Limit 1) Broadway
    

