import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_login_dialog import Ui_Dialog
import requests
import json

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.login_successful = False  # 로그인 성공 여부 추적
        self.token = None  # 로그인 토큰 저장
        self.site_data = None  # site API 응답 데이터 저장
        self.server_config = self.load_server_config()  # 서버 설정 로드
        
        # 패스워드 필드를 비밀번호 모드로 설정
        self.ui.line_edit_pw.setEchoMode(self.ui.line_edit_pw.EchoMode.Password)
        
        # 버튼 연결
        self.ui.buttonBox.accepted.connect(self.login)
        self.ui.buttonBox.rejected.connect(self.reject)
        
        # 기본값 설정 (테스트용)
        self.ui.line_edit_id.setText("jhyang")
    
    def load_server_config(self):
        """setting.json에서 서버 설정 로드"""
        try:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'setting.json')
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return {
                    'server_url': config.get('server_url', 'localhost'),
                    'port': config.get('port', '8000')
                }
        except Exception as e:
            print(f"설정 파일 로드 실패: {e}")
            # 기본값 반환
            return {
                'server_url': 'skysys.iptime.org',
                'port': '8000'
            }
    
    def get_api_base_url(self):
        """API 기본 URL 생성"""
        return f"http://{self.server_config['server_url']}:{self.server_config['port']}"
    
    def login(self):
        """로그인 처리"""
        user_id = self.ui.line_edit_id.text().strip()
        password = self.ui.line_edit_pw.text().strip()
        
        # 입력값 검증
        if not user_id or not password:
            QMessageBox.warning(self, "입력 오류", "아이디와 비밀번호를 모두 입력해주세요.")
            return
        
        # API를 통한 로그인 검증
        if self.authenticate_with_api(user_id, password):
            self.login_successful = True  # 로그인 성공 표시
            # 로그인 성공 후 site API 호출
            self.fetch_site_data()
            QMessageBox.information(self, "로그인 성공", "로그인에 성공했습니다!")
            self.accept()  # 다이얼로그 닫기 (성공)
        else:
            self.login_successful = False  # 로그인 실패 표시
            QMessageBox.warning(self, "로그인 실패", "아이디 또는 비밀번호가 올바르지 않습니다.")
            self.ui.line_edit_pw.clear()  # 비밀번호 필드 초기화
            self.ui.line_edit_id.setFocus()  # 아이디 필드에 포커스
            # 다이얼로그를 닫지 않고 계속 열어둠
    
    def authenticate_with_api(self, user_id, password):
        """API를 통한 로그인 인증"""
        try:
            # API 엔드포인트
            url = f"{self.get_api_base_url()}/login"
            
            # 요청 데이터
            data = {
                "username": user_id,
                "password": password
            }
            
            # POST 요청 전송 
            headers = {
                "Content-Type": "application/json",
                "accept": "application/json"
            }
            
            response = requests.post(
                url,
                json=data,
                headers=headers,
                timeout=10  # 10초 타임아웃
            )
            
            # 응답 상태 코드 확인
            if response.status_code == 200:
                # 응답 내용 확인
                try:
                    result = response.json()
                    print(result,"result")
                    
                    # result가 문자열이고 40자 이상인 경우 토큰으로 처리
                    if isinstance(result, str) and len(result) >= 40:
                        self.token = result
                        print(f"로그인 성공: {user_id} (토큰 저장)")
                        return True
                    
                    # 토큰값이 있으면 로그인 성공으로 판단
                    token_value = result.get("token") or result.get("access_token") or result.get("auth_token")
                    if token_value:
                        self.token = token_value
                        print(f"로그인 성공: {user_id}")
                        return True
                    
                    # 기존 success 필드도 확인 (백업)
                    elif result.get("success", False) or result.get("status") == "success":
                        print(f"로그인 성공: {user_id}")
                        return True
                    else:
                        print(f"로그인 실패: {result.get('message', '인증 실패')}")
                        return False
                except json.JSONDecodeError:
                    # JSON 파싱 실패 시 상태 코드만으로 판단
                    print(f"로그인 성공: {user_id} (응답: {response.text})")
                    return True
            else:
                print(f"로그인 실패: HTTP {response.status_code} - {response.text}")
                return False
                
        except requests.exceptions.ConnectionError:
            print("연결 오류: 서버에 연결할 수 없습니다.")
            QMessageBox.critical(self, "연결 오류", "서버에 연결할 수 없습니다.\n네트워크 연결을 확인해주세요.")
            return False
        except requests.exceptions.Timeout:
            print("타임아웃 오류: 서버 응답 시간이 초과되었습니다.")
            QMessageBox.critical(self, "타임아웃 오류", "서버 응답 시간이 초과되었습니다.\n잠시 후 다시 시도해주세요.")
            return False
        except requests.exceptions.RequestException as e:
            print(f"요청 오류: {str(e)}")
            QMessageBox.critical(self, "요청 오류", f"로그인 요청 중 오류가 발생했습니다:\n{str(e)}")
            return False
        except Exception as e:
            print(f"예상치 못한 오류: {str(e)}")
            QMessageBox.critical(self, "오류", f"예상치 못한 오류가 발생했습니다:\n{str(e)}")
            return False
    
    def fetch_site_data(self):
        """로그인 성공 후 site API 호출"""
        try:
            url = f"{self.get_api_base_url()}/site/"
            
            headers = {
                "Content-Type": "application/json",
                "accept": "application/json"
               
            }
            
            # 토큰이 있으면 Authorization 헤더 추가 (다양한 형식 시도)
            if self.token:
                headers["Authorization"] = f"Token {self.token}"
            
            # GET 요청에 name 파라미터를 쿼리 파라미터로 추가
            params = {
                "name": "site_list"
            }
            
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    self.site_data = response.json()
                    print(f"Site 데이터 로드 성공: {self.site_data}")
                except json.JSONDecodeError:
                    print(f"Site API 응답 파싱 실패: {response.text}")
            else:
                print(f"Site API 호출 실패: HTTP {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("Site API 연결 오류: 서버에 연결할 수 없습니다.")
        except requests.exceptions.Timeout:
            print("Site API 타임아웃: 요청 시간이 초과되었습니다.")
        except Exception as e:
            print(f"Site API 호출 중 오류 발생: {str(e)}")
