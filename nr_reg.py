import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data for the UK
uk_agri_gdp = np.array([0.9361,0.84428,0.8198,0.75968,0.89219,0.85048,0.72846,0.54491,0.57063,0.56246,0.67444,0.67607,0.58667,0.68254,0.6284,0.63339,0.74501,0.63116,0.57891,0.59405,0.5711,0.60472])
uk_agri_emp = np.array([1.71811,1.55394,1.5345,1.39229,1.38576,1.24883,1.27648,1.37677,1.35243,1.366,1.08086,1.11042,1.21589,1.22025,1.18886,1.05877,1.25617,1.13845,1.12568,1.16305,1.07002,1.04726])

uk_manu_gdp = np.array([14.3906,13.7917,13.2766,12.4764,12.1154,11.5623,10.9497,10.5142,10.0758,9.67198,9.59092,9.07197,9.44532,9.32935,9.34636,9.59367,9.41066,9.29478,9.10985,9.05424,8.9524,8.79686])
uk_manu_emp = np.array([26.666,25.8117,25.1673,24.6399,23.9114,23.3405,22.3017,22.2158,22.0624,22.1885,22.0036,19.6111,19.2097,19.1774,19.0669,18.8671,18.9664,18.661,18.473,18.2612,18.1258,18.1228])

uk_serv_gdp = np.array([66.2019,66.3201,66.2698,67.4903,67.8038,68.3397,68.9567,69.2621,69.3723,69.6988,69.8204,71.8187,70.9063,70.2697,70.4436,69.9929,70.1935,70.4514,70.9308,70.7619,70.7486,70.973])
uk_serv_emp = np.array([71.6157,72.6343,73.2981,73.9677,74.7027,75.4105,76.4217,76.4073,76.585,76.4454,76.9154,79.2784,79.5743,79.6023,79.7442,80.0741,79.7773,80.2004,80.4012,80.5756,80.8041,80.8298])

# Linear regression calculations
slope_agri, intercept_agri, r_value_agri, p_value_agri, std_err_agri = linregress(uk_agri_gdp, uk_agri_emp)
slope_manu, intercept_manu, r_value_manu, p_value_manu, std_err_manu = linregress(uk_manu_gdp, uk_manu_emp)
slope_serv, intercept_serv, r_value_serv, p_value_serv, std_err_serv = linregress(uk_serv_gdp, uk_serv_emp)

# Plotting
plt.figure(figsize=(18, 6))

# Agriculture Sector
plt.subplot(1, 3, 1)
plt.scatter(uk_agri_gdp, uk_agri_emp, color='green', label='Agriculture Data')
plt.plot(uk_agri_gdp, intercept_agri + slope_agri*uk_agri_gdp, 'r', label=f'Linear fit: R²={r_value_agri**2:.2f}')
plt.title('UK Agriculture GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

# Manufacturing Sector
plt.subplot(1, 3, 2)
plt.scatter(uk_manu_gdp, uk_manu_emp, color='blue', label='Manufacturing Data')
plt.plot(uk_manu_gdp,intercept_manu + slope_manu*uk_manu_gdp, 'r', label=f'Linear fit: R²={r_value_agri**2:.2f}')
plt.title('UK Manufacturing GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

# Services Sector
plt.subplot(1, 3, 3)
plt.scatter(uk_serv_gdp, uk_serv_emp, color='purple', label='Services Data')
plt.plot(uk_serv_gdp, intercept_serv + slope_serv * uk_serv_gdp, 'r', label=f'Linear fit: R²={r_value_serv**2:.2f}')
plt.title('UK Services GDP vs Employment')
plt.xlabel('GDP (% of GDP)')
plt.ylabel('Employment (% of total)')
plt.legend()

plt.tight_layout()
plt.show()

