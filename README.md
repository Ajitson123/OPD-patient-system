# Diabetes Statitical Analysis
## Applied Statistics on Real Clinical Data

###Overview
The project applies 18 core statistical concepts on the Pima Indians Diabetes Dataset (Kaggle).
As a medical graduate transitioning into health data science, I built this to bridge clinical knowledge with statistical analysis.
---
### Dataset
-**Source:** Kaggle - Pima Indians Diabetes Dataset
- **Patients:** 768 female patients
- **Features:** Glucose, BMI, Age, Pregnancies, Insulin, BloodPressure, SkinThickness, Outcome
- ---
### What This Project Covers
|chapter | Concept | Finding |
|1-3 | Histogram & Distribution | Glucose is right skewed |
| 4 | Mean, Median , Mode | Mean Glucose: 120.89 mg/dl|
| 5 | Std Dev & Variance | Glucose Std: 31.97|
| 6 | Z- Score & Outliers | 5 Outliers detected (glucose=0, missing data) |
| 7 | Z -Test | Sample mean significantly differs from normal population |
| 8 | T - Test | Diabetic ( 141.26 ) vs Non- diabetic (109.98) -p~0.00 |
| 9 | ANOVA | Glucose increases with age: Young > Middle > Elderly | 
| 10 | CI | 95% CI Glucose: [118.63, 123.16] |
| 11 | CLT | Confirmed on 1000 samples |

---
### Key Clinical Findings
**Glucose** is the strongest predictor of diabetes (r = 0.47)
- **BMI** is second strongest (r = 0.29)
- Elderly patients (50+) have significantly higher
- 5 patients have glucose = 0 - missing data issue requring processing before ML modeling
- **BloodPressure** is weakest predictor (r = 0.065) - likely drop before ML

- ### Tools Used
- Python, Pandas, Numpy
- Matplotlib, Seaborn
- Scipy (stats)

- ---
### Author
**Dr. Ajit ** - Medical Graduate | Aspiring Health Data Scients --- ML Engineer --- AI Health Tool Builder
MY ONEPIECE : Using clinical knowledge + data science + ai to build tool that solve real healthcare problems at scale in INDIA and BEYOND.
