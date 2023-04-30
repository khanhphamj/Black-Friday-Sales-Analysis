import pandas as pd

class dataSchema:
    user_id = "User_ID"
    product_id = "Product_ID"

def load_data_csv(path: str)-> pd.DataFrame:
    df = pd.read_csv(
        path,
        dtype={
            dataSchema.user_id: str,
            dataSchema.product_id: str
        }
    )
    return df