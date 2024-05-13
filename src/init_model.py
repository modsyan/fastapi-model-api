from model.lstm import Model


class InitModel:

    def Init():
        print("... Training LSTM model")
        model = Model.train()
        print("LSTM model trained [✔]")

        return model
