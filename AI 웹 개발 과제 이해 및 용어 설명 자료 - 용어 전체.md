# AI 웹 개발 과제 이해 및 용어 설명 자료 (용어 전체)

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


## 1. 이번 과제는 무엇을 하는 과제인가?


이번 과제의 핵심은 단순히 웹페이지 하나를 만드는 것이 아니다.


사용자가 웹페이지에 정보를 입력하면 JavaScript가 그 값을 처리하고, Python Backend가 AI API를 호출한 뒤, AI가 만든 결과를 다시 웹페이지에 보여주는 하나의 실제 AI 웹 서비스 흐름을 직접 구현하는 것이다.


또한 로컬 컴퓨터에서만 실행되는 프로그램이 아니라 GitHub를 통해 코드를 관리하고 Vercel에 배포하여 다른 사람도 URL을 통해 사용할 수 있도록 만드는 것이 목적이다.


과제에서는 특히 다음 능력을 중요하게 본다.


사용자 입력

↓

Frontend

↓

Backend

↓

AI API

↓

AI 응답

↓

검증

↓

사용자 화면 출력


실제로 과제 원문에서도 Frontend는 HTML/CSS/JavaScript를 사용하고, Backend는 Vercel Serverless Functions의 Python을 사용하며, Frontend에서 fetch("/api/...") 방식으로 Backend를 호출하도록 요구한다.


## 2. Frontend와 Backend

### Frontend란?


Front + End, 즉 사용자의 앞쪽에서 보이는 영역이다.


사용자가 Browser에서 직접 보고 조작하는 부분을 의미한다.


이번 프로젝트에서는 다음이 Frontend다.


index.html

css/style.css

js/main.js


예를 들면:


- Body Signal 선택
- 과일·채소 섭취 정도 입력
- AI Food Guide 실행 버튼
- Loading 표시
- AI 결과 카드
- 오류 메시지
- Hamburger Menu

등이 모두 Frontend에서 보이는 기능이다.


쉽게 비유하면:


Frontend = 손님이 이용하는 식당의 홀


이다.


### Backend란?


Back + End, 즉 사용자의 눈에는 직접 보이지 않는 뒤쪽 처리 영역이다.


이번 프로젝트에서는:


api/recommend.py


가 핵심 Backend다.


Backend에서는 다음 일을 한다.


Frontend에서 요청 받기

→ 입력값 다시 검사하기

→ API Key 가져오기

→ OpenAI API 호출하기

→ AI 응답 검사하기

→ 결과를 Frontend로 반환하기


비유하면:


Backend = 손님에게는 보이지 않는 식당 주방


이다.


사용자는 음식을 주문하지만 주방에서 실제 조리가 어떻게 이루어지는지는 직접 볼 필요가 없다.


## 3. HTML / CSS / JavaScript

### HTML


HTML = HyperText Markup Language


웹페이지의 구조를 만든다.


우리 프로젝트에서 HTML은 다음과 같은 것을 만든다.


- 제목
- 버튼
- 입력 Form
- Navigation
- Section
- 결과 영역
- FAQ

비유하면:


HTML = 건물의 뼈대


이다.


HTML만 있으면 구조는 있지만 예쁘지도 않고 복잡한 동작도 하지 않는다.


### CSS


CSS = Cascading Style Sheets


HTML로 만든 요소의 디자인과 배치를 담당한다.


예:


- 글자 크기
- 색상
- 버튼 모양
- Card
- 여백
- 화면 배치
- Mobile Layout

비유하면:


CSS = 건물의 인테리어 또는 옷


이다.


### JavaScript


JavaScript는 웹페이지에 동작을 만든다.


이번 프로젝트에서는 JavaScript가 다음을 담당한다.


- 사용자 입력값 읽기
- 입력값 검사
- 버튼 클릭 처리
- Backend 호출
- Loading 표시
- Timeout 처리
- AI 결과 표시
- 오류 메시지 표시
- Mobile Menu 동작

비유하면:


JavaScript = 움직이게 하는 신경과 근육


이다.


따라서 가장 간단하게 기억하면:


HTML = 구조

CSS = 디자인

JavaScript = 동작


이다.


## 4. Form


Form은 사용자가 웹페이지에서 값을 입력할 수 있도록 만든 영역이다.


예를 들어:


`<form id="bodySignalForm">`


형태로 사용할 수 있다.


이번 서비스에서는 Form을 통해:


생활 속 이상 신호 등 몸 상태

과일·채소 섭취 정도

평소 식생활

알레르기 관련 정보

피하고 싶은 음식


등을 입력한다.


## 5. API


API = Application Programming Interface


서로 다른 프로그램이 정해진 방법으로 정보를 주고받도록 만든 연결 방법이다.


이번 프로젝트에서는 크게 두 단계의 API 통신이 있다.


Browser

↓

우리 Backend API

↓

OpenAI API


예를 들어 Frontend는 OpenAI에 직접 요청하지 않는다.


대신:


Frontend

↓

`/api/recommend`

↓

Python Backend

↓

OpenAI API


순서로 요청한다.


## 6. Endpoint


Endpoint는 API 요청을 보내는 구체적인 주소다.


이번 프로젝트의 대표 Endpoint는:


`/api/recommend`


이다.


쉽게 말하면 API라는 건물이 있다면:


Endpoint = 그 건물 안의 특정 창구


라고 생각하면 된다.


예를 들어:


`/api/recommend`

`/api/login`

`/api/users`


처럼 기능마다 서로 다른 Endpoint를 만들 수 있다.


## 7. fetch()


`fetch()는 JavaScript에서 서버에 HTTP 요청을 보내는 기능이다.`


이번 프로젝트에서는 JavaScript가:


`fetch("/api/recommend")`


방식으로 Backend에 요청한다.


흐름은:


사용자 입력

↓

### JavaScript

↓

`fetch()`

↓

`/api/recommend`

↓

Python Backend


이다.


과제에서 fetch()를 이해하도록 요구하는 이유도 사용자 입력이 어떻게 Backend로 전달되고 결과가 다시 화면으로 돌아오는지를 설명할 수 있어야 하기 때문이다.


## 8. Request와 Response

### Request


Request = 요청


Frontend가 Backend에:


“이 데이터를 가지고 AI 추천을 만들어 주세요.”


라고 보내는 것이다.


예:


{

"body_signals": ["식사가 불규칙함"],

"fruit_vegetable_intake": "충분함"

}

### Response


Response = 응답


Backend가 처리 결과를 Frontend로 돌려주는 것이다.


예:


{

"success": true,

"data": {

"recommended_color": "Green",

"representative_food": "키위"

}

}


따라서:


Frontend → Request → Backend

Frontend ← Response ← Backend


라고 이해하면 된다.


## 9. JSON


JSON = JavaScript Object Notation


프로그램끼리 데이터를 주고받을 때 많이 사용하는 형식이다.


예:


{

"recommended_color": "Green",

"representative_food": "키위"

}


사람이 읽을 수도 있고 프로그램도 쉽게 처리할 수 있다는 장점이 있다.


이번 프로젝트에서는 AI가 자유로운 문장만 반환하도록 하지 않고 정해진 JSON 구조로 반환하도록 만들어 결과를 검사하기 쉽게 했다.


## 10. Schema


Schema = 데이터의 구조와 규칙


예를 들어 AI가 다음 항목을 반환해야 한다고 정한다.


recommended_color

representative_food

reason

nutrition

alternative_foods

food_guide

caution

health_notice


이것이 일종의 결과 Schema다.


이를 사용하면 AI가 아무 형식으로 응답하는 것이 아니라:


“이 형식에 맞춰 답하세요.”


라고 제한할 수 있다.


## 11. Validation


Validation = 검증


입력값이나 결과값이 우리가 정한 조건에 맞는지 확인하는 과정이다.


이번 프로젝트에는 두 종류가 중요하다.


### Frontend Validation


Browser에서 먼저 검사한다.


예:


Body Signal을 하나도 선택하지 않음

↓

Frontend에서 발견

↓

Backend 요청 자체를 보내지 않음


장점은 사용자에게 빠르게 알려줄 수 있다는 것이다.


### Backend Validation


Backend에서도 다시 확인한다.


왜 두 번 할까?


Frontend 검사는 Browser 개발자 도구나 직접 API 요청 등을 통해 우회할 수 있기 때문이다.


따라서:


Frontend 검증 = 사용자 편의


Backend 검증 = 시스템 보호


라고 기억하면 된다.


## 12. HTTP Status Code


서버가 요청 결과를 숫자로 알려주는 규칙이다.


대표적으로:


200 = 정상 처리

400 = 잘못된 요청

413 = 요청 데이터가 너무 큼

500 = 서버 내부 오류


가 있다.


숫자 첫 자리를 기준으로 보면:


2xx = 성공

4xx = 사용자가 보낸 요청 쪽 문제

5xx = Server 쪽 문제


정도로 이해하면 된다.


## 13. Loading


AI API는 결과가 바로 나오지 않을 수 있다.


사용자가 버튼을 눌렀는데 아무 변화가 없으면 프로그램이 멈춘 것으로 생각할 수 있다.


그래서 이번 서비스는 처리 중:


식생활 안내서를 만들고 있습니다.


라는 Loading 상태를 표시한다.


즉:


버튼 클릭

↓

Loading 시작

↓

API 요청

↓

응답

↓

Loading 종료

↓

결과 표시


이다.


## 14. Timeout


Timeout = 너무 오래 기다리면 요청을 종료하는 기준 시간


이번 프로젝트는:


15초


를 사용한다.


AI가 계속 응답하지 않는다고 Browser를 무한정 기다리게 할 수 없기 때문이다.


## 15. AbortController


JavaScript에서 진행 중인 요청을 중단할 수 있게 하는 기능이다.


이번 프로젝트에서는:


fetch 실행

↓

15초 대기

↓

응답 없음

↓

### AbortController

↓

요청 중단

↓

Timeout 메시지 표시


에 사용한다.


즉:


Timeout은 규칙이고, AbortController는 실제 요청을 중단하는 수단


이라고 이해하면 쉽다.


## 16. Error Handling


Error Handling = 오류가 발생했을 때 처리하는 방법


이번 과제에서는 최소 하나 이상의 실패 상황을 사용자에게 안내하도록 요구한다. 예시로 빈 입력, API 오류, 지연/Timeout이 제시되어 있다.


우리 프로젝트는 더 세분화했다.


빈 입력

API Error

Network Error

### Timeout


그리고 사용자가 보는 메시지와 개발자가 보는 Log를 구분했다.


예:


사용자:


AI 식생활 안내서를 불러오지 못했습니다.

잠시 후 다시 시도해 주세요.


개발자:


500

RuntimeError

...

## 17. Log


Log = 프로그램에서 어떤 일이 발생했는지 기록한 정보


사용자에게 보여주기 위한 것이 아니라 개발자가 문제를 찾기 위한 자료다.


예:


POST /api/recommend 200 OK


또는 오류 내용이 기록될 수 있다.


## 18. Build Log와 Runtime Log

### Build Log


서비스를 배포할 때 문제가 발생했는지 확인한다.


우리 프로젝트에서는 pyproject.toml 문제처럼 배포 준비 과정의 오류를 찾을 때 사용했다.


### Runtime Log


배포 자체는 성공했지만 실제로 프로그램을 실행하는 중 발생한 문제를 확인한다.


쉽게 구분하면:


### Build Log

= 집을 짓는 과정에서 발생한 문제


### Runtime Log

= 완성된 집에서 생활하면서 발생한 문제


이다.


## 19. Debugging


Debugging = 오류의 원인을 찾아 수정하는 과정


무작정 코드를 바꾸는 것이 아니다.


우리 프로젝트에서 사용한 흐름은:


문제가 어디서 발생했는지 확인

↓

Build Log / Runtime Log 확인

↓

원인 파악

↓

코드 또는 설정 수정

↓

Git Commit

↓

### Push

↓

재배포

↓

다시 검증


이다.


## 20. Local 환경


Local = 내 컴퓨터에서 실행하는 환경


예:


`http://localhost:8000`


또는:


`127.0.0.1`


은 내 컴퓨터를 의미한다.


다른 사람이 인터넷에서 이 주소로 우리 서비스를 이용할 수 있는 것은 아니다.


## 21. Production 환경


Production = 실제 사용자에게 제공하는 운영 환경


우리 프로젝트에서는 Vercel에 배포한 URL이 Production 환경이다.


즉:


### Local

= 개발자가 자기 컴퓨터에서 테스트


Production

= 실제 인터넷에 공개된 서비스


이다.


## 22. Deployment


Deployment = 배포


내 컴퓨터에서 만든 프로그램을 실제 인터넷에서 사용할 수 있도록 올리는 과정이다.


이번 과제에서는 Vercel을 사용한다.


과제 역시 GitHub와 Vercel을 연결하고, 배포 URL에서 Navigation·반응형·AI 기능 전체가 실제 동작하는지 확인하도록 요구한다.


## 23. Vercel


Vercel은 웹 서비스를 인터넷에 배포할 수 있도록 해주는 Platform이다.


이번 프로젝트에서는 두 역할을 한다.


Frontend 서비스

+

Python Backend 실행


특히 Python Backend는 Vercel의 Serverless Function 방식으로 실행된다.


## 24. Serverless


Serverless를 그대로 번역하면 “서버가 없다”처럼 보이지만 실제 뜻은 서버가 정말 없는 것이 아니다.


개발자가 직접:


Server 설치

Server 유지관리

항상 실행

OS 관리


등을 하지 않아도 Platform이 필요한 Server 환경을 제공한다는 의미에 가깝다.


그래서:


Serverless = 서버를 직접 운영하지 않고 필요한 Backend 기능을 실행하는 방식


이라고 이해하면 된다.


## 25. Vercel Serverless Functions


Vercel에서 요청이 들어왔을 때 필요한 Backend 코드를 실행하는 기능이다.


이번 프로젝트에서는:


`/api/recommend`


요청이 들어오면 Python 코드가 실행되어 AI API를 호출한다.


과제에서 Backend를 api/ 폴더에 Python으로 구현하도록 한 것도 이 구조 때문이다.


## 26. 환경변수(Environment Variable)


프로그램의 설정값을 Source Code와 분리해서 저장하는 방법이다.


예:


`AI_API_KEY`


API Key를 Python 파일에 직접 적지 않고:


`os.getenv("AI_API_KEY")`


형태로 불러온다.


## 27. API Key


API 서비스를 사용하는 사람 또는 프로그램을 인증하기 위한 비밀값이다.


쉽게 말하면:


API를 사용하는 비밀번호와 비슷한 인증정보


이다.


따라서:


Source Code

README

Screenshot

### GitHub

Frontend


등에 실제 값이 노출되면 안 된다.


과제에서도 API Key는 환경변수로 관리하고 코드·README·Screenshot에 노출하지 않도록 명시한다.


## 28. .env


로컬 컴퓨터에서 환경변수를 관리할 때 많이 사용하는 파일이다.


예:


`AI_API_KEY=실제키`


실제 .env는 GitHub에 올리지 않는다.


## 29. .env.example


다른 사람이 프로젝트를 사용할 때:


“이 프로그램에는 이런 환경변수가 필요합니다.”


라고 알려주기 위한 예시 파일이다.


예:


`AI_API_KEY=your_api_key_here`


실제 비밀값은 들어가지 않는다.


## 30. .gitignore


Git이 추적하지 않아야 하는 파일을 지정한다.


예:


`.env`

`.venv/`

`.vercel/`

`__pycache__/`


특히 .env를 제외하는 이유는 API Key 유출 방지와 관련이 있다.


## 31. Git


Git = 파일의 변경 이력을 관리하는 Version Control System


파일을 단순히 저장하는 것과 다르게:


언제

무엇을

어떻게

변경했는지


기록할 수 있다.


## 32. GitHub


Git으로 관리하는 Repository를 인터넷에서 저장·공유할 수 있는 서비스다.


비유하면:


Git = 변경 이력을 관리하는 기술


GitHub = 그 Git Repository를 온라인에서 보관하고 협업하는 서비스


이다.


## 33. Repository


Repository = 프로젝트 저장소


이번 프로젝트의 HTML, CSS, JavaScript, Python, README 등이 함께 들어 있는 Git 저장 공간이다.


## 34. Commit


특정 시점의 변경 내용을 Git 이력으로 저장하는 것이다.


예:


`git commit -m "Finalize deployment evidence and documentation"`


쉽게 말하면:


프로젝트의 현재 상태에 이름을 붙여 기록하는 것


이다.


## 35. Push


Local Git에 저장된 Commit을 GitHub 같은 원격 Repository에 보내는 작업이다.


내 PC

↓

`git push`

↓

### GitHub

## 36. Pull


반대로 GitHub의 변경 내용을 내 컴퓨터로 가져오는 것이다.


### GitHub

↓

`git pull`

↓

내 PC

## 37. Branch


Git에서 서로 다른 작업 흐름을 분리하기 위한 개념이다.


이번 프로젝트는:


main


Branch를 사용했다.


main은 보통 기본 또는 최종 코드가 관리되는 Branch다.


## 38. Responsive Web


Responsive = 반응형


Desktop, Tablet, Mobile처럼 화면 크기가 달라져도 Layout이 적절하게 변하도록 만드는 방식이다.


과제에서도 최소 두 가지 화면 크기에서 직접 확인하도록 요구한다.


이번 프로젝트에서는:


Desktop

1920 × 1080


Mobile

390 × 844


환경을 확인했다.


## 39. Media Query


CSS에서 화면 크기에 따라 다른 Style을 적용하는 기능이다.


예:


`@media (max-width: 900px) {`

}


의미는:


화면 폭이 900px 이하일 때 이 CSS를 적용한다.


이다.


이를 통해 Desktop Navigation을 Mobile에서 Hamburger Menu로 바꿀 수 있다.


## 40. Hamburger Menu


Mobile 화면에서 흔히 사용하는:


☰


형태의 Navigation Menu다.


화면이 작기 때문에 모든 Menu를 한 줄에 보여주지 않고 버튼 안에 숨겨두는 방식이다.


## 41. requirements.txt


Python 프로젝트에서 필요한 Package 목록을 기록하는 파일이다.


우리 프로젝트는:


openai

fastapi

uvicorn


을 사용한다.


다른 컴퓨터에서:


`pip install -r requirements.txt`


를 실행하면 필요한 Package를 설치할 수 있다.


## 42. Package


다른 개발자가 만들어 놓은 기능 묶음이다.


예:


openai

= OpenAI API 사용


fastapi

= Backend API 구현


uvicorn

= FastAPI를 로컬에서 실행

## 43. FastAPI


Python으로 Web API를 만들기 위한 Framework다.


이번 프로젝트에서는:


`/api/recommend`


Endpoint를 만드는 데 사용한다.


## 44. Uvicorn


FastAPI Application을 로컬 컴퓨터에서 실행해 주는 Web Server다.


예:


`python -m uvicorn api.recommend:app --host 127.0.0.1 --port 8000`


따라서 역할을 구분하면:


FastAPI = Backend 프로그램을 만드는 도구


Uvicorn = 그 프로그램을 실제 실행시키는 Server


이다.


## 45. Framework


프로그램을 만들 때 기본 구조와 규칙을 제공하는 도구다.


예:


### FastAPI

React

Vue


가 Framework에 해당한다.


이번 과제에서는 Frontend에 React/Vue 등을 사용하지 않고 순수 HTML/CSS/JavaScript를 사용하도록 제한하고 있다.


## 46. Prompt


AI에게 전달하는 지시문이다.


단순히:


음식 추천해 줘.


라고 할 수도 있지만 실제 서비스에서는 훨씬 구체적으로 지시한다.


예:


이 서비스는 의료 진단을 하지 않는다.

정해진 컬러푸드 정보를 사용한다.

JSON 형식으로 반환한다.

필수 항목을 모두 포함한다.


Prompt가 명확할수록 서비스에서 필요한 결과 구조를 얻기 쉽다.


## 47. AI의 비결정성


생성형 AI는 같은 입력을 넣어도 항상 완전히 같은 답을 생성한다고 보장할 수 없다.


우리 테스트에서도 같은 입력에:


### Local

→ Green / 키위


Production

→ Yellow / 감귤류


처럼 결과가 달라진 사례가 있었다.


이것은 반드시 Error라는 뜻은 아니다.


그래서 AI 서비스에서는 단순히 결과 문장이 같은지를 확인하기보다:


정상적인 JSON인가?

필수 Key가 있는가?

허용된 형식인가?

화면에 정상적으로 출력되는가?


를 검사하는 것이 중요하다.


## 48. Cache


한 번 얻은 데이터를 저장해두고 다시 사용하는 방법이다.


예를 들어 사용자마다 달라지지 않는 컬러푸드 기본 정보는 매번 AI에게 생성시키는 대신 저장된 정보를 이용할 수 있다.


장점:


속도 향상

API 호출 감소

비용 감소


그러나 개인화된 AI 결과를 무조건 Cache하면 다른 사용자에게 잘못된 결과를 보여줄 수 있으므로 구분해야 한다.


## 49. Streaming


AI 답변 전체가 완성될 때까지 기다리지 않고 생성되는 내용 일부를 먼저 사용자에게 보여주는 방식이다.


예:


일반 응답

████████████ 완료

→ 한 번에 출력


Streaming

██

████

██████

████████

→ 생성되는 동안 순차적으로 출력


긴 AI 답변에서는 사용자가 느끼는 대기시간을 줄일 수 있다.


## 50. 이번 프로젝트의 전체 구조를 한 문장으로 설명하면


다음 문장을 기억하면 좋습니다.


사용자가 HTML 기반 Form에서 생활 속 이상 신호 등 몸 상태와 식생활 정보를 입력하면 JavaScript가 입력값을 검증하고 fetch()로 FastAPI Backend의 /api/recommend Endpoint에 전달한다. Backend는 입력값을 다시 검증한 뒤 환경변수로 관리되는 API Key를 이용하여 OpenAI API를 호출하고, AI의 JSON 응답을 검증한 후 Frontend로 반환한다. Frontend는 검증된 결과를 안전하게 화면에 출력하며 Loading, Error, Network Error, 15초 Timeout 상황도 별도로 처리한다. 완성된 서비스는 GitHub에서 Version을 관리하고 Vercel에 배포하였다.


이 문장을 이해하고 자기 말로 풀어서 설명할 수 있다면 이번 과제의 기술적 핵심을 거의 모두 이해한 것입니다.


추가로 설명 자료에 넣을 가치가 있는 부분


17/17 평가의 “보완”은 이제 제출물을 다시 수정해야 한다는 의미로 볼 필요는 없습니다. 모두 PASS이기 때문입니다. 다만 학습 자료에는 다음 네 가지 정도는 넣어두는 것이 좋습니다.


첫째, HTTP의 GET과 POST 차이입니다. 이번 서비스의 AI 요청은 데이터를 서버로 보내 처리하므로 POST를 사용한다는 점을 알아두면 fetch() 설명이 훨씬 완성됩니다.


둘째, Client와 Server의 차이입니다. Browser가 Client이고 FastAPI가 Server 역할을 한다는 것을 이해하면 Frontend/Backend/API 관계가 한 번에 정리됩니다.


셋째, 보안과 Git 이력의 관계입니다. API Key를 GitHub에 Push한 뒤 현재 파일에서만 삭제해도 과거 Commit에 남을 수 있다는 점은 이번 과제에서 중요한 실무 개념입니다. 과제 원문 역시 Key 유출이 의심되면 폐기·재발급하고 노출된 Commit 이력도 정리할 수 있어야 한다고 명시합니다.


넷째, AI Coding Tool을 사용하는 목적입니다. 과제는 AI가 만들어 준 코드를 그대로 제출하는 것이 목표가 아니라, AI가 만든 코드에서 문제가 발생했을 때 어디서 문제가 생겼고 어떻게 고쳤는지를 설명할 수 있는 것을 학습 목표로 삼고 있습니다.


따라서 다음에는 이 자료를 더 실용적으로 ① 용어사전형, ② 전체 동작 흐름형, ③ 예상 질문·답변형, ④ 이번 프로젝트 실제 사례형으로 나눠 만들면 좋습니다. 특히 동료평가나 설명을 대비한다면 “이게 뭐예요?” → “왜 썼어요?” → “우리 프로젝트에서는 어디에 썼어요?”의 3단 구조가 가장 이해하기 쉽습니다.

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

