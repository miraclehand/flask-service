
https://github.com/miraclehand

* MongoDB(server:mlab.com)
	- pymongo:v.2.9.0
	-

* MongoDB(v.2.4.14 for 32bit)
	- Access for any where modify this
			  /etc/mongodb.conf
			make a comment "bind_tp=0.0.0.0"
	- $sudo /etc/init.d/mongodb restart
	- for compatibility. It import pymongo v2.6.3

* RESTFull API
	- pip3 install flask-restful

, sqlalchemy
pep and how to lint python code

Http Response Codes
200 성공
400 Bad Request - field validation 실패시
401 Unauthorized - API 인증,인가 실패
404 Not found ? 해당 리소스가 없음
500 Internal Server Error - 서버 에러

Authentication
1. API Key
2. API Token
3. HTTP Basic Auth
4. Digest access Authenication

무상태인증
1. HTTP Basic
	-> 사용자 아이디와 비밀번호를 base64로 인코딩해서 보냄. 패킷 탈취하면 끝
2. OAuth
	-> 도메인 사용자외에 별도의 ClientId와 ClientSecret가 필요하다.
	-> 페이스북 API, 유튜브 API 등 예측할 수 없는 클라이언트가 API를 소비하는 오픈 API 서비스에 적절하다.
	-> 토큰 뿐만아니라, Client* 발급 및 관리, 각 API 엔드포인트에 대한 접근 권한 제어를 포함하는 등, 크고 무겁다.
	-> 즉, 큰 서비스에만 어울린다.
3. JWT
	-> 토큰만 다룬다. 도메인 사용자를 그대로 사용하고, 도메인 사용자와 토큰간의 맵핑 테이블을 이용한다(주로 속도가 빠른 키-값 저장소 이용).
	-> 네트워크 구간에서 변조가 불가능하다. 변조되면 토큰은 무효화된다.
	-> 네트워크 구간에서 탈취 당해도 유효 기간(ttl) 또는 리프레시 가능 기간(refresh_ttl)이 지나면 무효화된다.
	-> 토큰 안에 사용자를 식별하기 위한 정보를 담고 있다. 즉, 토큰만 해독하면 사용자를 식별할 수 있다.
	-> 캡티브 API, 소형 API 서비스에 어울린다.

ref. http://bcho.tistory.com/955?category=252770
ref. https://opentutorials.org/module/3669




curl -v http://182.228.22.202:20080/auth/login 

curl -i -X POST -H "Content-Type: application/json" -d '{"username":"john","password":"hello"}' http://182.228.22.202:20080/api/v1.0/auth/join

curl http://182.228.22.202:20080/api/v1.0/login --user john:hello

curl -X GET http://182.228.22.202:20080/api/v1.0/prod/product
curl -i -X POST -H "Content-Type: application/json" -d '{"supplier_id":"2","supplier_name":"company2", "email":"com2@com2.com"}' http://182.228.22.202:20080/api/v1.0/prod/supplier




flask and react
https://realpython.com/the-ultimate-flask-front-end/


$pigar
$npm install
$bower install
$npm install -g gulp

* git
git status
git add Readme.txt
git commit -m "Add Readme.txt"
git remote -v
git push origin master
