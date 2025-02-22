# 📦 서울옥션 옥션 데이터 수집 및 ETL 시스템 구축

## 📝 프로젝트 개요

- 이 프로젝트는 서울옥션의 옥션 데이터를 수집하고 처리하여 **MongoDB**, **MariaDB**, **GCP**에 저장하는 **ETL 시스템**을 구축하는 것입니다. <br>
- 주요 기술 스택은 **Python**, **MongoDB**, **MariaDB**, **GCP**, **Cron**, **Airflow**입니다.

### 기간
2025.01.16 ~ (진행 중)

### 주요 목표
- **서울옥션 옥션 데이터 수집**  
- **MongoDB**에 메타 데이터와 원시 데이터 저장  
- **MariaDB**에 클렌징된 데이터 저장  
- **GCP**에 이미지 데이터 저장  
- **Cron**과 **Airflow**로 ETL 자동화

## 🛠️ 기술 스택
- **Python**: 데이터 크롤링 및 클렌징 알고리즘 구현
- **MongoDB**: 원시 데이터 및 메타 데이터 저장
- **MariaDB**: 클렌징된 데이터 저장
- **GCP**: 이미지 데이터 저장
- **Cron**: 스케줄링 및 자동화
- **Airflow**: ETL 파이프라인 자동화 및 관리

## 🗂️ 데이터 흐름 다이어그램
> **(여기에 데이터 프로세싱 다이어그램 추가예정)**

## 📅 프로젝트 일지

**일지 항목**은 Notion에서 관리됩니다. 


[➡️ 프로젝트 일지 확인하러 가기](https://slime-walnut-8b4.notion.site/17dc620b13a5801d8eafde9d65012abc?pvs=4)

<p aligne="center">
<img src="./readme_imgs/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EC%9D%BC%EC%A7%80.png" width="60%" height="50%">
</p>

프로젝트 진행 중 기록되는 주요 내용은 다음과 같습니다: 

1. **프로젝트 계획**  
   - 데이터 흐름 설계 및 시스템 구성
2. **데이터 수집**  
   - 서울옥션 API 분석 및 크롤러 설계
3. **데이터 클렌징 및 처리**  
   - 클렌징 알고리즘 개발 및 적용
4. **이미지 처리**  
   - GCP에 이미지 데이터 저장 방식 정의
5. **자동화**  
   - Cron과 Airflow를 이용한 ETL 자동화 구축
6. **테스트 및 디버깅**  
   - 데이터 연동 테스트 및 오류 해결
7. **배포 및 운영**  
   - 시스템 배포 및 모니터링

## 🚧 진행 중인 작업

- 서울옥션 API 분석 및 크롤러 설계
- MongoDB, MariaDB, GCP 데이터 저장 방식 최종 설계
- Cron과 Airflow를 통한 데이터 자동화 계획 수립

## 📂 설치 및 실행

### 요구 사항
- Python 3.11 이상
- MongoDB, MariaDB
- Google Cloud SDK
- Cron / Airflow

### 설치 방법
1. **MongoDB 및 MariaDB 설치**  
2. **GCP 설정** (Cloud Storage 버킷 생성)
3. **Cron / Airflow 설정**
4. **Python 패키지 설치**  
