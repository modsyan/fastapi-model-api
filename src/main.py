import fastapi
from init_model import InitModel

# services initialization
model = InitModel.Init()

# start server
app = fastapi.FastAPI()

@app.get("/api/stock/predict/")
def stockPredict(ticker: str):
  result = model.predict(str.ticker)
  return {"ticker": result}
