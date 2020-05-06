from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={
    'blackELO': {
        '$gte': '1500',
        '$lt': '1600'
    },
    'whiteELO': {
        '$gte': '1500',
        '$lt': '1600'
    }
}

result = client['chess']['matches'].find(
  filter=filter
)

import pandas as pd
df = pd.DataFrame(list(result))
print(df)