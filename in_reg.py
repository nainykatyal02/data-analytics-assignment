import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data for India
india_agri_gdp = np.array([24.1804,22.9725,21.611,21.6188,19.5345,19.5919,17.8146,17.6202,16.8094,16.7501,16.7909,16.7442,17.0265,17.1919,16.8453,17.1484,16.7919,16.1745,16.3638,16.5583,16.0316,16.7555])
india_agri_emp = np.array([60.6871,60.1066,59.6447,59.0859,58.4438,57.7151,56.7587,55.9982,55.0998,54.1719,53.3906,52.475,51.5153,49.2577,47.0042,46.4277,45.7835,45.1593,44.5213,43.9396,43.3288,41.3873])

india_manu_gdp = np.array([15.7193,15.1805,15.927,15.307,15.5587,15.5873,15.8272,15.973,17.3036,16.8645,17.0986,17.1435,17.0299,16.1393,15.8169,15.253,15.0655,15.5838,15.1622,15.0182,14.8815,13.4558])
india_manu_emp = np.array([15.9608,16.1601,16.3199,16.6609,17.0754,17.5571,18.2789,18.8042,19.3712,19.9962,20.5327,21.1169,21.8091,23.1109,24.355,24.4331,24.5279,24.5838,24.7128,24.8462,24.9491,25.3691])

india_serv_gdp = np.array([40.1325,41.9657,42.7329,43.8089,44.7288,44.7046,44.1148,44.4429,44.0432,44.0081,45.8825,45.9848,45.0337,45.4421,46.3011,46.6987,47.8224,47.7837,47.7494,47.6708,48.4315,50.0849])
india_serv_emp = np.array([23.3519,23.7331,24.0353,24.253,24.4807,24.7277,24.9622,25.1975,25.5289,25.8318,26.0766,26.408,26.6755,27.6312,28.6406,29.139,29.6889,30.2567,30.7658,31.2141,31.722,33.2434])

# Linear regression calculations
slope_agri, intercept_agri, r_value_agri, p_value_agri, std_err_agri = linregress(india_agri_gdp, india_agri_emp)
slope_manu, intercept_manu, r_value_manu, p_value_manu, std_err_manu = linregress(india_manu_gdp, india_manu_emp)
slope_serv, intercept_serv, r_value_serv, p_value_serv, std_err_serv = linregress(india_serv_gdp, india_serv_emp)

# Plotting
plt.figure(figsize=(18, 6))

# Agriculture Sector
plt.subplot(1, 3, 1)
plt.scatter(india_agri_gdp, india_agri_emp, color='green', label='Agriculture Data')
plt.plot(india_agri_gdp, intercept_agri + slope_agri*india_agri_gdp, 'r', label=f'Linear fit: R²={r_value_agri**2:.2f}')
plt.title('India Agriculture GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

# Manufacturing Sector
plt.subplot(1, 3, 2)
plt.scatter(india_manu_gdp, india_manu_emp, color='blue', label='Manufacturing Data')
plt.plot(india_manu_gdp,intercept_manu + slope_manu*india_manu_gdp, 'r', label=f'Linear fit: R²={r_value_manu**2:.2f}')
plt.title('India Manufacturing GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

# Services Sector
plt.subplot(1, 3, 3)
plt.scatter(india_serv_gdp, india_serv_emp, color='purple', label='Services Data')
plt.plot(india_serv_gdp, intercept_serv + slope_serv * india_serv_gdp, 'r', label=f'Linear fit: R²={r_value_serv**2:.2f}')
plt.title('India Services GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

plt.tight_layout()
plt.show()
