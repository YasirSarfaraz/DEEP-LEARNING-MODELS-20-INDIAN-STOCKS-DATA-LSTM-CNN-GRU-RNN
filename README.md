# Indian Stocks Analysis Using Deep Learning

This project focuses on analyzing Indian stocks using deep learning techniques. The repository contains scripts to facilitate the analysis and prediction of stock prices. The analysis covers 20 Indian stocks from different sectors, ensuring a diverse representation of the market.

### List of 20 Indian Stocks Analyzed

- **Communication Services**: BHARTIARTL.NS, RELIANCE.NS, IDEA.NS, TATACOMM.NS
- **Consumer Cyclical**: TATAMOTORS.NS, M&M.NS, MARUTI.NS, EICHERMOT.NS
- **Energy**: RELIANCE.NS, ONGC.NS, IOC.NS, BPCL.NS
- **Healthcare**: SUNPHARMA.NS, DRREDDY.NS, CIPLA.NS, DIVISLAB.NS
- **Technology**: INFY.NS, TCS.NS, WIPRO.NS, HCLTECH.NS

## Project Structure

- **Data**: Contains CSV files for various Indian stocks. Each CSV file includes historical stock prices with columns for Date, Open, High, Low, Close, and Volume.
- **Notebooks**: 
  - `main2.ipynb`: Jupyter notebook for model training and evaluation.
- **Scripts**:
  - `down.py`: Script for downloading stock data.
- **Results**: Contains the output of the models, including predictions and comparisons.

## Data Preprocessing

The dataset is preprocessed using the following steps:

1. **Loading Data**:
   - The historical stock price data is read from CSV files.
   - The Date column is converted to a datetime format, and the data is sorted in ascending order.

2. **Feature Scaling**:
   - The 'Close' price column is normalized using MinMaxScaler with a range of (0,1) to ensure numerical stability during model training.

3. **Creating Time-Series Sequences**:
   - A sliding window approach is used where past `look_back` (default: 10) closing prices are taken as input features, and the next closing price is the target.
   - `X` contains sequences of past closing prices, and `y` contains the corresponding next closing price.

4. **Splitting Data**:
   - The dataset is divided into training (80%) and testing (20%) sets.
   - The training and testing data are reshaped into a 3D format for model compatibility (`samples, time steps, features`).

## Deep Learning Models Implemented

The following deep learning models are trained and evaluated:

- **LSTM (Long Short-Term Memory)**
- **GRU (Gated Recurrent Unit)**
- **Simple RNN**
- **1D CNN (Convolutional Neural Network)**

Each model is trained using the Adam optimizer and Mean Squared Error (MSE) loss function.

## Model Evaluation

The models are evaluated using the following metrics:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Percentage Error (MAPE)**
- **Normalized RMSE (NRMSE)**
- **R-squared Score (R2)**

The results are stored for each sector and company, along with the actual vs. predicted stock prices.

## Architecture of our 4 Different Models
![LSTM_architecture](https://github.com/user-attachments/assets/4d1ebe5f-1897-456b-8f14-b67d007214a2)
![CNN1D_architecture](https://github.com/user-attachments/assets/01afb392-f11b-4336-84b9-501ce80ed8c5)
![GRU_architecture](https://github.com/user-attachments/assets/119c0f5f-7885-45c1-9036-7a1e4a59399b)
![SimpleRNN_architecture](https://github.com/user-attachments/assets/f6e21fda-4c8f-47fb-8137-a53965da2b5d)






## Future Enhancements

- Implementing attention mechanisms to improve model performance.
- Experimenting with hybrid models combining LSTM and CNN.
- Incorporating external financial indicators for better prediction accuracy.

