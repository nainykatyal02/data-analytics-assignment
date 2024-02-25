import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data for China
china_agri_gdp = np.array([17.159,16.0647,14.6762,13.9834,13.3014,12.3489,12.9166,11.6414,10.6257,10.2461,10.169,9.63618,9.32517,9.17765,9.11371,8.94289,8.64349,8.38701,8.05728,7.46356,7.04302,7.14369])
china_agri_emp = np.array([49.8,50.1,50.01,50.0099,50.01,49.1,46.8999,44.8,42.6,40.8,39.5999,38.0999,36.7,34.8,33.6,31.3999,29.4999,28.5917,27.7,26.98,26.0337,25.307])

china_manu_gdp = np.array([31.0387,31.197,31.3553,31.5137,31.672,31.8303,31.975,32.0939,32.4523,32.3833,32.1194,31.5962,31.6128,32.0647,31.5285,30.671,30.3964,28.9516,28.0694,28.1089,27.841,26.7747])
china_manu_emp = np.array([23.5002,23.0002,22.4956,22.2955,21.3958,21.5998,22.4995,23.8,25.1996,26.7999,27.1998,27.8,28.7001,29.5,30.2998,30.1,29.9006,29.1807,28.8004,28.1075,27.598,27.4244])

china_serv_gdp = np.array([37.0433,38.5753,39.7876,41.2231,42.2479,42.0282,41.1831,41.3359,41.8168,42.8696,42.8597,44.4066,44.1769,44.293,45.4633,46.8804,48.2709,50.7716,52.362,52.6847,53.2699,54.2689])
china_serv_emp = np.array([26.6997,26.8997,27.4943,27.6945,28.5941,29.3001,30.6004,31.3998,32.2003,32.4,33.2001,34.0999,34.5999,35.6999,36.1001,38.4999,40.5993,42.2274,43.4995,44.9124,46.3682,47.2684])

# Linear regression calculations
slope_agri, intercept_agri, r_value_agri, p_value_agri, std_err_agri = linregress(china_agri_gdp, china_agri_emp)
slope_manu, intercept_manu, r_value_manu, p_value_manu, std_err_manu = linregress(china_manu_gdp, china_manu_emp)
slope_serv, intercept_serv, r_value_serv, p_value_serv, std_err_serv = linregress(china_serv_gdp, china_serv_emp)

# Plotting
plt.figure(figsize=(18, 6))

# Agriculture Sector
plt.subplot(1, 3, 1)
plt.scatter(china_agri_gdp, china_agri_emp, color='green', label='Agriculture Data')
plt.plot(china_agri_gdp, intercept_agri + slope_agri*china_agri_gdp, 'r', label=f'Linear fit: R²={r_value_agri**2:.2f}')
plt.title('China Agriculture GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

# Manufacturing Sector
plt.subplot(1, 3, 2)
plt.scatter(china_manu_gdp, china_manu_emp, color='blue', label='Manufacturing Data')
plt.plot(china_manu_gdp,intercept_manu + slope_manu*china_manu_gdp, 'r', label=f'Linear fit: R²={r_value_manu**2:.2f}')
plt.title('China Manufacturing GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

# Services Sector
plt.subplot(1, 3, 3)
plt.scatter(china_serv_gdp, china_serv_emp, color='purple', label='Services Data')
plt.plot(china_serv_gdp, intercept_serv + slope_serv * china_serv_gdp, 'r', label=f'Linear fit: R²={r_value_serv**2:.2f}')
plt.title('China Services GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

plt.tight_layout()
plt.show()
