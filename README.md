# toktokhan


이 프로젝트는 Python 3.8.5버전에서 작성되었습니다.

이 저장소는 현재 AWS EC2서버와 데이터베이스는 AWS RDS서버에 배포되어 있습니다.

백엔드 과제만 수행하였습니다.

가상환경 설치

$ pip install -r requirements.txt 

테스트를 위한 엔드포인트 

- http://3.36.114.171/admin/ <br>
관리자 페이지로 아이디와 페스위드는 admin 입니다. 모든 조회, 등록이 가능합니다.

- http://3.36.114.171:8000/rest-auth/signup/ <br>
회원 가입 페이지로 Username, Email, Password1, Password2 입력 시 회원 가입이 가능합니다.

- http://3.36.114.171:8000/rest-auth/login/ <br>
회원 로그인 페이지로 Username, Email, Password 입력 시 로그인이 진행되며 토큰이 발행됩니다.<br>
admin 으로 로그인 시 Email은 admin@gmail.com 입니다.

- http://3.36.114.171:8000/rest-auth/logout/<br>
회원 로그아웃 페이지로 로그아웃 처리됩니다.

- http://3.36.114.171:8000/car/viewset/ <br>
등록된 차량을 조회, 등록할수 있는 페이지입니다. 현재 로그인을 하지 않더라도 조회, 등록 할 수 있게 되어있습니다.<br>
로그인 데코레이터는 적용을 하였으나 토큰과 같이 값을 전달하더라도 조회, 등록이 안되서 구현을 하지 못하였습니다.<br>
현재 차량 등록시 Username, Name, Accident_history, Price는 정상적으로 등록가능 하나, <br>
Image, Company name은 현재 작성은 가능하지만 등록이 되지 않는 현상이 있습니다.<br>

질문. 현재 로그인 유효성인증이 계속 실패하여 토큰을 전달하여도 접근이 불가능합니다. 이 부분에 대해 여러 방법으로 시도해 하였지만 구현하지 못하였습니다. 권한을 다르게 하여 접근해야되는지 아니면 DRF를 정확하게 이해하지 못하여 그런것인지 궁금합니다.<br>
질문. 현재 car view에 ViewSet을 이용하여 구현하였습니다. create로 정보를 같이 저장하는 것을 구현하고 싶어 이용을 하였지만 Foreign Key부분이 저장이 되지 않고 있습니다. 페이지에는 등록이 가능하게 나왔지만 어떻게 진행해야 할지 모르겠습니다. 



- http://3.36.114.171:8000/swagger/ swagger API 명세서<br>
- http://3.36.114.171:8000/redoc/   redoc API 명세서<br>

