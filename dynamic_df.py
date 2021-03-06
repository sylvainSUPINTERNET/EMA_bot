import pandas as pd

df = None
MAX_ENTRIES_IN_MEMORY=25

def test(new_value):
  global df

  if df is None:
    df = pd.DataFrame(data={"receivedAt": [f"DATE {new_value}"], "price": new_value})
  if df.shape[0] >= MAX_ENTRIES_IN_MEMORY:
    # df = df[['receivedAt','price']].shift(periods=1, fill_value=None)
    df = df.shift(periods=1, fill_value=None)
    df_temp = pd.DataFrame(data={"receivedAt": [f"DATE {new_value}"], "price": new_value})
    df.iloc[0] = df_temp
  else:
    df_temp = pd.DataFrame(data={"receivedAt": [f"DATE {new_value}"], "price": new_value})
    df = pd.concat([df_temp, df])

  print(df)
  return df

for i in range(50):
  test(i)
