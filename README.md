# 오늘의 몸 신호, AI 컬러푸드 가이드

> 사용자의 몸 상태와 생활 신호를 바탕으로 컬러푸드·전체식·통곡물 등 건강한 식생활을 위한 참고 정보를 제공하는 AI 웹 서비스



## 실행 화면 미리보기

웹페이지를 직접 실행하지 않는 경우에도 서비스의 전체 구조와 주요 기능,

사용자 입력 과정, AI 실행 과정 및 결과를 확인할 수 있도록 주요 실행 화면을 정리하였다.

01\~10번은 서비스의 주요 Page / Section 구현 화면이며,

11\~13번은 사용자 입력부터 AI Food Guide 실행, Loading, 결과 출력까지의 실제 동작 과정을 보여준다.



### 01. Main Page 정상 실행

![Main Page 정상 실행](./images/01.%20MainPage정상실행.png)

**메인 페이지 정상 실행 화면**

서비스명과 핵심 소개 문구, `AI Food Guide 시작` 버튼과 `컬러푸드 살펴보기` 버튼이 표시된 Home 화면이다.



### 02. Body Signal Page 실행

![Body Signal Page 실행](./images/02.%20BodySignalPage실행.png)

**Body Signal 사용자 입력 화면**

생활 속 이상 신호 등 몸 상태, 평소 과일·채소 섭취 정도, 식생활 습관,

알레르기 관련 정보, 피하고 싶은 음식 등의 사용자 입력 항목을 보여주는 화면이다.



### 03. AI Food Guide Page 실행

![AI Food Guide Page 실행](./images/03.%20AIFoodGuidePage실행.png)

**AI Food Guide 기능 안내 화면**

사용자 입력을 바탕으로 미리 정리된 컬러푸드·Whole Food·Whole Grain 정보를 참고하여

AI 식생활 안내서를 생성하는 기능을 소개하는 화면이다.



### 04. Color Guide Page 실행

![Color Guide Page 실행](./images/04.%20ColorGuidePage실행.png)

**Color Guide 컬러푸드 정보 화면**

Yellow·Purple·Red·Green 컬러별 대표 식품과 컬러푸드 정보를 한눈에 확인할 수 있는 화면이다.



### 05. Whole Food Page 실행

![Whole Food Page 실행](./images/05.%20WholeFoodPage실행.png)

**Whole Food 정보 화면**

과일과 채소의 먹을 수 있는 부분을 가능한 범위에서 활용하는 Whole Food 개념과

섭취 시 참고할 주의사항을 소개하는 화면이다.



### 06. Whole Grain Page 실행

![Whole Grain Page 실행](./images/06.%20WholeGrainPage실행.png)

**Whole Grain 정보 화면**

현미·통밀·통메밀 등 대표적인 통곡물의 종류와 특징,

주요 영양정보를 소개하는 화면이다.



### 07. Nutrition Page 실행

![Nutrition Page 실행](./images/07.%20NutritionPage실행.png)

**Nutrition 주요 영양정보 화면**

비타민 C·비타민 E·엽산·칼륨·식이섬유 등

서비스에서 다루는 주요 영양성분을 안내하는 화면이다.



### 08. My Foods Page 실행

![My Foods Page 실행](./images/08.%20MyFoodsPage실행.png)

**My Foods 추천 식품 저장 화면**

AI 추천 결과에서 사용자가 저장한 추천 식품을 다시 확인할 수 있는

My Foods 기능 화면이다.



### 09. About Page 실행

![About Page 실행](./images/09.%20AboutPage실행.png)

**About 서비스 소개 화면**

`오늘의 몸 신호, AI 컬러푸드 가이드`의 제작 목적과

서비스에서 AI가 수행하는 역할을 설명하는 화면이다.



### 10. FAQ Page 실행

![FAQ Page 실행](./images/10.%20FAQPage실행.png)

**FAQ 자주 묻는 질문 화면**

질병 진단 여부, 영양정보 구성 방식, 여러 색깔의 식품을 소개하는 이유,

건강 관련 의사결정 시 주의사항 등을 안내하는 화면이다.



### 11. AI Food Guide 실행 전 입력

![AI Food Guide 실행 전 입력](./images/11.%20AIFoodGuide실행전입력.png)

**AI Food Guide 실행 전 사용자 입력 화면**

Body Signal, 과일·채소 섭취 정도, 식생활 습관, 알레르기 관련 정보,

피하고 싶은 음식 등의 입력값을 설정한 뒤

`AI Food Guide 실행`을 준비한 화면이다.



### 12. AI Food Guide Loading

![AI Food Guide Loading](./images/12.%20AIFoodGuideLoading.png)

**AI Food Guide 실행 중 Loading 화면**

사용자가 `AI Food Guide 실행` 버튼을 누른 뒤 AI 응답을 기다리는 동안

`식생활 안내서를 만들고 있습니다.`라는 Loading 안내가 표시되는 화면이다.

AI 응답을 기다리는 동안 Loading 상태를 명확하게 표시하여

사용자가 현재 요청이 처리 중이라는 사실을 확인할 수 있도록 구현하였다.



### 13. AI Result 정상 실행

![AI Result 정상 실행](./images/13.%20AIResult정상실행.png)

**AI 식생활 안내서 결과 정상 실행 화면**

사용자 입력을 바탕으로 AI 추천 결과가 정상적으로 생성되어

추천 컬러푸드, 대표 식품, 추천 이유, 주요 영양정보,

함께 살펴볼 식품, Whole Food·Whole Grain 참고 정보,

섭취 시 참고사항 및 건강정보 이용 시 주의사항이 출력된 화면이다.

이 화면을 통해 다음과 같은 실제 AI 기능 흐름이 정상적으로 동작하는 것을 확인하였다.

`사용자 입력 → Frontend 검증 → Backend 요청 → OpenAI API 호출 → AI 응답 검증 → 결과 화면 출력`



#### 14. Mobile Main Page 실행

![Mobile Main Page 실행](./images/14.%20MobileMainPage실행.png)

**Mobile Main Page 반응형 실행 화면**

390 × 844 모바일 환경에서 Home Page의 Navigation이 Hamburger Menu 형태로 전환되고,

서비스 제목·소개 문구·버튼이 화면 폭에 맞게 정상적으로 배치된 것을 확인하였다.



#### 15. Mobile Body Signal 실행

![Mobile Body Signal 실행](./images/15.%20MobileBodySignal실행.png)

**Mobile Body Signal 입력 화면**

모바일 환경에서 Body Signal 선택 항목과 사용자 입력 Form이 한 열 구조로 배치되고,

각 입력 영역이 화면 폭 안에서 정상적으로 표시되는 것을 확인하였다.



#### 16. Mobile Body Signal 상세 입력

![Mobile Body Signal 상세 입력](./images/16.%20MobileBodySignal입력실행.png)

**Mobile Body Signal 상세 입력 화면**

과일·채소 섭취 정도, 식생활 습관, 알레르기 관련 정보 및 추가 입력 항목이

모바일 화면에서 서로 겹치지 않고 정상적으로 표시되는 것을 확인하였다.



#### 17. Mobile AI Food Guide 실행

![Mobile AI Food Guide 실행](./images/17.%20MobileAIFoodGuide실행.png)

**Mobile AI Food Guide 실행 화면**

모바일 화면에서도 AI Food Guide 기능 영역과 실행 버튼이

화면 폭에 맞게 정상적으로 배치되는 것을 확인하였다.



#### 18. Mobile Color Guide 실행

![Mobile Color Guide 실행](./images/18.%20MobileColorGuide실행.png)

**Mobile Color Guide 화면**

Yellow·Purple·Red·Green 컬러푸드 정보가 모바일 화면 폭에 맞게 배치되고,

각 콘텐츠가 화면 밖으로 벗어나지 않는 것을 확인하였다.



#### 19. Mobile Whole Food 실행

![Mobile Whole Food 실행](./images/19.%20MobileWholeFood실행.png)

**Mobile Whole Food 정보 화면**

Whole Food Section의 제목과 설명이 모바일 화면에서 읽기 쉬운 형태로

정상적으로 표시되는 것을 확인하였다.



#### 20. Mobile Whole Grain 실행

![Mobile Whole Grain 실행](./images/20.%20MobileWholeGrain실행.png)

**Mobile Whole Grain 정보 화면**

Whole Grain Section의 콘텐츠가 모바일 Layout에 맞게 조정되어

텍스트와 정보 영역이 화면 밖으로 벗어나지 않는 것을 확인하였다.



#### 21. Mobile Nutrition 실행

![Mobile Nutrition 실행](./images/21.%20MobileNutrition실행.png)

**Mobile Nutrition 정보 화면**

Nutrition Section의 주요 영양정보가 모바일 화면에서도

정상적인 Layout으로 표시되는 것을 확인하였다.



#### 22. Mobile My Foods 실행

![Mobile My Foods 실행](./images/22.%20MobileMyFoods실행.png)

**Mobile My Foods 화면**

저장한 추천 식품을 확인하는 My Foods Section이

모바일 화면 크기에 맞게 정상적으로 표시되는 것을 확인하였다.



#### 23. Mobile About 실행

![Mobile About 실행](./images/23.%20MobileAbout실행.png)

**Mobile About 서비스 소개 화면**

서비스 목적과 AI 활용 범위를 설명하는 About Section이

모바일 화면에서 읽기 쉬운 형태로 표시되는 것을 확인하였다.



#### 24. Mobile FAQ 실행

![Mobile FAQ 실행](./images/24.%20MobileFAQ실행.png)

**Mobile FAQ 화면**

FAQ의 질문 항목이 모바일 화면 폭에 맞게 표시되고,

화면 밖으로 벗어나거나 서로 겹치지 않는 것을 확인하였다.



---

## 1. 서비스 소개

### 1.1 서비스 개요

- 서비스명: 오늘의 몸 신호, AI 컬러푸드 가이드

- 한 줄 소개: 사용자의 몸 상태와 생활 신호를 바탕으로 컬러푸드·전체식·통곡물 등 건강한 식생활 참고 정보를 제공하는 AI 웹 서비스

- 서비스 분야: AI 기반 건강 식생활 정보·컬러푸드 추천 웹 서비스

- 제작 목적: 사용자가 자신의 몸 상태와 생활 습관을 간단히 입력하면 AI가 이를 바탕으로 컬러푸드·전체식·통곡물 등 다양한 식생활 정보를 알기 쉽게 안내하여, 일상에서 여러 식품을 균형 있게 살펴보고 건강한 식생활에 관심을 가질 수 있도록 돕는 것을 목적으로 한다.





### 1.2 제작 배경

평소 피로감, 불규칙한 식사, 과일·채소 섭취 부족 등 몸과 생활에서 여러 신호를 느끼더라도 어떤 식품과 식생활 정보를 참고하면 좋을지 쉽게 판단하기 어렵다.

건강 관련 정보는 양이 많고 내용도 복잡한 데다, 인터넷에는 부정확하거나 출처가 불분명한 정보도 있어 자신에게 필요한 식생활 정보를 찾아 이해하기 어려운 경우가 있다.

이에 KBS 「생로병사의 비밀」에서 다룬 컬러과일 건강법과 전체식 관련 내용을 참고하여, Yellow·Purple·Red·Green의 컬러푸드와 Whole Food·Whole Grain 정보를 하나의 웹 서비스에서 쉽게 살펴볼 수 있도록 기획하였다.

여기에 AI를 활용하여 사용자가 선택한 몸 상태와 생활 신호를 바탕으로 관련 식생활 정보를 이해하기 쉽게 안내하는 서비스를 만들고자 하였다.



### 1.3 서비스 목표

사용자가 현재 느끼는 몸 상태와 생활 신호를 어렵지 않게 선택하고, AI를 통해 자신이 참고할 수 있는 건강한 식생활 정보를 간편하게 확인할 수 있도록 하는 것을 목표로 한다.

단순히 한 가지 음식만 추천하는 것이 아니라 Yellow, Purple, Red, Green의 다양한 컬러푸드와 주요 영양성분을 함께 소개하여 여러 종류의 식품을 균형 있게 살펴볼 수 있도록 한다.

또한 컬러푸드에서 나아가 먹을 수 있는 과일·채소의 껍질 등을 활용하는 Whole Food와 현미·통밀·통메밀 등의 Whole Grain 정보도 제공하여 사용자가 일상적인 식생활을 폭넓게 이해할 수 있도록 한다.

AI는 사용자의 입력에 맞는 식생활 정보를 이해하기 쉽게 설명하고 추천하는 역할을 담당하며, 질병을 진단하거나 특정 음식이 질병을 치료한다고 판단하지 않는 식생활 참고 서비스로 구성한다.



### 1.4 타깃 사용자

- 주요 사용자: 평소 건강한 식생활과 다양한 식품 섭취에 관심이 있지만 어떤 식품과 식생활 정보를 참고해야 할지 고민하는 사람

- 사용 상황: 피로감, 불규칙한 식사, 과일·채소 섭취 부족, 배변 불편, 소화 부담 등 자신의 몸 상태나 생활 습관을 돌아보고 식생활 정보를 참고하고 싶을 때

- 사용자가 원하는 것: 자신의 몸 상태와 생활 신호에 맞춰 컬러푸드·전체식·통곡물 등의 식생활 정보와 추천 이유, 주요 영양정보, 섭취 시 참고사항 등을 쉽고 빠르게 확인하는 것



## 2. 서비스 핵심 원칙

### 2.1 건강정보 제공 원칙

이 서비스는 사용자의 입력을 바탕으로 질병이나 건강 상태를 진단하는 것이 아니라, 일상적인 몸 상태와 생활 신호를 돌아보고 건강한 식생활에 참고할 수 있는 정보를 제공하는 것을 원칙으로 한다.

사용자가 입력한 피로감, 식사 습관, 과일·채소 섭취 정도 등의 정보는 의료적 판단을 위한 자료가 아니라 식생활 정보를 안내하기 위한 참고 정보로만 활용한다.



### 2.2 음식 추천 원칙

특정 증상과 특정 음식을 1:1로 연결하여 해당 음식이 증상을 치료하거나 개선한다고 단정하지 않는다.

사용자의 몸 상태와 생활 신호를 참고하여 컬러푸드·전체식·통곡물 등 다양한 식품 정보를 안내하고, 한 가지 음식이나 한 가지 색깔에만 집중하기보다 여러 종류의 식품을 균형 있게 살펴볼 수 있도록 구성한다.

또한 사용자가 입력한 알레르기 관련 정보나 피하고 싶은 음식이 있을 경우 추천 과정에서 이를 고려하도록 설계한다.



### 2.3 AI 사용 범위

AI는 사용자가 입력한 몸 상태와 생활 신호, 평소 식생활, 피하고 싶은 음식 등의 정보를 바탕으로 적절한 식생활 정보를 선택하고 그 이유를 이해하기 쉬운 문장으로 설명하는 역할을 담당한다.

컬러푸드의 대표 식품과 주요 영양정보 등 사실성이 중요한 기본 정보는 신뢰할 수 있는 자료를 바탕으로 미리 정리한 식생활 정보를 활용하고, AI는 이러한 정보를 사용자의 입력에 맞게 선택·정리·설명하는 데 활용한다.

AI는 질병명을 판단하거나 질병을 진단하지 않으며, 특정 음식의 치료 효과를 판단하거나 의료진의 진단과 치료를 대신하지 않는다.



### 2.4 의료·건강정보 주의사항

이 서비스에서 제공하는 AI 추천 결과와 식생활 정보는 건강한 식생활을 위한 참고용 정보이며 의료적 진단이나 치료를 목적으로 하지 않는다.

개인이 앓고 있는 질환 등 건강 상태와 복용 중인 약물, 특정 식품에 대한 알레르기 반응 여부 등에 따라 섭취 시 고려해야 할 사항이 달라질 수 있으므로, 서비스의 결과만을 근거로 건강과 관련된 중요한 결정을 내려서는 안 된다.

증상이 만성적으로 지속되거나 심해지는 경우, 또는 질환과 관련하여 전문적인 판단이 필요한 경우에는 서비스의 추천에 의존하기보다 의사 등 의료전문가의 진료와 안내를 우선하도록 한다.



## 3. 주요 기능

### 3.1 Body Signal 입력

사용자는 현재 자신에게 해당하는 몸 상태와 생활 신호를 선택하거나 필요한 경우 직접 입력할 수 있다.

주요 선택 항목은 다음과 같이 구성한다.

- 피로감을 자주 느낌

- 배변이 불편함

- 식사가 불규칙함

- 과일·채소 섭취가 부족함

- 소화가 부담스러움

- 기타 상태 직접 입력

추가로 평소에 과일과 채소를 얼마나 섭취하는지와 특정 식품에 대한 알레르기 반응 여부, 피하고 싶은 음식 등을 입력할 수 있도록 하여 AI가 사용자의 상황을 참고할 수 있도록 한다.

필수 입력값이 비어 있거나 올바르지 않은 경우에는 Frontend에서 먼저 입력값을 확인하여 AI API에 요청을 보내지 않고, 사용자에게 입력 내용을 확인하도록 안내한다.



### 3.2 AI Food Guide

Body Signal에서 입력한 사용자의 몸 상태와 생활 신호, 평소 식생활 정보, 피하고 싶은 음식 등의 정보를 Python 기반 Backend를 통해 AI API에 전달한다.

AI는 입력 내용을 바탕으로 신뢰할 수 있는 자료를 토대로 미리 정리한 컬러푸드·전체식·통곡물 정보를 활용하여 사용자에게 참고할 만한 식생활 정보를 선택하고, 추천 이유와 주요 영양정보를 이해하기 쉬운 형태로 생성한다.

AI 응답은 정해진 JSON 구조로 받아 필요한 항목이 정상적으로 포함되어 있는지 Backend에서 검증한 뒤 Frontend로 전달한다.

AI 응답을 기다리는 동안에는 Loading 상태를 표시하며, API Error나 네트워크 오류, Timeout 등이 발생하면 사용자가 상황을 이해할 수 있도록 별도의 안내 메시지를 표시한다.



### 3.3 추천 결과

결과 화면에서는 사용자의 입력을 바탕으로 생성된 AI 식생활 안내서를 카드 형태로 알기 쉽게 보여준다.

주요 결과 항목은 다음과 같이 구성한다.

- 오늘의 추천 컬러푸드

- 대표 식품

- 추천 이유

- 주요 영양정보

- 함께 살펴볼 대안 식품

- Whole Food 또는 Whole Grain 관련 참고 정보

- 섭취 시 참고사항

- 건강정보 이용 시 주의사항

예를 들어 Green이 추천된 경우 키위를 대표 식품으로 보여주고, 관련 영양정보와 추천 이유를 함께 설명한다. 다른 색깔의 식품도 함께 제시하여 한 가지 음식에만 집중하지 않도록 안내한다.

결과 화면에는 **“AI가 음식은 추천하지만 질병은 진단하지 않습니다.”**라는 안내를 함께 표시하여 서비스가 의료 진단이나 치료를 목적으로 하지 않는다는 점을 명확하게 전달한다.



### 3.4 컬러푸드 정보

- Yellow: 레몬과 감귤류 등을 대표 식품으로 소개하고, 비타민 C와 플라보노이드 등 주요 영양성분과 식물성 성분에 대한 정보를 제공한다.

- Purple: 블루베리와 포도 등을 대표 식품으로 소개하고, 안토시아닌 등 보라색·청색 계열 식품에서 주로 살펴볼 수 있는 식물성 성분과 관련 정보를 제공한다.

- Red: 체리와 복분자, 토마토, 사과 등의 식품을 소개하고, 식품에 따라 안토시아닌·라이코펜 등 서로 다른 성분이 포함될 수 있다는 점을 함께 안내한다.

- Green: 키위와 아보카도, 멜론 등을 대표 식품으로 소개하고, 비타민 C·비타민 E·엽산·칼륨·식이섬유 등 주요 영양정보를 제공한다.

각 색깔을 특정 기능이나 질병과 1:1로 연결하기보다, 식품의 색깔에 따라 다양한 영양성분과 식물성 성분을 살펴볼 수 있다는 점을 중심으로 안내한다.



### 3.5 Whole Food

Whole Food Section에서는 과일과 채소의 먹을 수 있는 부분을 가능한 범위에서 버리지 않고 활용하는 전체식의 개념을 소개한다.

과일·채소의 껍질이나 겉부분에도 식이섬유를 비롯한 여러 영양성분과 식물성 성분이 포함될 수 있지만, 모든 식품의 껍질을 먹을 수 있는 것은 아니므로 식품의 종류에 따라 섭취 가능한 부분을 구분하여 안내한다.

껍질째 섭취할 수 있는 과일과 채소도 충분한 세척과 위생 관리가 필요하며, 식품의 상태와 개인의 상황을 고려하여 섭취하도록 안내한다.

또한 사용자가 일상생활에서 참고할 수 있도록 껍질째 활용할 수 있는 식품의 예와 세척·조리·활용 방법 등을 이해하기 쉽게 제공한다.



### 3.6 Whole Grain

Whole Grain Section에서는 현미·통밀·통메밀 등 곡물의 겉부분과 배아를 비교적 많이 유지하고 있는 대표적인 통곡물의 종류와 특징을 소개한다.

정제된 곡물과 비교하여 통곡물에서 살펴볼 수 있는 식이섬유, 비타민, 미네랄, 단백질 등의 주요 영양정보를 이해하기 쉽게 제공한다.

또한 통곡물이 모든 사람에게 동일하게 적합하다고 단정하지 않고, 개인의 소화 상태와 식습관 등을 고려하여 자신의 식생활에 적절하게 활용할 수 있도록 참고 정보를 제공한다.

현미·통밀·통메밀 등 대표적인 통곡물별 특징과 일상생활에서 활용할 수 있는 예시도 함께 보여준다.



### 3.7 Nutrition

Nutrition Section에서는 서비스에서 소개하는 컬러푸드·전체식·통곡물에 포함된 주요 영양성분을 사용자가 쉽게 이해할 수 있도록 설명한다.

비타민 C·비타민 E·엽산·칼륨·식이섬유 등의 주요 영양성분과 안토시아닌·플라보노이드·카로티노이드 등의 식물성 성분을 식품별로 정리하여 보여준다.

전문적인 영양 용어를 단순히 나열하기보다 각 성분이 어떤 식품에서 주로 확인되는지와 식생활에서 어떤 의미로 참고할 수 있는지를 쉬운 문장으로 설명한다.

영양성분 정보는 특정 질병의 예방이나 치료 효과를 단정하기 위한 것이 아니라, 사용자가 다양한 식품의 특징과 영양정보를 이해하기 위한 참고 정보로 제공한다.



### 3.8 Color Guide

Color Guide에서는 Yellow·Purple·Red·Green 네 가지 대표적인 컬러푸드와 각 색깔에 해당하는 식품의 주요 영양성분 정보를 한 화면에서 비교할 수 있도록 구성한다.

각 색깔별로 대표 식품, 주요 영양성분, 다양한 식품의 예시 등을 카드 또는 서로 비교하기 쉬운 형태로 보여주어 사용자가 색깔별 특징을 직관적으로 확인할 수 있도록 한다.

특정 색깔의 식품이 다른 색깔보다 더 건강에 좋다고 순위를 매기지 않고, 서로 다른 색깔의 식품을 다양하게 살펴보고 균형 있게 섭취하는 것이 중요하다는 방향으로 안내한다.

사용자는 Color Guide에서 관심 있는 색깔을 선택하여 해당 컬러푸드의 상세 정보를 확인할 수 있는 Section(상세 정보 영역)으로 이동할 수 있다.



## 4. 페이지 / Section 구성

| 번호 | Page / Section | 주요 내용 |

|---|---|---|

| 01 | Home | 서비스 소개, 주요 기능 안내, AI Food Guide 시작 버튼 제공 |

| 02 | Body Signal | 몸 상태와 생활 신호, 평소 식생활 습관, 알레르기 관련 정보 및 피하고 싶은 음식 입력 |

| 03 | AI Food Guide | 사용자 입력을 바탕으로 AI 식생활 안내서 생성 |

| 04 | Result | 추천 컬러푸드, 대표 식품, 추천 이유, 영양정보, 주의사항 표시 |

| 05 | Yellow | 레몬·감귤류 등 Yellow 컬러푸드와 관련 영양정보 소개 |

| 06 | Purple | 블루베리·포도 등 Purple 컬러푸드와 관련 영양정보 소개 |

| 07 | Red | 체리·복분자·토마토·사과 등 Red 컬러푸드와 관련 영양정보 소개 |

| 08 | Green | 키위·아보카도·멜론 등 Green 컬러푸드와 관련 영양정보 소개 |

| 09 | Whole Food | 과일·채소의 섭취 가능한 부분, 세척 방법, 조리·활용 방법 등 전체식 정보 소개 |

| 10 | Whole Grain | 현미·통밀·통메밀 등 대표적인 통곡물의 종류와 특징, 영양정보 소개 |

| 11 | Nutrition | 비타민·미네랄·식이섬유·식물성 성분 등 주요 영양정보 설명 |

| 12 | Color Guide | Yellow·Purple·Red·Green 컬러푸드와 대표 식품의 특징을 한눈에 비교 |

| 13 | My Foods | 사용자가 저장한 추천 식품과 식생활 습관에 참고할 수 있는 정보를 다시 확인 |

| 14 | About | 서비스 제작 목적, 정보 구성 방식, AI 활용 범위 소개 |

| 15 | FAQ | AI의 한계, 건강정보 이용 시 주의사항, 컬러푸드·전체식·통곡물 등 식생활 정보에 대한 설명 |

※ 실제 구현 과정에서 일부 Section을 통합하거나 제외한 경우에는 최종 제출 전에 실제 구현 결과에 맞게 표를 수정한다.



## 5. 사용자 이용 흐름

[사용자]

    ↓

[Home에서 서비스 소개 및 이용 방법 확인]

    ↓

[Body Signal에서 몸 상태와 생활 신호 입력]

    ↓

[평소 식생활 습관·알레르기 관련 정보·피하고 싶은 음식 입력]

    ↓

[AI Food Guide에 식생활 및 음식 추천 요청]

    ↓

[Backend에서 입력값 재검증 및 AI API 호출]

    ↓

[AI 응답의 JSON 구조 및 결과값 검증]

    ↓

[음식 및 식생활 추천 결과 화면]

사용자는 Home에서 서비스의 목적과 이용 방법을 확인한 뒤 Body Signal Section으로 이동한다.

몸 상태와 생활 신호, 평소 식생활 습관, 알레르기 관련 정보와 피하고 싶은 음식 등을 입력하고 AI Food Guide를 실행하면 Frontend에서 기본 입력값을 먼저 확인한다.

정상적인 입력값은 Backend로 전달되며, Backend에서 입력값을 다시 검증한 뒤 AI API에 요청을 전송한다.

AI가 생성한 응답은 정해진 JSON 구조와 필요한 결과값이 올바르게 포함되어 있는지 확인한 후 Frontend에 전달한다. 최종 결과 화면에서는 추천된 컬러푸드와 대표 식품, 추천 이유, 주요 영양정보, 섭취 시 참고사항 등을 보여준다.

입력 오류, AI API 오류, 네트워크 오류 또는 Timeout이 발생하는 경우에는 정상적인 추천 결과 화면을 보여주는 대신 사용자가 상황을 이해할 수 있는 오류 메시지를 표시한다.



## 6. AI 기능

### 6.1 AI 기능 개요

AI Food Guide는 사용자가 입력한 생활 속의 이상 신호 등 몸 상태와 평소 식생활 습관, 과일·채소의 섭취 정도, 알레르기 반응과 관련된 정보 및 피하고 싶은 음식 등을 바탕으로 식생활에 참고할 수 있는 컬러푸드·전체식·통곡물과 관련된 정보를 추천하고 이해하기 쉽게 설명하는 기능이다. 

대표 식품과 주요 영양정보에 대한 사실 확인이 중요하므로, 신뢰할 수 있는 자료를 바탕으로 미리 정리한 정보를 활용한다. AI는 이를 사용자의 입력에 맞게 선택하여 정리하고, 해당 식품을 추천하는 이유를 자연스러운 문장으로 생성하는 역할을 담당한다. 

AI는 사용자의 질병을 진단하거나 의학적 치료 방법을 결정하지 않으며, 생성된 결과는 건강한 식생활을 위한 참고 정보로 제공한다. 



### 6.2 AI 입력값

- 입력 1: 생활 속에서 느끼는 이상 신호 등 현재의 몸 상태 

- 입력 2: 평소 과일·채소의 섭취 정도 및 식생활 습관 

- 입력 3: 특정 식품에 대한 알레르기 반응과 관련된 정보 및 피하고 싶은 음식 정보 

- 기타 입력: 사용자가 추가로 전달하고 싶은 식생활 관련 내용 



### 6.3 AI 출력값

AI는 사용자의 입력을 바탕으로 다음과 같은 항목을 반환하도록 구성한다. 

- 추천하는 Color 

- 추천하는 Color에 해당하는 식품 중 대표 식품 

- 해당 식품을 추천하는 이유 

- 추천한 식품의 주요 영양정보 

- 대안으로 참고할 수 있는 식품과 관련 정보 

- Whole Food 또는 Whole Grain과 관련된 참고 정보 

- 식품 섭취 시 참고사항 

- 건강정보 이용 시 사용자가 참고할 주의 문구 

출력 결과는 사용자가 한눈에 이해할 수 있도록 정해진 구조로 반환하고, Frontend에서는 각각의 항목을 카드 형태로 구분하여 보여준다. 



### 6.4 AI 응답 JSON 구조

AI가 생성한 결과를 Frontend에서 일정한 형태로 표시하고 Backend에서 정상적인 응답인지 검증할 수 있도록 JSON 형식으로 응답을 구성한다.

예시는 다음과 같다.

```json

{

  "recommended_color": "Green",

  "representative_food": "키위",

  "reason": "키위를 추천하는 이유",

  "nutrition": [

    "비타민 C",

    "식이섬유",

    "칼륨"

  ],

  "alternative_foods": [

    "아보카도",

    "멜론"

  ],

  "food_guide": "Whole Food 또는 Whole Grain과 관련된 참고 정보",

  "caution": "식품 섭취 시 참고사항",

  "health_notice": "이 결과는 건강한 식생활을 위한 참고 정보이며 질병의 진단이나 치료를 대신하지 않습니다."

}

```

각 Key의 의미와 자료형은 다음과 같이 구성한다.

| Key | 자료형 | 내용 |

|---|---|---|

| `recommended_color` | String | 사용자의 입력을 바탕으로 추천하는 컬러 |

| `representative_food` | String | 추천 컬러에 해당하는 대표 식품 |

| `reason` | String | 해당 식품을 추천하는 이유 |

| `nutrition` | Array | 추천 식품의 주요 영양정보 |

| `alternative_foods` | Array | 대안으로 참고할 수 있는 식품 |

| `food_guide` | String | Whole Food 또는 Whole Grain과 관련된 참고 정보 |

| `caution` | String | 식품 섭취 시 참고사항 |

| `health_notice` | String | 건강정보 이용 시 사용자가 참고할 주의 문구 |



### 6.5 AI 응답 검증 순서

1. AI 응답이 올바른 JSON 형식인지 확인한다.

2. 필요한 필수 Key가 모두 포함되어 있는지 확인한다.

3. 각 Key의 값이 예상한 자료형(String, Array 등)과 일치하는지 확인한다.

4. 배열 항목과 결과값이 비어 있지 않고 예상한 범위의 값으로 구성되어 있는지 확인한다.

5. 검증을 통과한 결과만 Frontend로 전달하여 화면에 출력한다.

검증 과정에서 문제가 발견될 경우 잘못된 AI 응답을 그대로 화면에 표시하지 않고 Error로 처리하여 사용자에게 다시 시도하도록 안내한다.



## 7. 입력 검증

### 7.1 Frontend 검증

사용자가 AI Food Guide를 실행하기 전에 브라우저에서 필수 입력값이 정상적으로 입력되었는지 먼저 확인한다. 

몸 상태 또는 생활 속에서 느끼는 이상 신호와 같이 반드시 필요한 항목이 선택되지 않았거나 입력값이 비어 있는 경우에는 Backend와 AI API에 요청을 보내지 않고 사용자에게 입력 내용을 확인하도록 안내한다. 

직접 입력 항목에는 적절한 글자 수 제한 등을 적용하여 지나치게 길거나 예상하지 못한 입력이 전달되는 것을 방지한다. 

### 7.2 Backend 검증

Frontend에서 검증된 입력값도 Python 기반 Backend에서 다시 확인한다. 

Backend에서는 요청 데이터가 올바른 JSON 형식인지, 필요한 필수 항목이 존재하는지, 각 값의 자료형과 길이가 허용 범위에 해당하는지 등을 검사한다. 

검증에 실패한 요청은 AI API에 전달하지 않고 적절한 Error 응답을 Frontend로 반환한다. 

### 7.3 이중 검증을 하는 이유

Frontend 검증은 사용자가 잘못된 값을 입력했을 때 빠르게 안내하여 사용 편의성을 높이기 위한 과정이다. 

하지만 브라우저에서 이루어지는 Frontend 검증은 개발자 도구를 사용하거나 Backend에 직접 API 요청을 보내는 방식 등으로 우회될 수 있으므로, Backend에서도 입력값을 다시 검증한다. 

따라서 Frontend와 Backend에서 입력값을 각각 확인하는 이중 검증 방식을 적용하여 잘못되거나 예상하지 못한 데이터가 AI API에 전달되는 것을 줄인다. 

## 8. AI UX 및 실패 처리

### 8.1 Loading 처리

AI Food Guide 실행 후 AI 응답을 기다리는 동안 Loading 표시와 함께 **“식생활 안내서를 만들고 있습니다.”**와 같은 안내 문구를 보여준다. 

Loading 중에는 추천 버튼을 일시적으로 비활성화하여 사용자가 같은 요청을 반복해서 보내는 것을 방지한다. 

응답이 완료되거나 오류가 발생하면 Loading 상태를 종료한다. 

### 8.2 빈 입력 처리

- 발생 조건: 필수 Body Signal 항목이 선택되거나 입력되지 않은 경우 

- 사용자 안내: **“현재 몸 상태나 생활 신호에 해당하는 항목을 한 가지 이상 선택해 주세요.”** 

빈 입력은 Frontend에서 먼저 확인하여 불필요한 AI API 호출이 발생하지 않도록 한다. 

### 8.3 AI API 오류 처리

- 발생 조건: AI API가 정상적인 응답을 반환하지 않거나 4xx 또는 5xx 상태의 오류가 발생한 경우 

- 사용자 안내: **“AI 식생활 안내서를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.”** 

사용자 화면에는 이해하기 쉬운 메시지만 표시하고, 실제 HTTP 상태 코드나 세부 오류 내용은 개발 확인용 Log에서 확인하도록 구분한다. 

### 8.4 네트워크 오류 처리

발생 조건: 인터넷 연결 문제 또는 fetch() 요청 자체가 정상적으로 완료되지 않은 경우 

사용자 안내: “네트워크 연결을 확인한 후 다시 시도해 주세요.” 

네트워크 오류와 AI API 자체의 오류를 구분하여 사용자가 문제의 원인을 보다 쉽게 이해할 수 있도록 한다. 

### 8.5 Timeout 처리

Timeout 시간: 15초 

처리 방법: 설정한 시간 안에 정상적인 응답을 받지 못하면 AbortController를 이용하여 요청을 중단하고 Timeout으로 처리한다. 

사용자 안내: “응답 시간이 오래 걸리고 있습니다. 잠시 후 다시 시도해 주세요.” 

Timeout 발생 시 Loading 상태를 종료하고 다시 요청할 수 있도록 버튼을 활성화한다. 

## 9. 안전한 화면 출력

AI가 반환한 문자열을 `innerHTML`에 그대로 삽입하지 않고 `textContent` 등 안전한 방식으로 화면에 출력한다.

AI 응답의 JSON 구조와 필요한 Key를 먼저 검증한 뒤 검증된 값만 각각의 화면 요소에 표시하도록 구성한다.

이를 통해 AI 응답이나 사용자 입력에 HTML 또는 Script 형식의 문자열이 포함되더라도 웹페이지의 코드로 해석하거나 실행하지 않고 일반 문자로 표시하여, 예상하지 못한 화면 변경이나 보안 문제가 발생할 가능성을 줄인다.

또한 사용자에게 보여주는 오류 메시지와 개발자가 확인하는 세부 Error Log를 구분하여, API Key나 내부 오류 정보와 같은 민감한 정보가 사용자 화면에 노출되지 않도록 한다.

## 10. 기술 스택

### Frontend

- HTML: 웹페이지의 전체 구조와 각 Page / Section의 콘텐츠를 구성한다.

- CSS: 색상, 글꼴, 카드, 버튼, Layout 및 반응형 화면 등 웹페이지의 디자인을 담당한다.

- JavaScript: 사용자 입력 처리, 입력값 검증, Page / Section 이동, Backend 요청, Loading·Error 처리 및 AI 결과 화면 출력을 담당한다.

### Backend

- Language: Python

- Platform: Vercel Serverless Functions

- API Directory: `api/`

- 주요 역할: Frontend에서 전달된 입력값을 다시 검증하고 OpenAI API를 호출하며, AI 응답의 JSON 구조와 결과값을 검증한 후 Frontend에 전달한다.

### AI API

- Provider: OpenAI

- Model: `gpt-5.6-luna`

- Python SDK: OpenAI

- 사용 목적: 사용자의 생활 속 이상 신호 등 몸 상태와 식생활 습관 등을 바탕으로 미리 정리된 컬러푸드·전체식·통곡물 정보를 참고하여, 참고할 컬러푸드와 대표 식품을 선택하고 해당 식품을 추천하는 이유와 사용자가 이해하기 쉬운 식생활 안내 문구를 생성하는 데 사용한다.

### Deployment

- Hosting: Vercel

- Repository: GitHub

- 역할: GitHub에서 프로젝트 코드와 변경 이력을 관리하고, GitHub Repository를 Vercel과 연결하여 실제 웹 서비스를 배포한다.

## 11. 프로젝트 구조

```text

body-signal-color-food/

├── index.html

├── css/

│   └── style.css

├── js/

│   └── main.js

├── api/

│   └── recommend.py

├── images/

│   └── [실제 사용한 이미지 파일]

├── requirements.txt

├── .env.example

├── .gitignore

├── README.md

└── SERVICE_PLAN.md

## 12. Frontend ↔ Backend 연동 구조

```text

사용자 입력

   ↓

JavaScript에서 입력값 검증

   ↓

fetch("/api/recommend")

   ↓

Vercel Serverless Function (Python)

   ↓

Backend에서 입력값 재검증

   ↓

OpenAI API 호출

   ↓

AI 응답

   ↓

Backend에서 JSON 구조 및 결과값 검증

   ↓

JSON 응답

   ↓

Frontend에서 응답 확인 및 안전한 화면 출력

```

Frontend의 JavaScript는 사용자의 입력값을 확인한 뒤 `fetch()`를 이용하여 `/api/recommend` Endpoint에 요청을 전송한다.

Python 기반 Backend에서는 입력값을 다시 검증한 후 OpenAI API를 호출한다. AI가 생성한 응답은 Backend에서 JSON 구조와 필요한 결과값을 확인한 뒤 Frontend로 전달한다.

Frontend에서는 전달받은 결과를 확인하고 `textContent` 등을 이용하여 사용자 화면에 안전하게 표시한다.

※ `/api/recommend`는 `api/recommend.py`를 사용하는 경우의 권장 Endpoint이다. 실제 파일명이 달라지면 수정한다.

## 13. 로컬 실행 방법

### 13.1 저장소 내려받기

```bash

git clone [실제 GitHub Repository URL]

```

### 13.2 프로젝트 폴더 이동

```bash

cd body-signal-color-food

```

### 13.3 Python 패키지 설치

프로젝트에서 사용하는 Python Package를 `requirements.txt`를 이용하여 설치한다.

```bash

pip install -r requirements.txt

```

`requirements.txt`에는 OpenAI API 호출을 위한 `openai`, FastAPI Backend 실행을 위한 `fastapi`,

로컬 개발 서버 실행을 위한 `uvicorn`이 포함되어 있다.

### 13.4 환경변수 설정

OpenAI API를 호출하려면 `AI_API_KEY` 환경변수가 필요하다.

WSL / Linux 환경에서는 다음과 같이 설정할 수 있다.

```bash

export AI_API_KEY="your_api_key_here"

```

환경변수가 정상적으로 설정되었는지는 실제 Key 값을 출력하지 않고 다음과 같이 확인할 수 있다.

```bash

python -c "import os; print('SET' if os.getenv('AI_API_KEY') else 'NOT SET')"

```

정상적으로 설정된 경우 다음과 같이 표시된다.

```text

SET

```

실제 OpenAI API Key 값은 README나 Source Code에 직접 작성하지 않는다.

### 13.5 FastAPI 로컬 실행

개발 과정에서 FastAPI Backend와 Frontend의 실제 연동을 확인하기 위해 Uvicorn으로 로컬 서버를 실행하였다.

```bash

python -m uvicorn api.recommend:app --host 127.0.0.1 --port 8000

```

정상적으로 실행되면 Terminal에 다음과 같은 메시지가 표시된다.

```text

INFO:     Started server process [...]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://127.0.0.1:8000

```

Browser 접속 주소:

```text

http://localhost:8000

```

`recommend.py`의 FastAPI App에서 `index.html`, CSS, JavaScript 및 `/api/recommend` Endpoint를 함께 제공하도록 구성하여,

한 개의 로컬 서버에서 Frontend와 Backend의 연동을 확인할 수 있다.

### 13.6 AI 기능 로컬 동작 확인

Body Signal에서 사용자 입력값을 설정한 뒤 `AI Food Guide 실행` 버튼을 누르면

Frontend의 JavaScript가 `/api/recommend` Endpoint로 POST 요청을 전송한다.

정상적으로 처리된 경우 Terminal에서 다음과 같이 확인할 수 있다.

```text

POST /api/recommend HTTP/1.1" 200 OK

```

실제 테스트에서 사용자 입력을 바탕으로 OpenAI API 호출이 정상적으로 수행되었으며,

추천 컬러푸드, 대표 식품, 추천 이유, 주요 영양정보,

함께 살펴볼 식품, Whole Food·Whole Grain 참고 정보,

섭취 시 참고사항 및 건강정보 이용 시 주의사항이 결과 화면에 정상적으로 출력되는 것을 확인하였다.

### 13.7 Vercel 로컬 개발 환경 확인

Vercel 배포 구조를 로컬에서 확인할 때에는 Vercel CLI를 사용할 수 있다.

```bash

nvm use 22

vercel dev --debug

```

정상적으로 실행되면 다음과 같이 표시된다.

```text

Ready! Available at http://localhost:3000

```

접속 주소:

```text

http://localhost:3000

```

개발 과정에서는 Vercel CLI를 이용하여 Python Runtime과 FastAPI App의 연결 상태를 확인하였고,

실제 AI 기능의 최종 로컬 동작 검증은 Uvicorn을 이용한 `http://localhost:8000` 환경에서 수행하였다.

최종 제출 전에는 localhost 테스트에 그치지 않고 실제 Vercel 배포 URL에서도

Page / Section 이동, 사용자 입력, OpenAI API 호출 및 AI 결과 출력이 정상적으로 동작하는지 다시 확인한다.



## 14. 환경변수 관리

### 필요한 환경변수

| 환경변수 | 용도 |

|---|---|

| `AI_API_KEY` | Python Backend에서 OpenAI API를 호출할 때 사용하는 인증 정보 |

### 로컬 환경변수 설정 방법

로컬 개발 환경에서는 프로젝트 최상위에 `.env` 파일을 만들어 실제 OpenAI API Key를 환경변수로 관리한다.

예:

```text

AI_API_KEY=your_api_key_here

```

실제 API Key 값은 코드나 README에 직접 작성하지 않는다.

`.env` 파일은 `.gitignore`에 등록하여 GitHub에 Commit 또는 Push되지 않도록 한다.

`.env.example`에는 실제 비밀값을 입력하지 않고 필요한 환경변수 이름과 예시 형식만 작성한다.

예:

```text

AI_API_KEY=your_api_key_here

```

### Vercel 환경변수 설정 방법

Vercel Project의 Environment Variables에서 다음 환경변수를 등록한다.

```text

AI_API_KEY

```

Value에는 실제 발급받은 OpenAI API Key를 입력한다.

로컬의 `.env` 파일과 Vercel의 Environment Variables는 별도로 관리되므로, Vercel 배포 환경에도 동일한 이름의 환경변수를 직접 등록해야 한다.

환경변수를 추가하거나 변경한 경우에는 다시 배포한 뒤 실제 Vercel URL에서 OpenAI API 기능이 정상적으로 동작하는지 확인한다.

## 15. API Key 보안

OpenAI API Key는 Frontend 코드에 직접 작성하지 않고 Python 기반 Backend에서 환경변수를 통해 불러오도록 구성한다.

실제 API Key가 포함된 `.env` 파일은 `.gitignore`에 등록하여 GitHub에 Commit 또는 Push되지 않도록 한다.

README.md, SERVICE_PLAN.md, Source Code, GitHub Repository 및 과제 증빙 Screenshot에도 실제 OpenAI API Key가 노출되지 않도록 확인한다.

Frontend에서 OpenAI API Key를 직접 사용하지 않고 다음 구조를 사용한다.

```text

Frontend

   ↓

Python Backend

   ↓

OpenAI API

```

이를 통해 사용자의 Browser에서 API Key가 직접 노출되지 않도록 한다.

### API Key 유출 시 대응

1. 유출된 기존 OpenAI API Key를 즉시 폐기한다.

2. 새로운 OpenAI API Key를 발급한다.

3. 로컬 `.env` 파일의 `AI_API_KEY` 값을 새로운 Key로 변경한다.

4. Vercel Environment Variables의 `AI_API_KEY`도 새로운 Key로 변경한다.

5. Vercel에 다시 배포한다.

6. 실제 Vercel URL에서 AI 기능이 정상적으로 동작하는지 확인한다.

7. GitHub Commit 이력을 확인하여 Key가 포함된 기록이 있는 경우 노출된 이력까지 확인하고 필요한 정리 작업을 수행한다.

단순히 현재 파일에서 API Key를 삭제하는 것만으로는 이전 Git Commit에 Key가 남아 있을 수 있으므로 Commit 이력까지 확인한다.

## 16. requirements.txt

Python Backend에서 FastAPI Web Application을 실행하고 OpenAI API를 호출하기 위해

프로젝트에서 실제 사용하는 Python Package를 `requirements.txt`에 작성한다.

현재 `requirements.txt`는 다음과 같이 구성되어 있다.

```text

openai

fastapi

uvicorn

```

각 Package의 역할은 다음과 같다.

| Package | 역할 |

|---|---|

| `openai` | Python Backend에서 OpenAI API를 호출하기 위한 공식 Python SDK |

| `fastapi` | `/api/recommend` Endpoint와 Frontend 정적 파일 제공 등을 처리하는 Python Web Framework |

| `uvicorn` | FastAPI ASGI Application을 로컬 환경에서 실행하기 위한 Web Server |

개발 환경에서는 다음 명령으로 필요한 Package를 한 번에 설치할 수 있다.

```bash

pip install -r requirements.txt

```

실제 Backend에서 사용하는 Package만 `requirements.txt`에 작성하여,

다른 개발 환경이나 Vercel 배포 환경에서도 동일한 Python 의존성을 설치할 수 있도록 관리한다.



## 17. 반응형 웹

### Desktop

- 확인 해상도: 1920 × 1080

- 확인 결과: Navigation, 입력 Form, 버튼, 정보 카드 및 AI 결과 화면이 Desktop 화면 크기에 맞게 정상적으로 표시되는 것을 확인하였다.

### Mobile

- 확인 해상도: 390 × 844

- 확인 결과: Navigation이 Hamburger Menu 형태로 전환되고, 입력 Form과 각 Section의 콘텐츠가 한 열 구조로 배치되며, 버튼과 텍스트가 화면 밖으로 벗어나거나 서로 겹치지 않는 것을 확인하였다.

CSS Media Query를 이용하여 Desktop과 Mobile 화면 크기에 맞게 Layout이 조정되도록 구현하였다.

Mobile에서는 Navigation, 입력 Form, 카드, 버튼 및 AI 결과가 화면 밖으로 벗어나거나 서로 겹치지 않는지 실제 Browser의 반응형 모드에서 확인하였다.



### Mobile 반응형 실행 화면

아래 화면은 Chrome 개발자 도구의 Responsive Mode에서 `390 × 844` 크기로 실제 서비스를 확인한 결과이다.





## 18. Navigation

상단 Navigation을 통해 Home, Body Signal, AI Food Guide, Color Guide, Whole Food, Whole Grain, Nutrition, About, FAQ 등의 주요 Page / Section으로 이동할 수 있도록 구성한다.

Desktop에서는 주요 Menu를 Navigation에 표시하고, Mobile에서는 화면 크기를 고려하여 Hamburger Menu 등 모바일에 적합한 Navigation 방식을 적용한다.

Color Guide에서는 Yellow·Purple·Red·Green 중 관심 있는 컬러를 선택하여 해당 컬러푸드의 상세 정보를 확인할 수 있는 Section으로 이동할 수 있도록 구성한다.

현재 위치를 사용자가 쉽게 확인할 수 있도록 선택된 Menu 또는 Section에 시각적인 변화를 적용한다.

※ 실제 구현 과정에서 Section을 통합하거나 Menu 구성이 변경되면 최종 화면에 맞게 수정한다.

## 19. 배포

### Vercel 배포 URL

```text

[실제 Vercel 배포 후 URL 입력]

```

### GitHub Repository

```text

[실제 GitHub Repository URL 입력]

```

### GitHub ↔ Vercel 연동

프로젝트 코드는 GitHub Repository에서 관리하고 해당 Repository를 Vercel Project와 연결한다.

코드를 수정한 후 Git Commit과 Push를 수행하면 연결된 Vercel에서 변경된 코드를 기준으로 새로운 배포가 자동으로 진행되도록 구성한다.

배포 과정에서 문제가 발생한 경우 다음 순서로 확인한다.

```text

Deployments

    ↓

Build Logs

    ↓

Runtime Logs

    ↓

코드 및 환경변수 확인·수정

    ↓

Git Commit / Push

    ↓

자동 재배포

    ↓

실제 Vercel URL에서 다시 검증

```

## 20. 배포 환경 동작 확인

| 확인 항목 | 결과 |

|---|---|

| Page / Section 이동 | [실제 Vercel 배포 후 확인] |

| Desktop Layout | [실제 Vercel 배포 후 확인] |

| Mobile Layout | [실제 Vercel 배포 후 확인] |

| 사용자 입력 | [실제 Vercel 배포 후 확인] |

| OpenAI API 호출 | [실제 Vercel 배포 후 확인] |

| AI 결과 출력 | [실제 Vercel 배포 후 확인] |

| 빈 입력 Error | [실제 Vercel 배포 후 확인] |

| OpenAI API Error | [실제 Vercel 배포 후 확인] |

| Timeout | [실제 Vercel 배포 후 확인] |

localhost에서 정상적으로 동작하는 것만으로 완료로 판단하지 않고, 실제 Vercel URL에서도 각 기능을 직접 확인한 후 결과를 기록한다.

## 21. 테스트 Case

### Test 1 — 정상 입력

**입력 예시:**

- 생활 속 이상 신호 등 몸 상태: 식사가 불규칙함
- 과일·채소 섭취 현황: 충분함
- 평소 식생활 습관: 간편식이나 외식을 자주 이용함
- 알레르기 관련 정보: 없음
- 피하고 싶은 음식: 없음

**실행 전 화면**

![정상 입력 테스트 실행 전](./images/27.%20NormalInputTestBefore.png)

**예상 결과:**

AI가 사용자의 입력을 바탕으로 참고할 컬러푸드와 대표 식품을 선택하고,
해당 식품을 추천하는 이유, 주요 영양정보, 대안 식품,
Whole Food·Whole Grain 참고 정보 및 섭취 시 참고사항 등을 생성하여
결과 화면에 정상적으로 표시한다.

**실제 결과:**

정상 입력값을 설정한 뒤 AI Food Guide를 실행한 결과,
AI 추천 결과가 정상적으로 생성되었으며 추천 컬러푸드로 `Green`,
대표 식품으로 `키위`가 표시되었다.

또한 추천 이유, 주요 영양정보, 함께 살펴볼 식품,
Whole Food·Whole Grain 참고 정보, 섭취 시 참고사항 및
건강정보 이용 시 주의사항이 정상적으로 출력되는 것을 확인하였다.

![정상 입력 실제 테스트 결과](./images/28.%20NormalInputResult.png)



### Test 2 — 빈 입력

**입력:**

필수 Body Signal 항목을 선택하지 않은 상태에서 AI Food Guide 실행

**실행 전 화면**

![빈 입력 테스트 실행 전](./images/25.%20EmptyInputTestBefore.png)

**예상 결과:**

Frontend에서 빈 입력을 확인하여 Backend로 요청을 보내지 않고, 결과적으로 AI API도 호출하지 않는다.

**“생활 속 이상 신호 등 몸 상태를 한 가지 이상 선택하거나 기타 상태를 입력해 주세요.”**라는 안내 메시지를 표시한다.

**실제 결과:**

필수 Body Signal을 선택하지 않은 상태에서 AI Food Guide를 실행한 결과,
Frontend에서 빈 입력을 감지하고 사용자에게 입력 항목을 확인하도록 안내 메시지가 정상적으로 표시되는 것을 확인하였다.

![빈 입력 Error 실제 테스트 결과](./images/26.%20EmptyInputErrorResult.png)



### Test 3 — AI API 오류

**조건:**

정상적인 사용자 입력값을 설정한 상태에서 Backend에서 AI API 호출 직전에 의도적으로 오류를 발생시켰다.

**실행 전 화면**

![AI API Error 테스트 실행 전](./images/29.%20APIErrorTestBefore.png)

**예상 결과:**

Loading 상태를 종료하고 **“AI 식생활 안내서를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.”**라는 안내 메시지를 표시한다.

세부 오류 정보는 사용자 화면에 직접 노출하지 않고 개발 확인용 Log에서 확인한다.

**실제 결과:**

정상 입력값을 설정한 뒤 AI Food Guide를 실행하고, Backend에서 AI API Error를 의도적으로 발생시킨 결과,

Loading 상태가 종료되고 사용자 화면에

**“AI 식생활 안내서를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.”**

라는 안내 메시지가 정상적으로 표시되는 것을 확인하였다.

![AI API Error 실제 테스트 결과](./images/30.%20APIErrorResult.png)


**오류 테스트 종료 후 정상 복구 확인**

Test 3을 위해 추가했던 강제 오류 코드를 제거한 뒤 Backend 서버를 다시 시작하고,

동일한 서비스가 정상 상태로 복구되는지 추가로 확인하였다.

**Backend 서버 재시작 화면**

![AI API Error 테스트 후 Backend 서버 재시작](./images/31.%20APIErrorRecoveryServerRestart.png)

Terminal에서 기존 Uvicorn Server를 종료한 뒤 다시 실행하여,

새 Server Process가 시작되고 `http://127.0.0.1:8000`에서 정상적으로 실행되는 것을 확인하였다.


**정상 복구 확인 실행 전 화면**

![AI API Error 테스트 후 정상 복구 확인 실행 전](./images/32.%20APIErrorRecoveryTestBefore.png)

강제 오류 코드를 제거한 상태에서 정상 입력값을 다시 설정하고

AI Food Guide를 실행하여 정상 기능 복구 여부를 확인하였다.


**정상 복구 결과 화면**

![AI API Error 테스트 후 정상 복구 결과](./images/33.%20APIErrorRecoveryResult.png)

AI Food Guide를 다시 실행한 결과,

추천 컬러푸드 `Green`, 대표 식품 `키위`와 함께

추천 이유, 주요 영양정보, 함께 살펴볼 식품,

Whole Food·Whole Grain 참고 정보,

섭취 시 참고사항 및 건강정보 이용 시 주의사항이 정상적으로 출력되는 것을 확인하였다.

이를 통해 Test 3에서 사용한 강제 오류 코드가 제거된 이후

Backend와 AI 기능이 정상 상태로 복구되었음을 확인하였다.



### Test 4 — Timeout

**조건:**

AI 응답이 Frontend에 설정된 15초 Timeout 시간을 초과하도록
Backend에서 의도적으로 20초 지연을 발생시켰다.

**Timeout 테스트 설정 화면**

![Timeout 테스트 설정](./images/34.%20TimeoutTestSetup.png)

`recommend.py`의 OpenAI API 호출 직전에 `await asyncio.sleep(20)`을 임시로 추가하고,
Uvicorn Server를 다시 시작하여 Timeout 테스트 환경을 구성하였다.

**실행 전 화면**

![Timeout 테스트 실행 전](./images/35.%20TimeoutTestBefore.png)

정상적인 사용자 입력값을 설정한 뒤 `AI Food Guide 실행`을 준비하였다.

**예상 결과:**

Frontend에서 설정한 15초 안에 응답을 받지 못하면 `AbortController`를 이용하여 요청을 중단하고 Loading 상태를 종료한다.

**“응답 시간이 오래 걸리고 있습니다. 잠시 후 다시 시도해 주세요.”**라는 안내 메시지를 표시하고 다시 요청할 수 있도록 한다.

**실제 결과:**

Backend에서 의도적으로 20초 지연을 발생시킨 상태에서 AI Food Guide를 실행한 결과,
Frontend의 15초 Timeout이 정상적으로 동작하였다.

Loading 상태가 종료되고 사용자 화면에

**“응답 시간이 오래 걸리고 있습니다. 잠시 후 다시 시도해 주세요.”**

라는 안내 메시지가 정상적으로 표시되는 것을 확인하였다.

![Timeout 실제 테스트 결과](./images/36.%20TimeoutResult.png)

**Timeout 테스트 종료 후 정상 복구 확인**

Test 4를 위해 임시로 추가했던 `await asyncio.sleep(20)` 코드를 제거한 뒤
Backend 서버를 다시 시작하고 정상 기능이 복구되는지 확인하였다.

**정상 복구 확인 실행 전 화면**

![Timeout 테스트 후 정상 복구 확인 실행 전](./images/37.%20TimeoutRecoveryTestBefore.png)

Timeout 강제 발생 코드를 제거한 상태에서 정상적인 사용자 입력값을 다시 설정하고
AI Food Guide를 실행하여 정상 기능 복구 여부를 확인하였다.

**정상 복구 결과 화면**

![Timeout 테스트 후 정상 복구 결과](./images/38.%20TimeoutRecoveryResult.png)

AI Food Guide를 다시 실행한 결과,
추천 컬러푸드 `Green`, 대표 식품 `키위`와 함께
추천 이유, 주요 영양정보, 함께 살펴볼 식품,
Whole Food·Whole Grain 참고 정보,
섭취 시 참고사항 및 건강정보 이용 시 주의사항이 정상적으로 출력되는 것을 확인하였다.

이를 통해 Test 4에서 사용한 Timeout 강제 발생 코드가 제거된 이후
Backend와 AI 기능이 정상 상태로 복구되었음을 확인하였다.



## 22. 서비스 데이터 / 정보 출처

### 22.1 컬러푸드

Yellow·Purple·Red·Green 컬러푸드의 대표 식품과 주요 영양정보는 KBS 「생로병사의 비밀」의 「컬러과일 건강법」 관련 정리자료를 참고하여 구성한다.

컬러푸드 정보는 특정 색깔의 식품이 특정 질병을 치료하거나 증상을 개선한다고 단정하는 방식으로 사용하지 않고, 색깔에 따라 서로 다른 영양성분과 식물성 성분을 살펴볼 수 있다는 점을 중심으로 정리한다.

서비스에서는 다음과 같은 대표 식품을 중심으로 정보를 구성한다.

- Yellow: 레몬, 감귤류

- Purple: 블루베리, 포도

- Red: 체리, 복분자, 토마토, 사과

- Green: 키위, 아보카도, 멜론

대표 식품과 영양성분 정보는 AI가 임의로 생성하도록 하지 않고, 신뢰할 수 있는 자료를 바탕으로 미리 정리한 정보를 우선 활용한다.



### 22.2 Whole Food

Whole Food 정보는 KBS 「생로병사의 비밀」의 전체식 관련 정리자료를 참고하여 구성한다.

과일과 채소의 먹을 수 있는 껍질이나 겉부분을 활용하는 방법과 함께, 식품에 따라 섭취 가능한 부분과 먹지 않는 부분을 구분해야 한다는 점을 안내한다.

또한 껍질째 섭취할 수 있는 식품도 충분한 세척과 위생 관리가 필요하다는 내용을 포함하고, 사용자가 일상에서 참고할 수 있도록 식품별 세척·조리·활용 방법을 정리하여 제공한다.

모든 과일과 채소의 껍질을 섭취하도록 권장하지 않으며, 식품의 종류와 상태에 따라 적절하게 활용하도록 안내한다.



### 22.3 Whole Grain

Whole Grain 정보는 KBS 「생로병사의 비밀」의 통곡물 관련 정리자료를 참고하여 구성한다.

현미·통밀·통메밀 등 곡물의 겉부분과 배아를 비교적 많이 유지하고 있는 대표적인 통곡물의 종류와 특징을 정리한다.

통곡물에서 살펴볼 수 있는 식이섬유, 비타민, 미네랄, 단백질 등의 영양정보를 제공하며, 정제된 곡물과의 차이를 사용자가 쉽게 이해할 수 있도록 설명한다.

통곡물이 모든 사용자에게 동일하게 적합하다고 단정하지 않고 개인의 식습관과 소화 상태 등을 고려할 수 있도록 참고 정보 형태로 제공한다.



### 22.4 정보 활용 원칙

서비스에서 사용하는 대표 식품, 주요 영양성분, 컬러푸드·전체식·통곡물에 대한 기본 정보는 신뢰할 수 있는 자료를 참고하여 미리 정리한다.

AI는 이러한 기본 정보를 임의로 변경하거나 새로운 건강 사실을 만들어 내는 역할을 하지 않는다.

AI는 사용자가 입력한 생활 속 이상 신호 등 몸 상태와 식생활 습관을 바탕으로 미리 정리된 정보 중 참고할 컬러푸드와 대표 식품을 선택하고, 해당 식품을 추천하는 이유와 사용자가 이해하기 쉬운 식생활 안내 문구를 생성하는 역할을 담당한다.

건강과 관련된 정보는 특정 식품이 특정 질병을 예방하거나 치료한다고 단정하지 않고, 건강한 식생활을 위한 참고 정보로 제공한다.
