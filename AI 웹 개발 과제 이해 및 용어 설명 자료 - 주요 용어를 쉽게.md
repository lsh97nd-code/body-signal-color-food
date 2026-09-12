# AI 웹 개발 과제 이해 및 용어 설명 자료 (주요 용어를 쉽게)

## 빠르게 보는 핵심 용어

| 용어 | 가장 쉽게 말하면 | 이번 프로젝트에서의 역할 |
|---|---|---|
| HTML | 무엇이 있는가 | 제목, Form, Button, Section, 결과 영역 구성 |
| CSS | 어떻게 보이는가 | 색상, 글꼴, Card, 간격, Desktop·Mobile Layout |
| JavaScript | 무엇이 일어나는가 | 입력 검증, `fetch()`, Loading, Error, 결과 출력 |
| Frontend | 사용자가 보고 조작하는 영역 | `index.html`, `css/style.css`, `js/main.js` |
| Backend | 보이지 않는 곳에서 실제 처리 | `api/recommend.py`, 입력 재검증, AI API 호출 |
| API | 프로그램끼리 통신하는 약속 | Browser ↔ Backend ↔ OpenAI 연결 |
| Endpoint | 특정 API 기능의 주소 | `/api/recommend` |
| JSON | 프로그램끼리 주고받기 쉬운 데이터 형식 | AI 결과를 일정한 구조로 반환 |
| Validation | 값이 올바른지 검사 | Frontend + Backend 이중 검증 |
| Local | 내 컴퓨터에서 개발·시험하는 환경 | `localhost:8000` |
| Production | 실제 사용자가 이용하는 운영 환경 | Vercel 배포 URL |
| Git | 변경 이력 관리 | Commit 기록 |
| GitHub | Git 저장소를 온라인에 보관 | 코드와 문서 관리 |
| Vercel | 웹 서비스를 Build·Deploy하는 Platform | Frontend + Python Backend 배포 |

---


## 2. Frontend와 Backend


웹 서비스는 크게 Frontend와 Backend로 나누어 생각하면 이해하기 쉽다.


사용자가 직접 보고 클릭하고 입력하는 부분이 Frontend이고, 사용자의 눈에는 보이지 않지만 실제 데이터 처리와 API 호출을 담당하는 부분이 Backend다.


쉽게 건물에 비유하면 다음과 같다.


Frontend

= 사용자가 직접 이용하는 건물 내부 공간


Backend

= 일반 사용자에게 보이지 않는 관리실

### Frontend란?


Front + End라는 말처럼 사용자의 앞쪽에서 보이고 사용자가 직접 조작하는 부분이다.


Browser에서 보이는 다음 요소들이 모두 Frontend에 해당한다.


- 제목
- Navigation
- 입력 Form
Checkbox

Button

AI 결과 Card

Loading 안내

Error 메시지

- Hamburger Menu

이번 프로젝트에서 Frontend를 담당하는 주요 파일은 다음과 같다.


index.html

css/style.css

js/main.js


건물에 비유하면 Frontend는 손님이 직접 이용하는 공간이다.


사용자는 건물의 관리실 내부가 어떻게 구성되어 있는지 알 필요 없이, 문을 열고 버튼을 누르고 필요한 서비스를 이용하면 된다.


웹 서비스도 마찬가지다.


사용자는 AI API가 내부에서 어떻게 호출되는지 몰라도 화면에서 Body Signal을 선택하고 AI Food Guide 실행 버튼을 누르면 된다.


### Backend란?


Backend는 사용자의 화면 뒤에서 실제 처리를 담당하는 부분이다.


이번 프로젝트에서 핵심 Backend 파일은:


api/recommend.py


이다.


Backend에서는 다음과 같은 작업이 이루어진다.


Frontend의 요청 받기

↓

사용자 입력값 다시 확인

↓

환경변수에서 API Key 가져오기

↓

OpenAI API 호출

↓

AI가 반환한 결과 확인

↓

Frontend에 결과 반환


건물에 비유하면 Backend는 일반 사용자가 직접 들어갈 수 없는 관리실과 비슷하다.


건물 이용자는 엘리베이터를 타기 위해 기계실의 배선이나 제어장치를 직접 조작하지 않는다.


마찬가지로 Browser에서 API Key나 AI API를 직접 다루게 하지 않고 Backend가 대신 처리한다.


따라서 Backend를 사용하는 이유는 단순히 코드를 나누기 위해서만이 아니라 보안과 데이터 처리 역할을 분리하기 위해서이기도 하다.


## 3. HTML / CSS / JavaScript


HTML, CSS, JavaScript는 Frontend를 구성하는 가장 기본적인 세 가지 기술이다.


가장 짧게 기억하면 다음과 같다.


HTML = 무엇이 있는가

CSS = 어떻게 보이는가

JavaScript = 무엇이 일어나는가


건물에 비유하면 다음과 같이 이해할 수 있다.


HTML       = 건물의 구조와 공간

CSS        = 건물의 인테리어

JavaScript = 사용자가 조작하는 전기·작동 장치

Backend    = 건물 뒤편의 관리실

AI         = 관리실이 요청하는 전문 서비스

### HTML


HTML = HyperText Markup Language


HTML은 웹페이지에 어떤 내용과 요소가 존재하는지 정한다.


단순히 “눈에 보이는 구조”라고만 생각하기보다는, 건물에서:


어디에 문이 있는가?

어디에 방이 있는가?

어디에 계단이 있는가?

어떤 공간이 존재하는가?


를 정한다고 생각하면 쉽다.


이번 프로젝트에서는 HTML이 다음과 같은 요소를 만든다.


서비스 제목

- Navigation
Body Signal 입력 영역

AI Food Guide 실행 Button

AI 결과 표시 영역

Color Guide

Whole Food

Whole Grain

- FAQ

예를 들어:


`<button>AI Food Guide 실행</button>`


이라고 작성하면 화면에 Button이라는 요소 자체가 생긴다.


하지만 HTML만으로는 버튼을 예쁘게 만들거나 클릭했을 때 AI가 실행되게 만들지는 않는다.


즉:


HTML은 웹페이지에 무엇이 존재하는지 결정한다.


### CSS


CSS = Cascading Style Sheets


CSS는 HTML이 만든 요소를 어떻게 보이게 할지 결정한다.


건물로 보면 인테리어와 비슷하다.


벽 색깔

가구 위치

공간의 간격

- 글자 크기
조명

전체 분위기


를 정하는 것과 같다.


이번 프로젝트에서는 CSS가 다음을 담당한다.


Color

Font Size

Button Style

Card Design

Margin / Padding

Layout

Desktop 배치

Mobile 배치


예를 들어 HTML로 같은 Button을 만들어도 CSS에 따라:


작은 회색 Button

큰 둥근 Button

강조된 색상의 Button


등으로 전혀 다르게 보일 수 있다.


또한 Mobile에서는 Desktop과 화면 폭이 다르기 때문에 CSS의 Media Query를 이용하여 Layout을 변경한다.


즉:


CSS는 HTML 요소가 사용자에게 어떻게 보이는지 결정한다.


### JavaScript


JavaScript는 웹페이지에서 사용자의 행동에 반응하고 실제 동작을 수행하도록 만든다.


건물로 비유하면:


전등 Switch

자동문

Elevator

센서

작동 장치


와 비슷하다.


문과 엘리베이터가 건물에 존재하는 것은 HTML에 가깝고, 그 모양과 색은 CSS에 가깝다.


하지만 사용자가 Button을 눌렀을 때 실제로 Elevator가 움직이는 것은 JavaScript의 역할과 비슷하다.


이번 프로젝트에서 JavaScript는 다음과 같은 일을 한다.


사용자가 입력한 값 읽기

↓

입력값 확인

↓

AI Food Guide Button Click 감지

↓

- Loading 표시
↓

`fetch()로 Backend 호출`

↓

응답 받기

↓

AI 결과 화면 표시


또한:


### Timeout

Error 처리

- Hamburger Menu
My Foods 저장


등의 동작도 JavaScript가 담당한다.


즉:


JavaScript는 웹페이지에서 무엇이 일어나는지를 결정한다.


## 4. Client와 Server


웹 서비스를 이해할 때 Client와 Server를 알아두면 Frontend와 Backend 관계도 훨씬 쉽게 이해할 수 있다.


### Client


Client는 서비스를 요청하는 쪽이다.


이번 프로젝트에서는 사용자가 사용하는 Browser가 대표적인 Client다.


Chrome

Edge

Safari


등이 Client 역할을 한다.


사용자가 Browser에서:


AI Food Guide 실행


버튼을 누르면 Browser는 Backend에 필요한 처리를 요청한다.


### Server


Server는 Client의 요청을 받아 처리하고 결과를 돌려주는 쪽이다.


이번 프로젝트에서는 Vercel에서 실행되는 Python Backend가 Server 역할을 한다.


따라서 다음처럼 이해할 수 있다.


Browser(Client)

↓

"추천 결과를 만들어 주세요."

↓

Server(Backend)

↓

처리

↓

"결과는 이것입니다."

↓

Browser(Client)


쉽게 말하면 식당에서:


손님 = Client

주문 = Request

주방 = Server

완성된 음식 = Response


와 비슷하다.


## 5. API


API = Application Programming Interface


서로 다른 프로그램이나 서비스가 정해진 방법으로 요청과 응답을 주고받을 수 있도록 만든 연결 방식이다.


API를 음식점에 비유하면 주문 창구와 비슷하다.


손님이 직접 주방 안으로 들어가서 요리사에게 명령하지 않고, 정해진 주문 방법으로 요청한다.


프로그램도 마찬가지다.


이번 프로젝트에서는:


Browser

↓

우리 Backend API

↓

OpenAI API


라는 구조가 사용된다.


즉 Browser가 OpenAI API를 직접 호출하는 것이 아니라, 먼저 우리 Backend에 요청한다.


Frontend

↓

`/api/recommend`

↓

Python Backend

↓

OpenAI API


이 구조를 사용하면 API Key를 Browser에 노출하지 않고 Backend에서 안전하게 관리할 수 있다.


## 6. Endpoint


API가 서비스 전체의 주문 시스템이라면 Endpoint는 특정 업무를 담당하는 창구라고 볼 수 있다.


이번 프로젝트의 대표 Endpoint는:


`/api/recommend`


이다.


이 주소로 요청을 보내면 Backend가 AI 식생활 안내서를 만드는 처리를 수행한다.


예를 들어 서비스가 더 커진다면:


`/api/recommend`

`/api/login`

`/api/users`

`/api/history`


처럼 기능별로 Endpoint를 나눌 수 있다.


즉:


API = 전체 주문 시스템

Endpoint = 그 안의 특정 업무 창구


라고 생각하면 쉽다.


## 7. HTTP, GET, POST


Browser와 Server가 통신할 때 주로 사용하는 규칙을 HTTP라고 한다.


HTTP = HyperText Transfer Protocol


쉽게 말하면:


Browser와 Server가 서로 요청과 응답을 주고받을 때 사용하는 약속


이다.


그중 자주 사용하는 방식이 GET과 POST다.


### GET


주로 Server에 있는 정보를 가져올 때 사용한다.


예:


"이 페이지 보여 주세요."

"이 상품 정보 주세요."


의 느낌이다.


### POST


Server에 데이터를 보내서 새로운 처리나 작업을 요청할 때 많이 사용한다.


이번 프로젝트의 AI Food Guide는 사용자 입력값을 Backend로 보내고 AI 처리를 요청하기 때문에 POST를 사용한다.


Body Signal

식생활 습관

알레르기 관련 정보

피하고 싶은 음식

↓

### POST

↓

`/api/recommend`


쉽게 기억하면:


GET  = 가져오기

POST = 보내서 처리 요청하기


정도로 이해하면 된다.


## 8. fetch()


`fetch()는 JavaScript에서 Server로 HTTP 요청을 보내고 응답을 받을 수 있게 해주는 기능이다.`


이번 프로젝트에서는 JavaScript가:


`fetch("/api/recommend")`


형태로 Backend에 요청한다.


흐름은 다음과 같다.


사용자가 Form 입력

↓

JavaScript가 입력값 확인

↓

`fetch()`

↓

POST /api/recommend

↓

Python Backend

↓

AI API

↓

응답 반환

↓

### JavaScript

↓

결과 화면 표시


즉:


`fetch()는 Frontend와 Backend를 연결하는 전달 수단이다.`


전화에 비유하면:


Frontend = 전화를 거는 사람

`fetch()   = 전화 연결`

Backend   = 전화를 받는 곳


이라고 생각할 수도 있다.


## 9. Request와 Response


웹 통신은 크게 Request와 Response의 반복이라고 볼 수 있다.


### Request


Request = 요청


Client가 Server에게:


“이 작업을 해 주세요.”


라고 보내는 것이다.


이번 프로젝트에서는 사용자 입력값이 Request에 포함된다.


{

"body_signals": ["식사가 불규칙함"],

"fruit_vegetable_intake": "충분함"

}

### Response


Response = 응답


Server가 요청을 처리한 후 결과를 돌려주는 것이다.


예:


{

"success": true,

"data": {

"recommended_color": "Green",

"representative_food": "키위"

}

}


따라서 전체 흐름은:


### Client

↓

### Request

↓

### Server

↓

처리

↓

### Response

↓

### Client


이다.


## 10. JSON


JSON = JavaScript Object Notation


프로그램끼리 데이터를 주고받을 때 많이 사용하는 데이터 형식이다.


쉽게 말하면 프로그램이 읽기 좋은 정리된 표준 양식이다.


예:


{

"recommended_color": "Green",

"representative_food": "키위"

}


사람이 봐도:


추천 Color = Green

대표 식품 = 키위


라는 의미를 이해할 수 있고, 프로그램도 각 항목을 쉽게 찾아 사용할 수 있다.


AI에게 자유롭게 글을 쓰게 하면 응답 구조가 매번 달라질 수 있다.


그래서 이번 프로젝트에서는 정해진 JSON 구조로 응답을 받도록 했다.


## 11. Schema


Schema = 데이터가 어떤 구조와 규칙을 가져야 하는지 정한 설계도


건물을 지을 때 설계도가 있는 것처럼 데이터에도 설계도가 있다고 생각하면 된다.


예를 들어 AI에게 다음 항목이 반드시 있어야 한다고 정한다.


recommended_color

representative_food

reason

nutrition

alternative_foods

food_guide

caution

health_notice


그러면 Backend는 AI가 반환한 결과를 보고:


recommended_color가 있는가?

representative_food가 있는가?

nutrition은 Array인가?

필수 항목이 비어 있지는 않은가?


를 확인할 수 있다.


따라서 Schema를 사용하는 이유는:


AI의 자유로운 결과를 서비스가 처리할 수 있는 일정한 형태로 제한하기 위해서


이다.


## 12. Validation


Validation = 값이 정해진 조건에 맞는지 확인하는 것


쉽게 말하면 검사 과정이다.


이번 프로젝트에서는 Frontend와 Backend에서 두 번 검사한다.


### Frontend Validation


사용자가 보는 Browser에서 먼저 검사한다.


예:


Body Signal 선택 안 함

↓

Frontend에서 바로 발견

↓

안내 메시지 표시

↓

Backend 요청 안 함


장점은 사용자가 빠르게 오류를 알 수 있고 불필요한 API 호출도 줄일 수 있다는 것이다.


### Backend Validation


Frontend를 통과한 값도 Backend에서 다시 검사한다.


왜 굳이 두 번 할까?


Frontend는 사용자의 Browser에 있기 때문에 개발자 도구 등을 이용하면 검사를 우회할 수 있기 때문이다.


따라서:


### Frontend Validation

= 사용자가 실수했을 때 빠르게 안내


### Backend Validation

= 잘못되거나 예상하지 못한 요청으로부터 시스템 보호


라고 구분하면 된다.


쉽게 비유하면:


### Frontend Validation

= 건물 입구 안내 직원


### Backend Validation

= 내부 보안 검색대


이다.


## 13. Loading / Success / Error


AI 기능은 버튼을 누르는 즉시 결과가 나오는 것이 아니다.


따라서 사용자에게 현재 어떤 상태인지 보여주는 것이 중요하다.


대표적으로:


Idle

Loading

Success

Error


상태가 있다.


흐름을 보면:


사용자 입력

↓

실행 Button Click

↓

Loading

↓

API 요청

↓

┌─────────┴─────────┐

↓                   ↓

Success              Error

↓                   ↓

결과 표시          오류 안내


이번 프로젝트에서는 Loading 중:


식생활 안내서를 만들고 있습니다.


라는 메시지를 보여준다.


사용자는 이 문구를 보고 프로그램이 멈춘 것이 아니라 현재 AI 응답을 기다리는 중임을 알 수 있다.


## 14. Timeout과 AbortController

### Timeout


Timeout = 너무 오래 기다렸을 때 더 이상 기다리지 않도록 정한 시간 제한


이번 프로젝트에서는 15초를 사용한다.


AI 요청

↓

15초 안에 응답

→ 정상 처리


15초 초과

→ Timeout 처리


왜 필요한가?


AI API나 Network에 문제가 생겼는데 끝없이 기다리게 하면 사용자는 서비스가 고장 난 것으로 생각할 수 있기 때문이다.


### AbortController


AbortController는 JavaScript에서 진행 중인 요청을 실제로 중단하는 데 사용할 수 있는 기능이다.


둘의 차이를 쉽게 구분하면:


### Timeout

= 15초까지만 기다리겠다는 규칙


### AbortController

= 15초가 지났을 때 실제 요청을 멈추는 도구


이다.


비유하면:


### Timeout

= "15분까지만 기다리겠습니다."


### AbortController

= 15분이 지나 실제 주문을 취소하는 행동


이라고 이해할 수 있다.


## 15. Local 환경과 Deployment 환경


이 부분은 웹 개발에서 매우 중요하다.


### Local 환경


Local은 개발자가 자기 컴퓨터에서 프로그램을 만들고 시험하는 작업 공간이다.


예:


`http://localhost:8000`


은 자신의 컴퓨터 안에서 실행되고 있는 서버에 접속하는 주소다.


쉽게 요리에 비유하면:


Local = 집 주방에서 새로운 메뉴를 시험하는 상태


이다.


특징:


내 PC에서 실행

내가 주로 접근

.env 등 Local 설정 사용

코드를 수정한 뒤 바로 시험하기 쉬움

### Deployment 환경


Deployment는 만든 서비스를 실제 인터넷에서 다른 사람이 사용할 수 있게 올리는 것이다.


이번 프로젝트에서는 Vercel을 사용한다.


요리에 비유하면:


Deployment = 연습한 메뉴를 실제 식당에서 손님에게 판매하는 단계


이다.


특징:


Vercel의 실행 환경에서 동작

URL을 통해 다른 사람이 접속 가능

Vercel Environment Variables 사용

GitHub에 올라간 코드가 배포됨

실제 인터넷 환경에서 다시 검증 필요


가장 중요한 문장은:


같은 코드라도 실행되는 장소가 달라지면 환경도 달라질 수 있다.


이다.


## 16. Local에서는 되는데 Vercel에서는 안 될 수 있는 이유


Local에서 정상 실행됐다고 해서 Production에서도 반드시 정상 실행되는 것은 아니다.


예를 들어 Local에서는:


내 PC에 Python 설치됨

필요한 Package 설치됨

.env에 API Key 있음

Local 파일 경로 정상


일 수 있다.


하지만 Vercel에서는 별도의 환경을 사용한다.


Vercel Server

Environment Variable 별도 등록 필요

requirements.txt 기반 Package 설치

Vercel Routing 사용

Linux 기반 실행환경 차이 가능


따라서:


Local 성공 = Deployment 성공 보장


은 아니다.


실제 배포 후에는 다시:


- Navigation
Responsive

Frontend

Backend

AI API

환경변수


가 모두 정상인지 확인해야 한다.


## 17. Serverless


Serverless = Server + less


처음 보면 “서버가 없다”는 뜻처럼 보일 수 있지만 실제로 서버 자체가 사라진다는 의미는 아니다.


중요한 것은:


개발자가 Server를 직접 설치하고 유지·관리해야 하는 부담이 줄어든다.


는 의미다.


기존 Server 운영은 자동차를 직접 소유하는 것과 비슷하다.


자동차 구매

보험

주차

정비

연료 관리


를 직접 해야 한다.


Serverless는 필요할 때 택시를 부르는 것에 비유할 수 있다.


필요한 순간 호출

↓

사용

↓

이용이 끝남


개발자는 실제 물리 Server나 운영체제를 직접 관리하지 않아도 Platform이 필요한 실행 환경을 제공한다.


따라서:


Serverless = 서버가 없는 것이 아니라, 서버 운영의 많은 부분을 Cloud Platform이 대신 관리하는 방식


이라고 이해하면 된다.


## 18. 이번 프로젝트에서 Serverless가 동작하는 흐름


이번 프로젝트에서는 다음 흐름으로 이해하면 된다.


사용자

↓

`fetch("/api/recommend")`

↓

### Vercel

↓

Python api/recommend.py 실행

↓

AI_API_KEY 환경변수 사용

↓

OpenAI API 호출

↓

JSON 결과 받음

↓

Frontend에 Response 반환


즉 사용자가 AI Food Guide를 실행할 때 필요한 Backend Function이 동작한다.


사용자는 Server를 직접 관리할 필요가 없다.


## 19. Environment Variable


Environment Variable = 실행 환경에 따로 저장해 두는 설정값


Source Code와 중요한 설정값을 분리하기 위해 사용한다.


이번 프로젝트에서는:


`AI_API_KEY`


를 Environment Variable로 관리한다.


Python에서는:


`os.getenv("AI_API_KEY")`


처럼 값을 가져온다.


이를 사용하는 중요한 이유는:


Code

≠

비밀정보


로 분리하기 위해서다.


특히 API Key를 Source Code에 직접 작성하면 GitHub에 함께 올라갈 위험이 있다.


## 20. API Key 보안


API Key는 API 제공 서비스에 자신을 인증하는 비밀정보다.


쉽게 비유하면:


API 서비스를 이용하기 위한 비밀번호 또는 출입카드


와 비슷하다.


따라서 실제 API Key는:


Source Code

README

Screenshot

### GitHub

Frontend


에 노출하지 않아야 한다.


Frontend에서 API Key를 직접 사용하지 않는 이유도 여기에 있다.


Browser

↓

누구나 개발자 도구로 확인 가능


하기 때문이다.


그래서:


Browser

↓

Backend

↓

Environment Variable

↓

AI API


구조를 사용한다.


## 21. .env와 Vercel Environment Variables의 차이


둘은 같은 목적의 값을 저장하지만 사용하는 장소가 다르다.


### Local


내 컴퓨터에서는:


`.env`


를 사용할 수 있다.


예:


`AI_API_KEY=실제키`

### Vercel


실제 배포 환경에서는 Vercel Dashboard의:


Environment Variables


에 별도로 등록한다.


즉:


Local .env

≠

Vercel Environment Variables


이다.


같은 이름을 사용하더라도 서로 자동으로 공유되는 것이 아니다.


그래서 Local에서는 AI가 되는데 Vercel에서는 환경변수를 등록하지 않아 AI 호출이 실패할 수도 있다.


## 22. .gitignore


.gitignore는 Git에게:


“이 파일은 Git으로 관리하거나 GitHub에 올리지 마.”


라고 알려주는 파일이다.


예:


`.env`

`.venv/`

`.vercel/`

`__pycache__/`


특히:


`.env`


를 제외하는 것은 API Key 보호와 직접 관련된다.


단, 중요한 점이 있다.


API Key가 한 번 Git Commit에 포함되었다면 나중에 .gitignore를 추가한다고 과거 기록까지 자동으로 사라지는 것은 아니다.


따라서 Key 유출이 의심되면:


기존 Key 폐기

↓

새 Key 발급

↓

환경변수 변경

↓

필요하면 Git History 확인·정리


가 필요하다.


## 23. Git과 GitHub


둘은 같은 것이 아니다.


### Git


Git = Version Control System


파일의 변경 이력을 관리하는 기술이다.


쉽게 말하면:


프로젝트의 시간 기록 장치


와 비슷하다.


언제 어떤 변경을 했는지 기록할 수 있다.


### GitHub


GitHub는 Git Repository를 인터넷에서 저장하고 공유할 수 있게 해주는 서비스다.


간단히:


### Git

= 변경 이력을 관리하는 기술


### GitHub

= Git으로 관리되는 프로젝트를 온라인에 보관하는 서비스


라고 기억하면 된다.


## 24. Repository / Commit / Push

### Repository


프로젝트 전체를 관리하는 저장소다.


### HTML

### CSS

### JavaScript

Python

README

설정 파일


등이 함께 들어 있다.


### Commit


특정 시점의 변경 내용을 기록하는 것이다.


비유하면:


게임의 Save Point


와 비슷하다.


현재 프로젝트 상태를 하나의 기록으로 남긴다.


### Push


Local에 있는 Commit을 GitHub에 보내는 작업이다.


내 PC

↓

Git Commit

↓

`git push`

↓

### GitHub


이다.


## 25. GitHub와 Vercel 연동


GitHub와 Vercel을 연결하면 Local에서 변경한 코드를 GitHub에 Push한 뒤 자동으로 새 Deployment가 진행될 수 있다.


흐름은 다음과 같다.


내 PC에서 코드 수정

↓

`git add`

↓

`git commit`

↓

`git push`

↓

GitHub에 최신 코드 저장

↓

Vercel이 변경 감지

↓

### Build

↓

Deploy

↓

Production URL에 새 Version 반영


이 구조의 장점은 개발자가 매번 Vercel에 파일을 수동으로 올릴 필요가 없다는 것이다.


## 26. CI/CD


GitHub와 Vercel 자동 배포 흐름을 이해할 때 CI/CD라는 용어도 함께 알아두면 좋다.


### CI


Continuous Integration


직역하면:


지속적인 통합


이라는 뜻이다.


여러 변경사항을 계속 합치고 문제가 없는지 확인하는 과정이다.


쉽게 말하면:


코드 변경

↓

GitHub에 반영

↓

새 코드가 기존 프로젝트와 잘 합쳐지는지 확인


하는 과정이라고 보면 된다.


### CD


CD는 상황에 따라:


Continuous Delivery

또는

Continuous Deployment


라고 부른다.


공통적인 핵심은 검증된 변경사항을 실제 서비스에 계속 전달하거나 배포하는 것이다.


이번 프로젝트 흐름을 단순화하면:


Local 개발

↓

Version Control

↓

### GitHub

↓

Vercel Build / Deploy

↓

Live Service


라고 이해하면 된다.


## 27. Build와 Runtime

### Build


프로그램을 실제 실행 가능한 형태로 준비하는 과정이다.


예를 들어 Vercel이 프로젝트를 배포하면서:


프로젝트 설정 읽기

Python 환경 준비

필요 Package 설치

실행 구조 확인


등을 수행한다.


이 단계에서 문제가 발생하면 Build Error다.


### Runtime


Build와 Deployment가 끝난 뒤 실제 사용자가 서비스를 사용하는 동안 프로그램이 실행되는 시점을 Runtime이라고 한다.


예:


사용자가 AI Food Guide 실행

↓

Backend Function 실행

↓

AI API 호출


도 Runtime에서 발생한다.


따라서:


Build Error

= 가게를 열기 전에 준비 과정에서 생긴 문제


Runtime Error

= 가게를 연 뒤 실제 영업 중 생긴 문제


라고 이해하면 쉽다.


## 28. Build Log와 Runtime Log


Log는 프로그램에서 발생한 일을 기록한 정보다.


### Build Log


배포 준비 과정에서 발생한 일을 확인한다.


이번 프로젝트에서 pyproject.toml 설정 문제처럼 Vercel Build가 실패했을 때 확인할 수 있다.


### Runtime Log


배포는 성공했지만 실제 서비스 동작 중 발생한 문제를 확인한다.


예:


API 호출 실패

환경변수 문제

Backend Error


등을 찾을 수 있다.


따라서 오류가 발생했다고 무조건 코드를 먼저 바꾸는 것이 아니라:


배포 자체가 실패했는가?

→ Build Log


배포는 됐는데 실행 중 실패했는가?

→ Runtime Log


를 먼저 구분하는 것이 중요하다.


## 29. Debugging


Debugging = 오류의 원인을 찾아 수정하는 과정


Debugging은 무작정 코드를 여러 번 바꾸는 것이 아니다.


이번 프로젝트에서 사용할 수 있는 기본 흐름은 다음과 같다.


문제가 발생한 위치 확인

↓

Build Log / Runtime Log 확인

↓

오류 메시지 읽기

↓

원인 추정

↓

코드 또는 설정 수정

↓

Local Test

↓

Git Commit / Push

↓

Vercel 재배포

↓

Production에서 다시 확인


즉:


Debugging은 코드를 고치는 행위보다 먼저, 어디가 잘못되었는지 찾는 과정이다.


## 30. Framework와 Library / Package

### Framework


Framework는 프로그램을 만들 때 사용할 기본 구조와 개발 방식을 제공한다.


예:


### FastAPI

React

Vue


건물을 지을 때 사용하는 기본 골조 시스템과 비슷하다.


이번 프로젝트에서는 Frontend에 React/Vue를 사용하지 않고 순수 HTML/CSS/JavaScript를 사용하며, Backend에는 FastAPI를 사용했다.


### Package


Package는 필요한 기능을 가져다 쓸 수 있도록 만들어진 코드 묶음이다.


이번 프로젝트의 requirements.txt에는:


openai

fastapi

uvicorn


이 있다.


역할은 다음과 같다.


openai

= OpenAI API 호출


fastapi

= Backend API 구현


uvicorn

= FastAPI를 Local에서 실행

## 31. FastAPI와 Uvicorn


둘도 자주 헷갈린다.


### FastAPI


Python으로 Backend API를 만드는 Framework다.


예를 들어:


`/api/recommend`


Endpoint를 만들고 Request를 받아 처리하는 구조를 정의한다.


### Uvicorn


FastAPI Application을 실제 Local 환경에서 실행해 주는 Server다.


쉽게 말하면:


### FastAPI

= 식당 운영 규칙과 메뉴를 만드는 것


### Uvicorn

= 실제로 식당 문을 열어 손님 요청을 받게 하는 것


이라고 볼 수 있다.


가장 짧게 기억하면:


FastAPI = Backend 프로그램 구성

Uvicorn = 그 프로그램 실행


이다.


## 32. Responsive Web


Responsive Web은 Desktop, Tablet, Mobile처럼 화면 크기가 달라져도 웹페이지 Layout이 알맞게 바뀌도록 만드는 방식이다.


이번 프로젝트에서는:


Desktop

1920 × 1080


Mobile

390 × 844


환경에서 확인했다.


Desktop에서는 메뉴가 가로로 표시될 수 있지만 Mobile에서는 공간이 좁기 때문에 Hamburger Menu로 바뀐다.


즉 Responsive는 단순히 화면을 축소하는 것이 아니라:


화면 크기에 맞게 배치를 다시 구성하는 것


이다.


## 33. Media Query


Media Query는 CSS에서 화면 크기 같은 조건에 따라 다른 Style을 적용하는 기능이다.


예:


`@media (max-width: 900px) {`

}


는:


화면 폭이 900px 이하일 때 이 안의 CSS를 적용하라.


라는 의미다.


따라서:


Desktop Navigation

↓ 화면이 작아짐

Mobile Hamburger Menu


처럼 Layout을 바꿀 수 있다.


## 34. AI Prompt


Prompt는 AI에게 전달하는 지시문과 조건이다.


일반적인 AI 사용에서는:


키위에 대해 설명해 줘.


처럼 자유롭게 질문할 수 있다.


하지만 웹 서비스에서는 결과 형식이 일정해야 한다.


그래서 Prompt에:


서비스 목적

사용자 입력

사용 가능한 식품 정보

금지할 내용

결과 JSON 구조

주의사항


등을 함께 넣는다.


예:


질병을 진단하지 않는다.

특정 식품이 질병을 치료한다고 표현하지 않는다.

정해진 JSON 구조로 반환한다.

필수 항목을 모두 포함한다.


와 같은 조건을 줄 수 있다.


즉:


Prompt는 AI에게 단순히 질문하는 문장이 아니라, 서비스 안에서 AI가 따라야 하는 업무 지침서 역할도 한다.


## 35. AI의 비결정성


생성형 AI는 같은 입력이라고 해서 항상 완전히 같은 문장을 출력한다고 보장할 수 없다.


이번 프로젝트에서도 같은 입력에 대해:


### Local

→ Green / 키위


Production

→ Yellow / 감귤류


처럼 다른 결과가 나온 사례가 있었다.


이것은 반드시 오류를 의미하지 않는다.


AI는 정해진 계산식만 수행하는 프로그램과 달리 여러 가능한 답변 중 하나를 생성할 수 있기 때문이다.


그래서 AI 서비스에서는:


결과가 지난번과 같은가?


만 확인하기보다는:


JSON 형식인가?

필수 Key가 존재하는가?

자료형이 올바른가?

허용된 값인가?

화면에 정상 출력되는가?


를 확인하는 것이 중요하다.


## 36. Cache


Cache는 이미 만들어 놓은 결과나 데이터를 저장해 두었다가 다시 사용하는 방식이다.


예를 들어:


Yellow 컬러푸드 기본 설명

Whole Food 기본 설명

Whole Grain 기본 설명


처럼 사용자마다 변하지 않는 정보는 매번 AI에게 새로 만들게 하지 않고 저장된 값을 사용할 수 있다.


장점:


응답 속도 향상

AI API 호출 감소

비용 감소


가 있다.


하지만:


사용자 A의 개인화 결과

↓

Cache

↓

사용자 B에게 그대로 보여줌


처럼 사용하면 잘못된 결과가 될 수 있다.


따라서:


정적인 공통 정보

→ Cache 활용 가능


사용자별 개인화 결과

→ 신중하게 사용


해야 한다.


## 37. Streaming


Streaming은 AI의 전체 답변이 완성될 때까지 기다리지 않고, 만들어지는 내용을 조금씩 먼저 사용자에게 보여주는 방식이다.


일반 응답:


AI 생성 중..........

AI 생성 중..........

완료

↓

전체 결과 표시


Streaming:


AI

AI 식생활

AI 식생활 안내를

AI 식생활 안내를 생성하고...


처럼 결과가 생성되는 중에도 일부를 볼 수 있다.


따라서 실제 처리 시간이 완전히 줄어드는 것은 아니더라도 사용자가 느끼는 대기시간을 줄일 수 있다.


## 38. 이번 프로젝트 전체 동작을 가장 쉽게 설명하면


이번 프로젝트는 다음과 같이 이해하면 된다.


## 1. 사용자가 Browser에서 Body Signal과 식생활 정보를 입력한다.


## 2. HTML은 입력 Form과 Button이 어디에 있는지 구성한다.


## 3. CSS는 화면의 Color, 크기, Card, Desktop·Mobile Layout을 만든다.


## 4. JavaScript가 사용자의 입력값을 읽고 먼저 검증한다.


## 5. 문제가 없으면 fetch()를 사용하여 /api/recommend로 POST 요청을 보낸다.


## 6. Vercel에서 Python FastAPI Backend가 요청을 받는다.


## 7. Backend가 입력값을 다시 검증한다.


## 8. Environment Variable에서 AI_API_KEY를 불러온다.


## 9. Backend가 OpenAI API에 요청한다.


## 10. AI가 JSON 형태의 결과를 반환한다.


## 11. Backend가 JSON 구조와 필수 Key를 다시 검증한다.


## 12. 정상적인 결과만 Frontend로 전달한다.


## 13. JavaScript가 결과를 안전하게 화면에 표시한다.


## 14. 응답이 늦거나 Error가 발생하면 Loading, Network Error,

API Error, Timeout 등을 구분하여 안내한다.


## 15. 코드는 Git으로 Version을 관리하고 GitHub에 Push한다.


## 16. GitHub와 연결된 Vercel이 변경사항을 Build하고 Production에 배포한다.


## 17. 실제 Vercel URL에서 Desktop·Mobile·AI 기능을 다시 확인한다.


이를 한 문장으로 줄이면:


사용자의 입력을 Frontend가 받고 JavaScript가 Backend에 전달하면, Python Backend가 보안이 필요한 API Key와 AI API 호출을 처리하고, 검증된 AI 결과를 다시 Frontend에 보내 사용자 화면에 보여주는 웹 서비스이며, GitHub와 Vercel을 이용해 Version 관리와 실제 인터넷 배포까지 수행한 프로젝트다.


## 39. 가장 짧게 외워두면 좋은 핵심 문장


처음부터 모든 용어를 길게 외울 필요는 없다.


아래 정도만 정확히 이해하면 나머지는 연결해서 설명할 수 있다.


### HTML

= 무엇이 있는가


### CSS

= 어떻게 보이는가


### JavaScript

= 무엇이 일어나는가


Frontend

= 사용자가 보고 조작하는 영역


Backend

= 보이지 않는 곳에서 실제 처리를 담당하는 영역


### Client

= 서비스를 요청하는 쪽


### Server

= 요청을 처리하고 결과를 주는 쪽


API

= 프로그램끼리 통신하기 위한 약속


Endpoint

= 특정 API 기능을 요청하는 주소


`fetch()`

= JavaScript에서 Server에 요청을 보내는 기능


### Request

= 요청


### Response

= 응답


JSON

= 프로그램끼리 주고받기 쉬운 데이터 형식


Validation

= 데이터가 올바른지 검사


### Local

= 내 컴퓨터에서 개발·시험하는 환경


Production

= 실제 사용자가 이용하는 운영 환경


Deployment

= 서비스를 인터넷에서 사용할 수 있도록 올리는 것


Serverless

= 서버가 없는 것이 아니라 Server 운영 부담을 Platform에 맡기는 방식


Environment Variable

= Code와 분리해서 관리하는 설정값


API Key

= API 사용을 인증하는 비밀정보


### Git

= 변경 이력 관리


### GitHub

= Git Repository를 온라인에서 보관하는 서비스


### Commit

= 현재 변경사항을 하나의 기록으로 남김


### Push

= Local Commit을 GitHub로 전송


### Vercel

= 실제 웹 서비스를 Build하고 배포하는 Platform


Debugging

= 문제가 발생한 위치와 원인을 찾아 수정하는 과정


이 정도 방향이면 기존 자료보다 훨씬 초보자가 읽기 쉬우면서도, 단순 암기가 아니라 이번 과제에서 실제로 어떻게 사용했는지까지 연결된 설명 자료가 됩니다. 기존 자료에 있던 Request/Response, JSON, Validation, Timeout, Git, Vercel 등의 핵심 항목도 그대로 살리면서 이해 중심으로 확장한 형태입니다.

---

## 핵심 비교표

### HTML / CSS / JavaScript / Backend / AI

| 구분 | 쉬운 비유 | 핵심 역할 | 이번 프로젝트 예시 |
|---|---|---|---|
| HTML | 건물의 구조와 공간 | 무엇이 있는지 구성 | 질문, Button, Form, Result 영역 |
| CSS | 건물의 인테리어 | 어떻게 보일지 결정 | 색상, 크기, 간격, Mobile Layout |
| JavaScript | 전기·작동 장치 | 사용자 행동에 반응 | 입력 검증, `fetch()`, 결과 표시 |
| Backend | 일반 사용자에게 보이지 않는 관리실 | 실제 처리와 보안 | API Key 사용, AI API 호출 |
| AI | 관리실이 요청하는 전문 서비스 | 자연어 기반 결과 생성 | 식생활 안내 결과 생성 |

### Client / Server

| 구분 | 역할 | 이번 프로젝트 |
|---|---|---|
| Client | 요청하는 쪽 | 사용자의 Browser |
| Server | 요청을 처리하고 결과를 돌려주는 쪽 | Vercel에서 실행되는 FastAPI Backend |
| Request | Client가 보내는 요청 | 사용자 입력 JSON |
| Response | Server가 돌려주는 결과 | AI 추천 JSON |

### GET / POST

| 방식 | 쉽게 말하면 | 주로 쓰는 경우 | 이번 프로젝트 |
|---|---|---|---|
| GET | 가져오기 | 조회 | 상태 확인 등에 사용 가능 |
| POST | 보내서 처리 요청하기 | 입력값 전송, 생성·처리 | AI Food Guide 요청 |

### Frontend Validation / Backend Validation

| 구분 | 목적 | 이유 |
|---|---|---|
| Frontend Validation | 사용자에게 빠르게 안내 | 잘못된 입력을 즉시 발견하고 불필요한 요청 방지 |
| Backend Validation | 시스템 보호 | Frontend 검증은 우회될 수 있으므로 Server에서 다시 검사 |

### Local / Production

| 구분 | Local | Production |
|---|---|---|
| 실행 장소 | 내 PC | Vercel |
| 대표 주소 | `localhost:8000` | 실제 Vercel URL |
| 환경변수 | `.env` 등 Local 설정 | Vercel Environment Variables |
| 접근 | 주로 개발자 본인 | 인터넷을 통해 사용자 접근 가능 |
| 목적 | 개발·시험 | 실제 서비스 운영 |

### Build / Runtime

| 구분 | 의미 | 오류 예시 |
|---|---|---|
| Build | 실행 가능한 상태로 준비하는 과정 | Package 설치 실패, 설정 파일 문제 |
| Runtime | 배포 후 실제 실행되는 시점 | API 호출 실패, 환경변수 문제 |

### Git / GitHub / Commit / Push

| 용어 | 의미 |
|---|---|
| Git | 파일 변경 이력을 관리하는 Version Control System |
| GitHub | Git Repository를 온라인에 보관·공유하는 서비스 |
| Repository | 프로젝트 저장소 |
| Commit | 특정 시점의 변경 내용을 기록 |
| Push | Local Commit을 GitHub로 전송 |
| Pull | GitHub의 변경 내용을 Local로 가져옴 |

### Timeout / AbortController

| 용어 | 의미 |
|---|---|
| Timeout | 얼마까지 기다릴지 정한 시간 제한 |
| AbortController | 제한 시간이 지나면 진행 중인 요청을 실제로 중단하는 JavaScript 도구 |

---

## 전체 동작 흐름

```text
사용자 입력
    ↓
HTML Form
    ↓
JavaScript 입력 검증
    ↓
fetch() / POST
    ↓
/api/recommend
    ↓
FastAPI Backend
    ↓
Backend 입력 재검증
    ↓
Environment Variable에서 AI_API_KEY 사용
    ↓
OpenAI API 호출
    ↓
AI JSON 응답
    ↓
Backend Schema 검증
    ↓
Frontend Response
    ↓
JavaScript가 안전하게 화면에 출력
```

## GitHub → Vercel 배포 흐름

```text
내 PC에서 코드 수정
    ↓
git add
    ↓
git commit
    ↓
git push
    ↓
GitHub
    ↓
Vercel이 변경 감지
    ↓
Build
    ↓
Deploy
    ↓
Production URL 반영
```

> **핵심:** Local에서 정상 동작했다고 해서 Production에서도 반드시 같은 것은 아니다. 실행 환경, 환경변수, Package 설치, Routing 등이 달라질 수 있으므로 실제 배포 URL에서 다시 검증해야 한다.

