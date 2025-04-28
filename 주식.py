import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# 주식 데이터 다운로드
data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

# 매매 신호 생성
data['Signal'] = 0
data['Signal'][50:] = np.where(data['SMA50'][50:] > data['SMA200'][50:], 1, 0)
data['Position'] = data['Signal'].diff()

# 그래프 그리기
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA50'], label='50-Day SMA')
plt.plot(data['SMA200'], label='200-Day SMA')
plt.plot(data[data['Position'] == 1].index, data['SMA50'][data['Position'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, data['SMA50'][data['Position'] == -1], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.title('AAPL Price with Buy/Sell Signals')
plt.legend()
plt.show()
