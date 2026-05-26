# Dynamic Pricing Optimization Engine

A high-performance, data-driven microservice that calculates the mathematically optimal price for products to maximize profit. Built with **FastAPI**, this engine leverages **Pandas** and **PyArrow** for high-speed in-memory data caching, and **SciPy** to compute multivariate optimization bounds based on real-time market conditions.

---

## Architecture

The project is organized into three core layers:

1. **Data Layer (`data_layer.py`)** — Uses PyArrow to load a highly compressed Parquet database into RAM on server boot. This eliminates disk I/O bottlenecks and enables the API to filter hundreds of thousands of rows in milliseconds using Pandas Boolean indexing.

2. **Optimization Engine (`main.py`)** — Uses SciPy's `minimize` algorithm to locate the exact peak of a profit parabola. It balances base costs, dynamic demand multipliers, and competitor pricing to determine the absolute maximum profit margin.

3. **API Routing (`main.py`)** — Served via FastAPI and secured with Pydantic data validation.

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.12+ |
| Web Framework & Server | FastAPI, Uvicorn |
| Mathematical Optimization | SciPy |
| Data Engineering & Caching | Pandas, PyArrow |
| Synthetic Data Generation | NumPy |

---

## Getting Started

Follow the steps below to generate the synthetic database, convert it for high-speed access, and start the API server.

### 1. Clone and Set Up the Environment

```bash
git clone https://github.com/Yash49-Xe/dynamic-pricing-engine.git
cd dynamic-pricing-engine

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pydantic scipy pandas pyarrow numpy
```

### 2. Generate the Database

Do not supply an external CSV file. Run the included generator script to synthesize 100,000 realistic products, complete with base costs, competitor markups, and historical sales data.

```bash
python generate_data.py
```

### 3. Convert to Parquet

Convert the raw CSV into a highly compressed, column-oriented Parquet file for instant RAM caching on server boot.

```bash
python convert.py
```

### 4. Start the Server

```bash
python -m uvicorn main:app --reload
```

---

## API Reference

Once the server is running, navigate to `http://127.0.0.1:8000/docs` to access the interactive Swagger UI, or send requests directly to the endpoint below.

### Endpoint

```
POST /api/v1/optimize-price
```

### Request Body

The client submits only the product ID. All data extraction and computation are handled securely on the backend.

```json
{
  "product_id": "widget_84291"
}
```

### Response

```json
{
  "product_id": "widget_84291",
  "base_cost": 15.0,
  "competitor_price": 30.0,
  "optimized_price": 34.5,
  "expected_profit": 19012.5
}
```