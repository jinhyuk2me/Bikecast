![배너](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/banner.png?raw=true)



<h3>👨‍💼 팀장</h3>

<table>
  <thead>
    <tr>
      <th>이름</th>
      <th>GitHub</th>
      <th>역할</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>장진혁</strong></td>
      <td>
        <a href="https://github.com/jinhyuk2me">
          <img src="https://img.shields.io/badge/github-jinhyuk2me-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        프로젝트 기획 및 총괄<br>
        DB 설계, 구축, 관리<br>
        실시간 수요 예측 시스템 개발 (SR_01)<br>
        설치 위치 추천 시스템 개발 (SR_02)
      </td>
    </tr>
  </tbody>
</table>

<h3>👥 팀원</h3>

<table>
  <thead>
    <tr>
      <th>이름</th>
      <th>GitHub</th>
      <th>역할</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>김대인</strong></td>
      <td>
        <a href="https://github.com/Daeinism">
          <img src="https://img.shields.io/badge/github-Daeinism-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        날씨 데이터 수집·분석·시각화<br>
        DB 시각화, 관리 보완<br>
        백엔드 기능 개발: SQL, 고도/거리 계산, API 연동
      </td>
    </tr>
    <tr>
      <td><strong>김민수</strong></td>
      <td>
        <a href="https://github.com/kimminsu0519">
          <img src="https://img.shields.io/badge/github-kimminsu0519-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        대중교통 접근성 지표 설계<br>
        교통 이용량 분석 및 상관관계 검증<br>
        문서 통일, 코드 정리, 배포 전 검토
      </td>
    </tr>
    <tr>
      <td><strong>김범진</strong></td>
      <td>
        <a href="https://github.com/jbjj0708">
          <img src="https://img.shields.io/badge/github-jbjj0708-181717?style=flat-square&logo=github&logoColor=white">
        </a>
      </td>
      <td>
        분석 가설 수립<br>
        공공데이터 수집 및 정제<br>
        데이터 분석 및 시각화
      </td>
    </tr>
  </tbody>
</table>

---

## 📚 목차

1. [프로젝트 개요](#1-프로젝트-개요)  
2. [기술 스택](#2-기술-스택)  
3. [프로젝트 목적 / 필요성](#3-프로젝트-목적--필요성)  
4. [요구사항 정의 (UR / SR)](#4-요구사항-정의)  
5. [데이터베이스 구성 및 출처](#5-데이터베이스-구성-및-출처)  
6. [EDA (탐색적 데이터 분석)](#6-eda-탐색적-데이터-분석)  
7. [기능 설명](#7-기능-설명)  
8. [모델 설명 및 성능 평가](#8-모델-설명-및-성능-평가)  
9. [한계점](#9-한계점)  
10. [디렉토리 구조](#10-디렉토리-구조)  


> 📄 English version: [`README.en.md`](README.en.md)

# 🚲 Bikecast: 서울시 공공자전거 수요 예측 및 분석

## 1. 프로젝트 개요

이 프로젝트는 **탐색적 데이터 분석(EDA)** 을 기반으로, 서울시 공공자전거 서비스인 **따릉이**의 **수요 예측**과 **신규 대여소 설치 위치 추천** 기능을 구현하기 위한 데이터 분석 프로젝트입니다.

> **📅 프로젝트 기간: 2025.03.24 ~ 2025.03.27**

![1-2](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/1-2.png?raw=true)

서울시 따릉이는 현재 서울시민 10명 중 4명이 이용할 정도로 일상에 깊숙이 자리 잡은 교통수단이지만, **대여소별 자전거 부족 문제**는 여전히 해결되지 않은 과제로 남아 있습니다.

따릉이는 **One-Way 방식**으로 운영되어, 사용자가 **어디서든 대여하고 다른 곳에 반납**할 수 있습니다. 이러한 구조로 인해 특정 대여소에서는 **공급 부족**, 다른 대여소에서는 **자전거 과잉** 문제가 반복적으로 발생합니다.

| 운영상 문제점 | 설명 |
|---------------|------|
| 자전거 부족 | 수요 대비 공급이 항상 모자란 대여소 |
| 자전거 과잉 | 자전거가 반납만 되고 회수되지 않는 대여소 |
| 급변 대응 한계 | 특정 시간대 수요 폭증 시 실시간 대응 불가 |

현재는 수량 기준 초과/미달 상황에 따라 자전거를 회수하거나 옮기는 **사후적 대응 방식**으로만 운영되고 있으며, 이는 **예측이 없는 수동적 운영**이기 때문에 **실시간 수요 변화에 선제적으로 대응하기 어려운 구조**입니다.

---

## 2. 기술 스택

| 분류 | 기술 | 배지 |
|------|------|------|
| **개발환경** | Linux (Ubuntu)<br>VS Code<br>Jupyter Notebook | ![Linux](https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)<br>![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)<br>![Jupyter](https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) |
| **언어** | Python | ![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **데이터 분석** | Pandas<br>Matplotlib<br>Seaborn<br>GeoPandas | ![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)<br>![Matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)<br>![Seaborn](https://img.shields.io/badge/seaborn-4B8BBE?style=for-the-badge&logo=python&logoColor=white)<br>![GeoPandas](https://img.shields.io/badge/Geopandas-139C5A?style=for-the-badge&logo=geopandas&logoColor=white) |
| **모델링** | XGBoost<br>scikit-learn | ![XGBoost](https://img.shields.io/badge/xgboost-FF6600?style=for-the-badge&logo=apache&logoColor=white)<br>![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |
| **DB** | MySQL<br>AWS RDS | ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)<br>![AWS](https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white) |
| **시각화** | Folium | ![Folium](https://img.shields.io/badge/folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white) |
| **UI** | PyQt5 | ![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white) |
| **형상 관리** | Git / GitHub | ![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) |
| **협업 도구** | Confluence<br>Jira<br>Slack | ![Confluence](https://img.shields.io/badge/confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white)<br>![Jira](https://img.shields.io/badge/jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)<br>![Slack](https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) |


---

## 3. 프로젝트 목적 / 필요성

```🕒🚲 필요한 시간에, 필요한 곳에```

서울시 따릉이 운영의 비효율 문제를 해결하기 위해서는 **데이터 기반 수요 예측 모델링**과 이를 바탕으로 한 **운영 전략 수립**이 필요합니다.

1. 다양한 요인(기상, 고도, 인구, 교통 등)을 반영한 정교한 **수요 예측 모델** 구축  
2. 이를 바탕으로 다음 기능 구현:
- **시간대별·대여소별 수요 예측** → 선제적 자전거 재배치  
- **장소 기반 수요 예측** → 신규 대여소 설치 위치 추천

 > 🎯 **궁극적인 목표** : "어디에, 언제 자전거가 필요할지"를 예측하여 공공자전거 운영을 **더 효율적으로 만드는 것** 

---

## 4. 요구사항 정의

분석된 **User Requirement (UR)** 를 바탕으로, 시스템이 구현해야 할 **System Requirement (SR)** 를 정의하였습니다.
각 SR은 본 프로젝트의 핵심 기능으로 구현되며, 이후 기능 설명 및 모델 설계의 기반이 됩니다.

| User Requirement (UR) | 설명 |
|----------------------|------|
| UR_01 | 특정 대여소의 시간대별 대여량을 예측받을 수 있어야 한다. |
| UR_02 | 신규 대여소 설치에 적합한 위치를 추천받을 수 있어야 한다. |

| System Requirement (SR) | 설명 |
|----------------------|------|
| SR_01 | **시간 및 환경 정보**를 기반으로 특정 대여소의 **시간대별 대여량**을 예측하는 기능 |
| SR_02 | **공간 및 위치 정보**를 바탕으로 설치가 필요한 위치를 추천하는 기능 |

---

## 5. 데이터베이스 구성 및 출처

서울시 공공자전거 수요에 영향을 미치는 시공간적 요인을 정량적으로 분석하기 위해, 다양한 출처의 데이터를 수집하고 통합하였습니다.
해당 데이터는 **EDA, feature 도출, 가설 검증, 모델 input 구성** 전반에 직접 활용됩니다.

### 5-1. 데이터 출처

데이터 수집은 아래와 같은 주요 공공·외부 리소스를 기반으로 진행되었습니다:

- **서울시 열린데이터광장**: 따릉이 대여 이력, 생활인구, 상권 정보, 소득 수준, 등고선 데이터  
- **기상청 데이터 포털 및 API**: 기온, 강수량, 풍속 등 날씨 정보  
- **공공데이터포털**: 지하철·버스 등 대중교통 이용량  
- **Google API**: 대여소별 고도 정보  

### 5-2. 데이터베이스 구조

![ERD](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/4-1.png?raw=true)

데이터베이스는 기능별 분석 목적에 맞춰 **모듈형 테이블 구조**로 설계되었으며,  
예측 모델 학습 및 EDA 분석에 필요한 시점에는 테이블 간 조인 및 전처리를 통해 통합하여 활용합니다.

데이터는 다음과 같이 네 가지 주요 영역으로 분류됩니다:

- **위치 정보**: 자치구, 행정동, 대여소 위치 좌표 등  
- **수요 데이터**: 따릉이 대여량 (월별, 일별, 시간별)  
- **시간 기반 feature**: 날짜, 요일, 시간대, 공휴일 여부, 기온·강수량 등 날씨 정보  
- **공간 기반 feature**: 생활인구, 대중교통 접근성, 산업체 수, 고도, 상권 정보 등

### 5-3. 데이터 통합 및 전처리

수집된 모든 데이터는 **AWS RDS MySQL 서버**에 저장되며, 그 중에서도 **`rental` 테이블**은 2024년 한 해 동안의 전체 이용기록 **44,543,263건**을 담고 있는 **핵심 원천 데이터**입니다. 
기상, 인구, 교통, 상권 등 외부 데이터 역시 서버 내 **별도 테이블**로 저장되어 있으며, 각 데이터는 분석 목적에 따라 **SQL 쿼리로 개별 추출**됩니다.

EDA 분석과 모델 학습에 필요한 데이터는 **각 테이블을 SQL로 호출한 뒤 Pandas 기반 DataFrame으로 변환**하고, 분석 단계에서 **병합 · 전처리 · feature 생성** 작업을 수행합니다.

한편, 학습용 데이터셋은 **MySQL 서버 내부에서 SQL로 별도로 구축한 학습용 테이블**을 활용하며, 이 테이블은 **[대여 시각, 대여소 ID]를 Primary Key**로 하고, 주요 feature가 전처리된 상태로 포함되어 있어 모델 학습 단계에서는 **단순 쿼리 호출만으로 활용**이 가능합니다.

> 📌 `rental` 테이블은 EDA 분석과 학습용 데이터셋 구성의 **출발점**이며, 전체 분석에서 **수요 패턴 이해와 예측 모델 설계의 기반이 되는 중심 테이블**입니다.



---

## 6. EDA (탐색적 데이터 분석)

### 6.1 EDA 분석 및 Feature 선택

앞서 정리한 통합 데이터셋(2024년 한 해 동안의 **이용 기록 44,543,263건**)을 바탕으로, 본 프로젝트에서는 **공공자전거 수요에 영향을 주는 요인**을 식별하고자 탐색적 데이터 분석(EDA)을 수행하였습니다.  
이 과정은 예측 모델링의 기반이 되는 **feature selection**의 출발점이자, 실제 수요 변화에 영향을 미치는 주요 요인을 확인하기 위한 **가설 검증 단계**이기도 합니다.

분석은 크게 다음 두 축의 가설로 나누어 진행되었습니다:

#### 주요 가설:
> “공공자전거의 이용량은 다음과 같은 요인들에 의해 결정될 것이다.”

1. **시간 및 환경 feature**: 시간대, 기온, 강수량, 습도 등  
2. **공간 및 위치 feature**: 고도, 교통 접근성, 주변 인구, 상업시설 수 등


| 시간 및 환경 특성       | 공간 및 위치 특성               |
|------------------------|-------------------------------|
| 시간                   | 대중교통 근접성                |
| 공휴일                 | 대중교통 승하차량              |
| 요일                   | 생활인구                      |
| 기온                   | 산업 및 고용 환경             |
| 강수량                 | 소득                          |
| 습도                   | 상권(주변 점포 수)            |
| 풍속                   | 자전거 인프라(자전거 도로)    |
| 일사량                 | 여가 인프라(공원)             |

가설에 대한 분석을 통해 수요 예측에 유의미한 **features**를 도출할 수 있었습니다. 예를 들어, **기온**과 **강수량**은 수요 변화에 큰 영향을 미쳤으며, **고도**와 **교통 접근성** 또한 중요한 features로 확인되었습니다.

이 과정에서 수행된 EDA는 feature selection의 핵심 기준이 되었으며, 도출된 features는 예측 모델의 입력 변수로 활용되었습니다.

### 6.2 XGBoost 모델링 및 자동 feature 선택

`XGBoost` 모델은 **feature 중요도(Feature Importance)** 를 자동으로 평가하여, 학습 과정에서 중요도가 낮은 feature를 제거하고 핵심 feature에 집중할 수 있도록 설계되어 있습니다. EDA 단계에서 도출된 feature를 기반으로 학습이 이루어지며, 이는 예측 성능의 최적화에 기여합니다.

#### XGBoost의 주요 특징:
- **Feature Importance**: 각 feature의 중요도를 수치화하여, 불필요한 feature는 자동으로 제외하고 핵심 feature만을 학습합니다. 이를 통해 예측 성능을 극대화할 수 있습니다.
- **모델 해석 가능성**: 어떤 feature가 예측 결과에 영향을 미쳤는지를 확인할 수 있어, 결과 해석과 의사결정에 유용합니다.

EDA와 XGBoost는 **상호 보완적인 관계**에 있습니다. EDA를 통해 도출한 중요한 feature를 기반으로 XGBoost가 학습되며, 이는 예측 정확도 향상에 직접적으로 연결됩니다.

#### SR_01 기능에 대한 반영:
- **시간대**, **날씨** 등의 feature는 SR_01에서 핵심 입력으로 사용되며, 시간대별 수요 예측의 정밀도를 높이는 데 기여합니다. 예를 들어, 특정 대여소의 시간대별 수요 예측에는 **기온, 강수량, 요일, 풍속** 등의 feature가 함께 사용되어, **기상 조건 변화에 따른 수요 급감/급증 패턴**을 정밀하게 반영할 수 있습니다.

#### SR_02 기능에 대한 반영:
- **고도, 교통 접근성, 생활 인구** 등의 공간 기반 feature는 SR_02의 설치 위치 예측 모델에 반영되어, 지역별 상대적 수요 예측을 가능하게 합니다. 예를 들어, **고도가 낮고 대중교통 접근성이 높은 지역**은 예측 수요가 높게 나타나는 경향이 있으며, 이는 실제 설치 전략 수립에 활용될 수 있습니다.

---

### 6.3 EDA 분석 결과와 모델링의 연결

### ⏱️ 가설 그룹 A. 시간 및 환경 특성

---

### 🧪 가설 A-1. "자전거 이용량은 시간대의 영향을 많이 받을 것이다"

#### 📌 분석 내용
- 시간대, 요일, 월별 수요 집계
- 출퇴근 시간, 금요일, 봄/가을에 수요 집중

#### 📊 시각화  
![시간대](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/5-2.png?raw=true)
![주중vs주말](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-3.png?raw=true)  
![평일vs휴일](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-4.png?raw=true)  
![요일별](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-5.png?raw=true)  
![계절별](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-6.png?raw=true)

#### ✅ 결론
- 출근(7-9시), 퇴근(17-19시) 시간대에 수요 급등  
- 평일 > 주말, 금요일 집중  
- 봄/가을 > 여름/겨울  
→ **SR_01 기능의 주요 feature로 채택**

---

### 🧪 가설 A-2. "날씨 조건은 자전거 사용량에 크게 영향을 줄 것이다"

#### 📌 분석 내용
- 기온, 강수량, 습도, 일사량별 수요 변화 분석
- 날씨 API 연동 가능성 검토

#### 📊 시각화  
![기온](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-7.png?raw=true)  
![강수량](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-8.png?raw=true)  
![습도](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-9.png?raw=true)  
![일사량](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-10.png?raw=true)

#### ✅ 결론
- 기온 22도 전후에서 최적 수요  
- 강수량 발생 시 수요 급감  
- 일사량↑ → 수요↑ / 습도 80%↑ → 수요↓  
→ **SR_01 기능의 주요 feature로 채택**

---

### 📍 가설 그룹 B. 공간 및 위치 특성

---

### 🧪 가설 B-1. "고도가 높을수록 자전거 수요는 낮아진다"

#### 📌 분석 내용
- 대여소별 고도와 평균 대여량 비교

#### 📊 시각화  
![고도1](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-11.png?raw=true)  
![고도2](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-12.png?raw=true)  
![고도3](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-13.png?raw=true)

#### ✅ 결론
- 고도↑ → 수요↓  
→ **SR_02 feature로 채택**

---

### 🧪 가설 B-2. "지하철역/버스정류장과 가까울수록 수요가 높다"

#### 📌 분석 내용
- 대여소 ↔ 최근접 대중교통 거리 측정 및 그룹 분석

#### 📊 시각화  
![교통 거리](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-15.png?raw=true)

#### ✅ 결론
- 거리↑ → 수요↓  
→ **SR_02 feature로 채택**

---

### 🧪 가설 B-3. "가까운 대중교통의 이용량이 높을수록 수요가 높다"

#### 📌 분석 내용
- 대여소별 최근접 지하철/버스의 승하차량과 수요 비교

#### 📊 시각화  
![교통 이용량](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-24.png?raw=true)

#### ✅ 결론
- 가까운 대중교통 이용량↑ → 수요↑  
→ **SR_02 feature로 채택**

---

### 🧪 가설 B-4. "생활인구가 많을수록 자전거 수요도 많다"

#### 📌 분석 내용
- 자치구별 생활인구와 대여소 수요 매핑

#### 📊 시각화  
![생활인구](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-17.png?raw=true)

#### ✅ 결론
- 생활인구↑ → 수요↑  
→ **SR_02 feature로 채택**

---

### 🧪 가설 B-5. "공원이 가까울수록 수요가 많다"

#### 📌 분석 내용
- 자치구별 공원 수와 대여량 비교

#### 📊 시각화  
![공원수](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-22.png?raw=true)

#### ✅ 결론
- 공원 수↑ → 수요↑  
→ **SR_02 feature로 채택**

---

### 🧪 가설 B-6. "산업 및 고용 환경은 수요를 변화시킨다"

#### 📌 분석 내용
- 사업체 수, 종사자 수 vs 대여량 (자치구/행정동 단위 분석)

#### 📊 시각화  
![산업1](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-18.png?raw=true)  
![산업2](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-19.png?raw=true)  
![산업3](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-20.png?raw=true)  
![산업4](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-21.png?raw=true)

#### ✅ 결론
- 산업체 밀집 지역일수록 수요↑  
→ **SR_02 feature로 채택**

---

### 🧪 가설 B-7. "자전거도로가 많을수록 수요가 많다"

#### 📌 분석 내용
- 자치구별 자전거도로 노선 수와 대여량 비교

#### 📊 시각화  
![자전거도로](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-23.png?raw=true)

#### ✅ 결론
- 자전거도로↑ → 수요↑  
→ **SR_02 feature로 채택**

---

## 7. 기능 설명

### 🚴‍♀️ SR_01. 대여소별 시간대별 수요 예측

- XGBoost 기반 회귀 모델 사용
- 입력: 대여소 ID, 날짜, 시간, 기온, 풍속 등  
  → ※ 기상청 API를 통해 **오늘 / 내일 / 모레**의 예보 데이터를 자동 수집하여 예측에 반영
- 출력: 예상 대여량 숫자 (GUI로 실시간 확인 가능)
- 학습 데이터셋 규모: **8022개 샘플**

![SR_01_출력화면](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-1.png?raw=true)

### 🗺 SR_02. 신규 대여소 설치 위치 추천

- 지정된 좌표 범위 내 격자 후보지 생성  
- 위치 특성 기반 수요 예측 모델 적용  
- 예측값 상위 후보지를 지도에 마커로 시각화  
- 입력 예시:  
  `[Input] right_bottom = (37.5600, 126.9700), left_top = (37.5700, 126.9800), limit = 200, n = 3`  
- 학습 모델: 3-Stage XGBoost 회귀 (저수요 / 중간 / 고수요 구간별 분리 학습)

![SR_02_출력화면](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/6-2.png?raw=true)

---

## 8. 모델 설명 및 성능 평가

본 프로젝트는 **시간 기반 수요 예측 기능(SR_01)** 과 **공간 기반 설치 위치 추천 기능(SR_02)** 을 중심으로 구성되며,  
각 기능의 구현을 위해 `XGBoost` 기반 예측 모델을 설계하고 학습하였습니다.  
예측 성능 평가는 `RMSE`, `MAE`, `(S)MAPE`, `R²` 등의 지표를 기준으로 수행하였으며, 다음과 같은 결과를 얻었습니다.

---

### 📍 SR_01: 시간대별 수요 예측 기능

해당 기능은 **대여소별, 시간대별 수요를 사전에 예측**함으로써 자전거의 선제적 재배치를 가능하게 합니다.  
이를 구현하기 위해 XGBoost 회귀 모델을 활용하였으며, 다양한 시간 및 환경 feature를 입력 변수로 사용하였습니다.

- **사용한 예측 모델**: XGBoost 회귀  
- **입력 변수**: 날짜, 시간, 기온, 풍속, 강수량, 습도, 고도, 요일 등  
- **예측 대상**: 시간대별 대여량

![모델](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/7-1.png?raw=true)

| 지표 | 값 |
|------|----|
| RMSE | 9.60 |
| MAE  | 6.66 |
| MAPE | 23.24% |
| R²   | 0.835 |

- 전체 구간 기준 R² = 0.835, 특히 실수요 구간(실제 대여량 > 10)에서는 R² = 0.860까지 도달  
- 주요 시간 및 날씨 feature가 수요 변동을 충분히 설명함을 입증  
- **해당 모델은 SR_01 기능을 실현하기에 충분한 수준의 예측 성능을 확보**하였으며, 실시간 운영 판단에 활용 가능

---

### 🗺 SR_02: 설치 위치 추천 기능

해당 기능은 **신규 대여소 설치 후보지 중 수요가 높을 것으로 예상되는 위치를 추천**하는 기능입니다.  
공간 특성 기반의 예측 모델을 활용하여, 각 후보 위치의 상대적 수요 수준을 추정합니다.

- **사용한 예측 모델**: 3-Stage XGBoost 회귀 (수요 구간별 분리 학습)  
- **입력 변수**: 위도, 경도, 고도, 주변 인구, 유동 인구, 교통 접근성, 상업시설 수 등  
- **예측 대상**: 일 평균 대여 수요 예측값

![모델](https://github.com/addinedu-ros-9th/eda-repo-1/blob/main/img/7-2.png?raw=true)

| 지표 | 값 |
|------|----|
| RMSE  | 20.49 |
| MAE   | 12.60 |
| MAPE  | 41.59% |
| SMAPE | 33.96% |
| R²    | 0.761 |

- 3-Stage 구조로 수요 구간(저·중·고)을 분리하여 학습하였으나, 고수요 구간에서는 예측 정확도가 낮은 편  
- 특히 특수 입지 조건을 가진 지역은 일반 feature들만으로 설명되기 어려움  
- 절대 수요 예측에는 한계가 있으며, 후보지 간 상대적 수요 경향을 비교하는 보조 지표로서 제한적으로 활용 가능
- 입지 전략 수립을 위한 1차적 필터링 지표 또는 참고 자료 수준의 기능을 수행하기에 적합함
>[!Note]
> 그럼에도 불구하고 R² = 0.761이라는 수치는 복잡한 외부 요인을 배제하고도 공간 기반 feature만으로 일정 수준의 수요 분포를 설명할 수 있음을 보여줍니다. 이 결과는 본 모델이 설치 위치 추천 기능의 기반으로서 활용 가능성을 지니고 있으며, 이후 고수요 지역 특성을 보완하거나 민간 데이터를 추가하는 방식으로 정밀도 향상을 기대할 수 있습니다.
>
> 👉 이어지는 [9. 한계점](#9-한계점) 에서는 이러한 예측 한계의 원인을 보다 구체적으로 분석하겠습니다.

---

## 9. 한계점

프로젝트 수행 과정에서 다음과 같은 구조적 한계가 확인되었으며, 이는 모델 성능 및 활용 가능성에 영향을 미쳤습니다.

---

### 9-1. 고수요 대여소 예측의 구조적 한계

#### 고수요 대여소의 비선형적·복합적 특성

- 고수요 대여소는 **여러 feature가 결합되었을 때 특정 임계치를 초과하며 수요가 급증하는 특성**을 보이는 경우가 많음  
- 본 프로젝트에서는 XGBoost와 같이 비선형 모델을 사용하였음에도, **이러한 급격한 변화 패턴은 예측에 한계가 존재**  
- 이는 feature 간 상호작용이 매우 복잡하거나, 데이터 외적 요인(랜드마크, 이벤트 등)이 작용하기 때문일 수 있음

> 📌 **시사점**:  
> 고수요 대여소의 수요를 정밀하게 예측하기 위해서는 **기존 feature 외에도 장소 특수성을 반영할 수 있는 외부 요인(POI, 이벤트, 인지도 등)** 을 추가하거나, **복합적인 패턴을 더 효과적으로 학습할 수 있는 고차원 모델 구조**가 필요할 수 있음


---

### 9-2. 공공데이터 수집·활용의 한계

#### 데이터 해상도 제약

- 공공 API는 시간·공간 해상도가 낮은 경우가 많음  
- 이로 인해 **세밀한 위치 기반 패턴 분석 및 시간대별 변화 감지에 제약** 발생  
- 의도했던 ‘행정동 단위’ 수준의 분석이 어려워 **자치구 단위로 분석 수준을 낮춰야 했던 사례 존재**

#### 전처리 과정의 수작업 증가

- 다양한 데이터 간 **좌표계 불일치**, **행정동 코드 매핑 오류** 등으로 인해  
  데이터 병합 및 정제가 자동화되지 않고 **수작업 보정이 많이 요구됨**

#### 민간 데이터 대비 정보의 제약

- 유동 인구, 상권, 통행량 등 공공데이터는 민간에 비해 해상도와 최신성이 떨어지는 경우 많음  
- 이는 예측 정밀도를 떨어뜨리는 요소로 작용  
- 민간 API(카카오, Tmap, SKT 유동인구 등)와의 연계를 통한 보완이 필요

> 📌 **시사점**:  
> 본 프로젝트의 예측 성능 및 분석 정밀도는 **공공데이터 품질과 해상도에 직접적으로 영향을 받습니다.** 향후에는 **민간 데이터 연계 및 공공데이터 고도화**를 통해 정밀도를 향상시킬 필요가 있습니다.


---

## 10. 디렉토리 구조

본 프로젝트는 기능 단위로 다음과 같은 3개 상위 디렉토리로 구성되어 있으며,  
각 디렉토리는 데이터 수집, 분석, 서비스 구현이라는 주요 흐름에 따라 역할이 분리되어 있습니다.

```
📦 Project Root
├── data_collection     # 공공데이터 수집 및 전처리 스크립트
├── data_analysis       # 데이터 탐색, feature 분석, EDA 시각화
├── service             # 예측 모델 학습 및 사용자 기능 구현 (SR_01 / SR_02)
```

### 📁 data_collection

> 공공데이터 및 외부 API를 활용한 데이터 수집과 전처리 코드가 포함된 폴더입니다.

### 📁 data_analysis

> 수요 패턴 분석, 시각화, feature selection 등 탐색적 분석(EDA)을 위한 코드가 포함되어 있습니다.  
> 실제 예측 모델 학습은 `service` 폴더에서 별도로 수행됩니다.

### 📁 service

> 예측 모델 학습, 추론, 사용자 기능(SR_01, SR_02) 구현을 포함하는 핵심 실행 디렉토리입니다.


```📌 전체 프로젝트는 데이터 수집 → 탐색적 분석 → 기능 구현 및 학습의 흐름으로 구성되어 있으며, 기능별 유지보수와 역할 분리가 용이하도록 설계되어 있습니다.```
