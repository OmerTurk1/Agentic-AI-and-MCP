import pandas as pd
import matplotlib.pyplot as plt

# Verilerin Yüklenmesi
# CSV dosyanızın yolunu buraya yazın
data = pd.read_csv('./mcp_workspace/THY Stock Price History.csv')

# Tarih sütununun datetime formatına çevrilmesi
data['Date'] = pd.to_datetime(data['Date'])

# Verilerin Görselleştirilmesi
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Price'], label='Close Price')
plt.title('THY Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price (TL)')
plt.legend()
plt.grid()
plt.show()