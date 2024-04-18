import matplotlib.pyplot as plt

# Input data (these could be collected via user input in an actual lab setup)
dates = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
    '2021-01-06'
]
prices = [150, 152, 149, 157, 153, 158]


# Calculate moving average
def calculate_moving_average(prices, window_size):
    moving_averages = []
    i = 0
    while i < len(prices) - window_size + 1:
        this_window = prices[i:i + window_size]
        window_average = sum(this_window) / window_size
        moving_averages.append(window_average)
        i += 1
    return moving_averages


moving_average = calculate_moving_average(prices, 2)

# Adjusting date array to align with moving averages
# adjusted_dates = dates[1:-1]  # Adjust according to the window size
adjusted_dates = dates[1:]  # Adjust according to the window size

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, marker='o', label='Actual Prices')
plt.plot(adjusted_dates,
         moving_average,
         marker='x',
         linestyle='--',
         label='2 Day Moving Average')
plt.title('Stock Price Trends')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.savefig('/mnt/c/Users/mjovanovich/output.png')
