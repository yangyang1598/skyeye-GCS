import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtQuick import QQuickView
from PySide6.QtQml import qmlRegisterType
from PySide6.QtQuickWidgets import QQuickWidget
# from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
import os
import folium
from folium import plugins
import tempfile
from dialog.login_dialog import LoginDialog
from dialog.mission_device_list_dialog import MissionDeviceListDialog

import requests

class MainMap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("스마트 지도")
        self.setGeometry(100, 100, 1200, 800)
        
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 웹뷰 생성 (오프라인 지도용)
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        # QML 위젯 생성 (온라인 지도용)
        self.qml_widget = QQuickWidget()
        layout.addWidget(self.qml_widget)
        
        # 초기에는 QML 위젯 숨김
        self.qml_widget.setVisible(False)
        
        # 네트워크 상태 확인 후 적절한 지도 로드
        self.check_network_and_load_map()
        
        # 주기적으로 네트워크 상태 확인 (30초마다), 불필요 시 삭제
        self.network_timer = QTimer()
        self.network_timer.timeout.connect(self.check_network_and_load_map)
        self.network_timer.start(3000)  # 30초
        
        # 지도 로드 후 로그인 다이얼로그 표시
        QTimer.singleShot(1000, self.show_login_dialog)
        
        # 로그인 성공 후 임무장비 다이얼로그 테스트 (선택사항)
        # self.show_mission_device_dialog()
    
    def is_online(self):
        """네트워크 연결 상태 확인"""
        try:
            # Google에 간단한 요청을 보내서 연결 상태 확인
            response = requests.get('https://www.google.com', timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def check_network_and_load_map(self):
        """네트워크 상태에 따라 적절한 지도 로드"""
        if self.is_online():
            # 온라인 상태에서 qml_widget이 이미 활성화되어 있는지 확인
            if not self.qml_widget.isVisible():
                self.load_online_map()
            else:
                pass
        else:
            # 오프라인 상태에서 web_view가 이미 활성화되어 있는지 확인
            if not self.web_view.isVisible():
                print("오프라인 상태: OpenStreetMap 로드")
                self.load_offline_openstreetmap()
            else:
                pass
    
    def load_offline_openstreetmap(self):
        """오프라인용 OpenStreetMap 생성 및 로드"""
        try:
            # QML 위젯 숨기고 웹뷰 표시
            self.qml_widget.setVisible(False)
            self.web_view.setVisible(True)
            
            # OpenStreetMap 기반 오프라인 지도 생성
            m = folium.Map(
                location=[37.5665, 126.9780],  # 서울 중심
                zoom_start=13,
                tiles='OpenStreetMap'
            )
            
            # 기본 마커 추가
            folium.Marker(
                [37.5665, 126.9780],
                popup='서울시청',
                tooltip='현재 위치'
            ).add_to(m)
            
            # 임시 HTML 파일로 저장
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8')
            m.save(temp_file.name)
            temp_file.close()
            
            # 웹뷰에서 로드
            self.web_view.load(QUrl.fromLocalFile(temp_file.name))
            
        except Exception as e:
            print(f"OpenStreetMap 로드 실패: {e}")
            self.show_error_message()
    
    def load_online_map(self):
        """Qt Location을 사용한 온라인 지도 로드"""
        try:
            # 웹뷰 숨기고 QML 위젯 표시
            self.web_view.setVisible(False)
            
            # QML 파일 경로 설정
            qml_file = os.path.join(os.path.dirname(__file__), 'map.qml')
            
            if os.path.exists(qml_file):
                self.qml_widget.setSource(QUrl.fromLocalFile(qml_file))
                self.qml_widget.setResizeMode(QQuickWidget.SizeRootObjectToView)
                self.qml_widget.setVisible(True)
                
                
            else:
                print(f"QML 파일을 찾을 수 없습니다: {qml_file}")
                self.load_offline_openstreetmap()
                
        except Exception as e:
            print(f"Qt Location 지도 로드 오류: {e}")
            # 오류 발생 시 오프라인 지도로 대체
            self.load_offline_openstreetmap()
    
    def show_error_message(self):
        """오프라인 지도 구성 오류 메시지 표시"""
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("지도 오류")
        msg_box.setText("오프라인 기본 맵 구성 오류가 발생했습니다")
        msg_box.setInformativeText("네트워크 연결을 확인하거나 애플리케이션을 다시 시작해주세요.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
    
    def show_login_dialog(self):
        """지도 로드 후 로그인 다이얼로그 표시"""
        while True:
            login_dialog = LoginDialog(self)
            result = login_dialog.exec()
            
            if result == QDialog.Accepted and login_dialog.login_successful:
                
                # 로그인 성공 후 임무장비 목록 다이얼로그 표시
                self.show_mission_device_dialog(login_dialog.site_data)
                break
            elif result == QDialog.Rejected:
                QMessageBox.information(self, "로그인 취소", "로그인이 취소되었습니다.")
                break
            # 로그인 실패 시 다이얼로그를 다시 표시 (while 루프 계속)
    
    def show_mission_device_dialog(self, site_data=None):
        """임무장비 목록 다이얼로그 표시"""
        device_dialog = MissionDeviceListDialog(self, site_data)
        result = device_dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:
            selected_device = device_dialog.get_selected_device()
            if selected_device:
                print(f"선택된 장비: {selected_device}")
            else:
                print("선택된 장비가 없습니다.")
        else:
            print("임무장비 선택이 취소되었습니다.")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 기본적으로 스마트 지도 위젯 사용 (온라인/오프라인 자동 전환)
    window = MainMap()
    
    window.show()
    sys.exit(app.exec())