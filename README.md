# adb-capture


## Use
### Install files...

#### Windows
파이썬을 3.8.10을 설치해 준다.
pyenv-win으로 설치하면 조금 쉽다.

### pyenv 설치하기

* choco : `choco install pyenv-win`

### 3.8.10 파이썬을 설치

```
pyenv install 3.8.10
pyenv local 3.8.10
python --version
```

* 윈도우에서 자꾸 스토어가 뜬다면 여기를 확인 해 보자.
  * https://stackoverflow.com/questions/58754860/cmd-opens-window-store-when-i-type-python

> %USERPROFILE%\AppData\Local\Microsoft\WindowsApps

위 폴더에서 `Python.exe`, `Python3.exe` 파일을 지워 줘야 한다.

### 파이썬 가상 환경 만들어 주기

```cmd
> python -m pip install --upgrade pip
> python -m pip install virtualenv
> python -m virtualenv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
```

# ui to py
```
pyuic5.exe -x .\mainUi.ui -o .\mainUi.py
```


#### Linux

```bash
$ sudo apt-get install chromium-chromedriver
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

------



## Make Install file..

### .spec 파일 만들기
```
pyi-makespec [--onefile] main.py
```

```
pyinstaller main.spec
```

또는
### 직접 빌드하기
```
pyinstaller --onefile -F --log-level DEBUG --debug main.py
```


# Update all package
```
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```


## Reference
* [Convert Images to PDF using Python](https://datatofish.com/images-to-pdf-python/)

# Note
- 다른 윈도우 클릭시 클릭이 되지 않는 경우에는 프로그램을 관리자 모드로 실행 해 주면 된다.

# Todo
- [ ] 다중모니터 지원 기능 라이브러리 개선
- [ ] 디스플레이 설정 추가
- [ ] 스와이프 기능 개선
- [x] 이미지가 3장 연속 중복이면 중단 하기