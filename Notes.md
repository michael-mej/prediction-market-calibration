## Session1

Essentially just got in touch with the Polymarket API, downloaded a resolved market into a Json (in data). The fetching program in src is written as is so that we only extract 1 already resolved market

The next task is to pull specifically the files i want to

##Session 2

Requested acces of more markets from the API. Established that the max limit it provides at a time is 100.
Pulled data into a csv format and into a pandas DataFrame for further analysis

Found that manu columns are mostly nulleed (rows 72 to 89 withe xception of 82 and 73)

Narrowed down the column that dertirmins market ourcome. Found the column "outcomePrices" which contained expected strings of from [number near 1, number near 0] (one event had happend). But surpisingly most markets are [0, 0] and some are numbers near 0.5 implying the final price of shares was neither 1 nor 0

Task for next session. Issolate the [0, 0] values and determine what column specifically causes this
