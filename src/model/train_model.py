from model.lstm import Model


class InitModel:

    def Init(ticker: str):
        print("... Training LSTM model")

        # 1 - call api 
        apkKey = "YOUR_API"
        Url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={apkKey}"
        # call
        data = ""

        # 2 - call preprocssing function

        train_x, train_y, test_x, test_y = preprocess_data(data)

        # 3- Train Model
        model = Model(
        train_x, train_y, test_x, test_y, ephocs=100, batch_size=32 
        )

        model = model.history()

        print("LSTM model trained [✔]")
        
        # return Model
        return model