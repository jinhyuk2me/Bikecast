![Banner](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/banner.png?raw=true)

<h3>👨‍💼 Team Lead</h3>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>GitHub</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Jinhyeok Jang</strong></td>
      <td>
        <a href="https://github.com/jinhyuk2me">
          <img src="https://img.shields.io/badge/github-jinhyuk2me-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        Project planning & ownership<br>
        DB schema design, deployment, and operation<br>
        SR_01: Real-time demand forecasting system<br>
        SR_02: Rental-station site recommendation engine
      </td>
    </tr>
  </tbody>
</table>

<h3>👥 Team Members</h3>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>GitHub</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Daein Kim</strong></td>
      <td>
        <a href="https://github.com/Daeinism">
          <img src="https://img.shields.io/badge/github-Daeinism-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        Weather data collection, analysis, and visualization<br>
        DB visualization & maintenance support<br>
        Backend features: SQL pipelines, altitude/distance calculation, API integration
      </td>
    </tr>
    <tr>
      <td><strong>Minsu Kim</strong></td>
      <td>
        <a href="https://github.com/kimminsu0519">
          <img src="https://img.shields.io/badge/github-kimminsu0519-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        Public-transit accessibility metric design<br>
        Transit ridership analysis and correlation validation<br>
        Documentation alignment, code cleanup, release checklist
      </td>
    </tr>
    <tr>
      <td><strong>Beomjin Kim</strong></td>
      <td>
        <a href="https://github.com/jbjj0708">
          <img src="https://img.shields.io/badge/github-jbjj0708-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        Hypothesis design for analysis<br>
        Public-data collection and curation<br>
        Data analysis and visualization
      </td>
    </tr>
  </tbody>
</table>

---

## 📚 Table of Contents

1. [Project Overview](#1-project-overview)  
2. [Tech Stack](#2-tech-stack)  
3. [Why This Project Matters](#3-why-this-project-matters)  
4. [Requirements (UR / SR)](#4-requirements)  
5. [Database Architecture & Sources](#5-database-architecture--sources)  
6. [EDA (Exploratory Data Analysis)](#6-eda-exploratory-data-analysis)  
7. [Feature Walkthrough](#7-feature-walkthrough)  
8. [Models & Performance](#8-models--performance)  
9. [Limitations](#9-limitations)  
10. [Directory Structure](#10-directory-structure)  

> 📄 Korean version: [`README.ko.md`](README.ko.md)

# 🚲 Bikecast: Demand Forecasting & Site Analytics for Seoul Bike

## 1. Project Overview

Bikecast is a data-analytics project that leverages **exploratory data analysis (EDA)** to implement two core capabilities for Seoul’s public bike service (Ddareungi): **usage demand forecasting** and **new station site recommendations**.

> **📅 Timeline: 24–27 March 2025**

![1-2](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/1-2.png?raw=true)

Even though four out of ten Seoul citizens regularly ride Ddareungi, many stations still experience chronic shortage or surplus issues.

The service is operated in a **one-way rental** model—users can pick up a bike anywhere and drop it off elsewhere. As a result, some stations repeatedly run dry while others amass unused bikes.

| Operational Pain Point | Description |
|------------------------|-------------|
| Bike shortage | Stations that are always under-supplied relative to demand |
| Bike surplus | Stations where bikes get dropped off but rarely collected |
| Poor surge response | No proactive way to react to time-specific spikes |

Current operations mostly rely on **after-the-fact redistribution** once thresholds are exceeded. Because there is **no predictive component**, it is hard to react quickly to sudden changes in demand.

---

## 2. Tech Stack

| Category | Technologies | Badges |
|----------|-------------|--------|
| **Environment** | Linux (Ubuntu)<br>VS Code<br>Jupyter Notebook | ![Linux](https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)<br>![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)<br>![Jupyter](https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) |
| **Language** | Python | ![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Data Analysis** | Pandas<br>Matplotlib<br>Seaborn<br>GeoPandas | ![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)<br>![Matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)<br>![Seaborn](https://img.shields.io/badge/seaborn-4B8BBE?style=for-the-badge&logo=python&logoColor=white)<br>![GeoPandas](https://img.shields.io/badge/Geopandas-139C5A?style=for-the-badge&logo=geopandas&logoColor=white) |
| **Modeling** | XGBoost<br>scikit-learn | ![XGBoost](https://img.shields.io/badge/xgboost-FF6600?style=for-the-badge&logo=apache&logoColor=white)<br>![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |
| **Database** | MySQL<br>AWS RDS | ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)<br>![AWS](https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white) |
| **Visualization** | Folium | ![Folium](https://img.shields.io/badge/folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white) |
| **UI** | PyQt5 | ![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white) |
| **Version Control** | Git / GitHub | ![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) |
| **Collaboration** | Confluence<br>Jira<br>Slack | ![Confluence](https://img.shields.io/badge/confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white)<br>![Jira](https://img.shields.io/badge/jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)<br>![Slack](https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) |

---

## 3. Why This Project Matters

```🕒🚲 Put bikes where and when they are needed```

To eliminate inefficiencies in Seoul Bike operations we need **data-driven demand forecasting** and **actionable operating strategies** built on top of those insights.

1. Build a high-fidelity **demand forecasting model** that reflects weather, elevation, population, transit access, and more.  
2. Implement two functions on top of the model:
   - **Station- and time-specific forecasts** for proactive redistribution.
   - **Location-based demand estimation** for recommending new station sites.

> 🎯 **Ultimate goal**: Predict “where and when bikes will be needed” and make the public-bike system radically more efficient.

---

## 4. Requirements

User requirements (UR) were translated into the two core system requirements (SR) that drive development.

| User Requirement (UR) | Description |
|-----------------------|-------------|
| UR_01 | Riders should be able to request demand forecasts per station and time slot. |
| UR_02 | Operators should receive recommendations for new station sites with high expected usage. |

| System Requirement (SR) | Description |
|-------------------------|-------------|
| SR_01 | Predict hourly rentals for a specific station based on time and environmental signals. |
| SR_02 | Recommend candidate locations using spatial and contextual features. |

---

## 5. Database Architecture & Sources

We gathered and unified multi-source data to capture spatio-temporal factors that influence demand. Every dataset feeds directly into EDA, feature engineering, hypothesis testing, and model inputs.

### 5-1. Data Sources

- **Seoul Open Data**: rental logs, floating population, commercial-district info, income distribution, contour data.  
- **KMA Data Portal & API**: temperature, rainfall, wind speed, and other weather metrics.  
- **Public Data Portal**: subway/bus ridership.  
- **Google API**: elevation per station.  

### 5-2. Database Layout

![ERD](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/4-1.png?raw=true)

The schema is modular so that tables can be joined per analysis need. Data feeds fall into four groups:

- **Location**: boroughs, districts, station coordinates.  
- **Demand**: per-month / per-day / per-hour rental volumes.  
- **Temporal features**: date, weekday, holidays, weather metrics (temperature, rainfall, etc.).  
- **Spatial features**: floating population, transit accessibility, company counts, elevation, commercial info.  

### 5-3. Integration & Preprocessing

All datasets live on **AWS RDS MySQL**. The **`rental` table** stores **44,543,263 records** from 2024 and acts as the primary source. Weather, population, transit, and commercial tables are stored separately and fetched with SQL per analysis need.

For EDA or modeling, we query each table, convert the result into Pandas DataFrames, and then perform joins, preprocessing, and feature engineering.

For training, we rely on a dedicated learning table inside MySQL. It uses **[rental timestamp, station ID]** as the primary key, already includes preprocessed features, and can be consumed directly from the model pipeline.

> 📌 The `rental` table is the **starting point** for both EDA and training datasets, anchoring every demand-pattern analysis and forecast design.

---

## 6. EDA (Exploratory Data Analysis)

### 6.1 Method & Feature Selection

Using the integrated dataset (all **44,543,263 rentals from 2024**), we performed EDA to identify the factors that shape public-bike demand. This step kick-starts feature selection and validates real-world hypotheses.

Two axes guided the analysis:

> “Bike usage is determined by the following factors.”

1. **Temporal & environmental features**: time slot, temperature, rainfall, humidity, etc.  
2. **Spatial & locational features**: elevation, transit access, population, number of businesses, etc.  

| Temporal & Environmental | Spatial & Locational |
|-------------------------|----------------------|
| Time of day             | Proximity to transit  |
| Holidays                | Transit ridership     |
| Day of week             | Floating population   |
| Temperature             | Industrial & employment density |
| Rainfall                | Income level          |
| Humidity                | Commercial density (shops) |
| Wind speed              | Bike infrastructure (bike lanes) |
| Solar radiation         | Leisure infra (parks) |

The analysis confirmed that weather (temperature, rainfall) plus spatial factors (elevation, transit access) significantly impact demand. These findings steered feature selection for the models.

### 6.2 XGBoost & Automatic Feature Selection

`XGBoost` evaluates **feature importance** during training, drops low-importance variables, and focuses on what matters most. The features derived during EDA were fed into the model to maximize accuracy.

- **Feature importance** quantifies each variable’s contribution, pruning unnecessary inputs automatically.  
- **Interpretability** lets us inspect which features influenced predictions, aiding operations.

EDA and XGBoost reinforce each other: hypotheses produce candidate features; XGBoost prioritizes them to improve accuracy.

- For **SR_01**, time-of-day, temperature, rainfall, weekday, and wind speed are key inputs, enabling us to capture sudden drops/spikes tied to weather.  
- For **SR_02**, elevation, transit accessibility, and floating population help estimate location-level demand. Areas that are low in elevation and well-connected to transit tend to show higher demand and are surfaced as site candidates.

### 6.3 Linking EDA Findings to Modeling

#### ⏱️ Hypothesis Group A: Temporal & Environmental Factors

---

### 🧪 Hypothesis A-1. “Usage varies heavily by time of day.”

- Aggregated demand by hour, weekday, and month.  
- Identified peaks during commute hours, on Fridays, and during spring/fall.

![시간대](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/5-2.png?raw=true)  
![주중vs주말](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-3.png?raw=true)  
![평일vs휴일](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-4.png?raw=true)  
![요일별](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-5.png?raw=true)  
![계절별](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-6.png?raw=true)

**Findings**
- Sharp surges at 7–9 am and 5–7 pm.  
- Weekdays > weekends, with Friday being the busiest.  
- Spring/Fall > Summer/Winter.  
→ Adopted as a key feature group for **SR_01**.

---

### 🧪 Hypothesis A-2. “Weather strongly impacts usage.”

- Analyzed temperature, rainfall, humidity, and solar radiation.  
- Assessed feasibility of real-time integration with the national weather API.

![기온](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-7.png?raw=true)  
![강수량](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-8.png?raw=true)  
![습도](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-9.png?raw=true)  
![일사량](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-10.png?raw=true)

**Findings**
- Demand peaks around 22 °C.  
- Rain immediately suppresses usage.  
- More sunshine boosts demand; humidity above 80% lowers it.  
→ Fed directly into **SR_01**.

---

#### 📍 Hypothesis Group B: Spatial & Locational Factors

---

### 🧪 Hypothesis B-1. “Higher elevation → lower demand.”

- Compared station elevation to average rentals.

![고도1](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-11.png?raw=true)  
![고도2](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-12.png?raw=true)  
![고도3](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-13.png?raw=true)

**Findings**
- Demand drops as elevation increases.  
→ Used as an **SR_02** feature.

---

### 🧪 Hypothesis B-2. “Closer to transit = higher demand.”

- Measured the distance between each station and the nearest subway/bus stop.

![교통 거리](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-15.png?raw=true)

**Findings**
- Demand decreases as distance grows.  
→ Adopted for **SR_02**.

---

### 🧪 Hypothesis B-3. “Transit ridership near the station matters.”

- Compared station demand to ridership at the nearest subway/bus stop.

![교통 이용량](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-24.png?raw=true)

**Findings**
- Higher nearby transit ridership correlates with higher bike demand.  
→ Included in **SR_02**.

---

### 🧪 Hypothesis B-4. “More floating population → higher demand.”

- Mapped floating population per borough to station demand.

![생활인구](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-17.png?raw=true)

**Findings**
- Strong positive correlation.  
→ Used for **SR_02**.

---

### 🧪 Hypothesis B-5. “Proximity to parks ignites demand.”

- Compared the number of parks per borough to rentals.

![공원수](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-22.png?raw=true)

**Findings**
- More parks → more demand.  
→ Fed into **SR_02**.

---

### 🧪 Hypothesis B-6. “Industrial & employment density drives demand.”

- Analyzed business counts and employee numbers vs. demand (borough/district level).

![산업1](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-18.png?raw=true)  
![산업2](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-19.png?raw=true)  
![산업3](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-20.png?raw=true)  
![산업4](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-21.png?raw=true)

**Findings**
- Industrial clusters coincide with higher demand.  
→ Incorporated into **SR_02**.

---

### 🧪 Hypothesis B-7. “More bike lanes → more demand.”

- Compared the number of bike-lane routes per borough to rentals.

![자전거도로](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-23.png?raw=true)

**Findings**
- Bike-lane density correlates with higher demand.  
→ Adopted for **SR_02**.

---

## 7. Feature Walkthrough

### 🚴‍♀️ SR_01 — Station-level, time-based demand forecasts

- Regression model powered by XGBoost.  
- Inputs: station ID, date, time slot, temperature, wind speed, etc. Weather forecasts for **today / tomorrow / day after** are pulled automatically via the KMA API.  
- Output: predicted rental count per time slot (displayed live in the GUI).  
- Training size: **8,022 samples**.

![SR_01_출력화면](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-1.png?raw=true)

### 🗺 SR_02 — Recommend new station sites

- Generate grid-based candidate points inside the user-defined bounding box.  
- Apply the spatial-demand model to each candidate.  
- Visualize the top-N predicted locations on a Folium map.  
- Example input:  
  `[Input] right_bottom = (37.5600, 126.9700), left_top = (37.5700, 126.9800), limit = 200, n = 3`  
- Modeling approach: 3-stage XGBoost regression (trained separately on low / mid / high demand ranges).

![SR_02_출력화면](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-2.png?raw=true)

---

## 8. Models & Performance

Bikecast focuses on **time-based demand forecasting (SR_01)** and **location-based site recommendations (SR_02)**. Both use XGBoost regressors, and we evaluated them with RMSE, MAE, (S)MAPE, and R².

### 📍 SR_01: Hourly demand forecasting

This feature predicts demand per station/time slot so we can rebalance bikes proactively.

- **Model**: XGBoost regression.  
- **Inputs**: date, time, temperature, wind speed, rainfall, humidity, elevation, weekday, etc.  
- **Target**: rentals per time slot.

![모델](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/7-1.png?raw=true)

| Metric | Value |
|--------|-------|
| RMSE | 9.60 |
| MAE  | 6.66 |
| MAPE | 23.24% |
| R²   | 0.835 |

- Overall R² = 0.835; within the practical range (rentals > 10) it rises to 0.860.  
- Confirms that temporal/weather features adequately explain demand variance.  
- Provides sufficient accuracy to drive SR_01 in real-time operations.

### 🗺 SR_02: Site recommendation

This feature estimates relative demand for potential new stations.

- **Model**: 3-stage XGBoost regression trained separately on low/mid/high segments.  
- **Inputs**: latitude, longitude, elevation, residential/floating population, transit access, number of shops, etc.  
- **Target**: predicted daily demand peak.

![모델](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/7-2.png?raw=true)

| Metric | Value |
|--------|-------|
| RMSE  | 20.49 |
| MAE   | 12.60 |
| MAPE  | 41.59% |
| SMAPE | 33.96% |
| R²    | 0.761 |

- Segmenting by demand range helps, but high-demand areas are still harder to predict.  
- Certain special-purpose zones cannot be fully explained using the current feature set.  
- Works best as a **relative ranking** metric rather than an absolute predictor.  
- Useful as a first-pass filter when deciding where to invest in new stations.

> [!Note]
> Even with limited features, R² = 0.761 shows that spatial signals alone can explain a significant portion of demand variation. Future improvements could combine private datasets or incorporate additional features unique to high-demand hot spots.

---

## 9. Limitations

### 9-1. Structural challenges when forecasting high-demand stations

- Certain stations exhibit **non-linear spikes** once multiple features cross specific thresholds.  
- Even though XGBoost can model non-linear behavior, such sharp swings remain difficult to capture.  
- External factors (landmarks, events, brand recognition) may also drive demand but are not in our features.

> **Implication**: We need external POI/event data or higher-capacity models to fully cover crowd-favorite stations.

### 9-2. Public-data constraints

#### Data resolution
- Many public APIs have coarse temporal/spatial granularity, forcing us to downscale some analyses from district level to borough level.  

#### Manual preprocessing
- Coordinate systems and administrative codes often mismatch, so we had to manually correct datasets before merging.  

#### Lack of private depth
- Public data has lower freshness and resolution than commercial sources (e.g., Kakao, T-map, SKT mobility data).  
- This constrains precision. Integrating private APIs would improve overall fidelity.

> **Implication**: The quality of public datasets directly limits prediction accuracy. A hybrid approach with private mobility/intelligence data would dramatically raise precision.

---

## 10. Directory Structure

The repository is split into three top-level directories aligned with the data lifecycle: collection → analysis → service implementation.

```
📦 Project Root
├── data_collection     # Scripts for public-data ingestion & preprocessing
├── data_analysis       # EDA notebooks, feature studies, visualization
├── service             # Training/inference pipelines and user-facing features (SR_01 / SR_02)
```

### 📁 data_collection
Public/open-data ingestion and preprocessing scripts.

### 📁 data_analysis
EDA notebooks for pattern discovery, feature selection, and visualization. Model training is handled separately under `service`.

### 📁 service
Core execution directory containing training code, inference scripts, and the SR_01/SR_02 applications.

```📌 The entire workflow flows from data collection → exploratory analysis → model training & feature delivery. Each directory maps to that lifecycle for easier maintenance.```
