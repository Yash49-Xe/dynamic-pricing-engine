import pandas as pd

print("Loading Parquet database into RAM...")
df = pd.read_parquet("inventory.parquet", engine = "pyarrow")

def get_product_data(target_id: str):
    product_row = df[df['product_id'] == target_id]
    
    if product_row.empty:
        return None
        
    #pandas will return a series in product_row as there can be multiple product_id = target_id, also last element is data_type so we will use iloc[0]
    base_cost = product_row['base_cost'].iloc[0]
    competitor_price = product_row['competitor_price'].iloc[0]
    sales = product_row['sales_last_30_days'].iloc[0]
    
    return {
        "base_cost": float(base_cost),
        "competitor_price": float(competitor_price),
        "demand_multiplier": float(sales / 1000)
    }