import pandas as pd

df = None

EMA_SMALL_PERIOD_DAYS = 12
EMA_BIG_PERIOD_DAYS = 26

def test(new_value):
  global df

  if df is None:
      df = pd.DataFrame(data={"receivedAt": [f"DATE {new_value}"], "price": new_value, "12_EMA": None, "26_EMA": None})

  if df is not None:
      if df.shape[0] >= 50 :
      # dataFrame = pd.DataFrame(data={"receivedAt": [f"DATE {new_value_2}"], "price": new_value_2, "12_EMA": None, "26_EMA": None})
        new_dataframe = pd.DataFrame(data={"receivedAt": [f"DATE {new_value}"], "price": new_value, "12_EMA": None, "26_EMA": None})
        df = pd.concat([df, new_dataframe])
        # remove first line 
        df = df.iloc[1: , :]
        df['12_EMA'] = df['price'].ewm(span = EMA_SMALL_PERIOD_DAYS, adjust = False).mean()
        df['26_EMA'] = df['price'].ewm(span = EMA_BIG_PERIOD_DAYS, adjust = False).mean()
      else:
        new_dataframe = pd.DataFrame(data={"receivedAt": [f"DATE {new_value}"], "price": new_value, "12_EMA": None, "26_EMA": None})
        df = pd.concat([df, new_dataframe])
        df['12_EMA'] = df['price'].ewm(span = EMA_SMALL_PERIOD_DAYS, adjust = False).mean()
        df['26_EMA'] = df['price'].ewm(span = EMA_BIG_PERIOD_DAYS, adjust = False).mean()


for i in range(100):
  test(i)
print(df)
