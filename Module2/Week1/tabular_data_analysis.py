import numpy as np
import pandas as pd
df = pd.read_csv('advertising.csv')
data = df.to_numpy()

# Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales
sales_data = data[:, 3] # lấy giá trị tất cả các dòng ở cột 3_Sales
max_sales = np.max(sales_data)
max_index = np.argmax(sales_data)
print(max_sales, max_index)

# Tính Giá trị trung bình của cột TV
tv_data = data[:, 0]
print(tv_data[:10])
avg_tv = tv_data.mean()
print(avg_tv)

# Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20

sales_data = data[:, 3] >= 20
sales_count = np.sum(sales_data)
print(sales_count)

# Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng trên cột Sales lớn hơn hoặc bằng 15:
sales_data_15 = data[:, 3] >= 15
radio_data = data[:, 1]
avg_radio = radio_data[sales_data_15].mean()
print(avg_radio)

# Calculate the total values of Sales (Condition: Newpaper > the average value of all numbers in Newpaper)
newpaper_data = data[:, 2]
newpaper_mean = newpaper_data.mean()
newpaper_cond = newpaper_data > newpaper_mean
sales_data = data[:, 3]
sales_cond = sales_data * newpaper_cond
sales_sum = np.sum(sales_cond)
print(sales_sum)

# Create new array that contains three values : Good, Average, Bad
# Value > the average of Sales => Good, < => Bad, = => Average
sales_data = data[:, 3]
sales_mean = sales_data.mean()
score_sales = np.where(sales_data > sales_mean, 'Good', np.where(sales_data == sales_mean, 'Average', 'Bad'))
print(score_sales[7:10])

# Create new array that contains three values : Good, Average, Bad
# Value > the closest value to the average of Sales => Good, < => Bad, = => Average

sales_data = data[:, 3]
sales_mean = sales_data.mean()
print("Sales_mean:", sales_mean)
sub_mean = sales_data - sales_mean
sub_abs = abs(sales_data - sales_mean)
avarage_index = np.argmin(sub_abs)
sales_average = sales_data[avarage_index]
print("Sales_average:", sales_average)
score_sales = np.where(sales_data > sales_average, 'Good', np.where(sales_data == sales_average, 'Average', 'Bad'))
print(score_sales[7:10])