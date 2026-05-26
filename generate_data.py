import pandas as pd
import numpy as np

# 1. Set how massive you want your database to be
NUM_PRODUCTS = 100_000 

print(f"Generating {NUM_PRODUCTS} products...")

# 2. Generate mathematically realistic fake data
# Product IDs: widget_1, widget_2, etc.
product_ids = [f"widget_{i}" for i in range(1, NUM_PRODUCTS + 1)]

# Base Cost: Random prices between $5.00 and $150.00
base_costs = np.round(np.random.uniform(5.0, 150.0, NUM_PRODUCTS), 2)

# Competitor Price: We assume competitors mark up the base cost by 20% to 150%
markups = np.random.uniform(1.2, 2.5, NUM_PRODUCTS)
competitor_prices = np.round(base_costs * markups, 2)

sales = np.random.randint(100, 5001, NUM_PRODUCTS)

# 3. Build the Pandas DataFrame
df = pd.DataFrame({
    "product_id": product_ids,
    "base_cost": base_costs,
    "competitor_price": competitor_prices,
    "sales_last_30_days": sales
})

# 4. Save it as your large CSV
print("Saving to large_inventory.csv...")
df.to_csv("inventory.csv", index=False)

print("Done! You now have a massive dataset.")