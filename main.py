from fastapi import FastAPI
from pydantic import BaseModel, Field
from scipy.optimize import minimize
from data_layer import get_product_data

app = FastAPI()

class PricingRequest(BaseModel):
    product_id: str

@app.post("/api/v1/optimize-price")
def OptimizePrice(data: PricingRequest):
    market_data = get_product_data(data.product_id)

    if market_data is None:
        return {"error" : "Product not found"}
    
    def profit_function(x):
        price = x[0]
        demand = (1000 * market_data["demand_multiplier"]) - (50 * (price - market_data["competitor_price"]))
        demand = max(0,demand)
        
        profit = -(price - market_data["base_cost"]) * demand      #I added -ve sign so that minimize func calculates the maximum

        return profit

    function_bounds = [(market_data["base_cost"], 2 * market_data["competitor_price"])]

    initial_guess = [market_data["competitor_price"]]

    result = minimize(profit_function, x0 = initial_guess, bounds = function_bounds)

    return {
        "product id" : data.product_id,
        "base cost" : market_data["base_cost"],
        "competitor price" : market_data["competitor_price"],
        "optimized price" : round(result.x[0],2),
        "expected profit" : round(-result.fun, 2)
    }
