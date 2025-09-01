import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_mission_device_list_dialog import Ui_Dialog

class MissionDeviceListDialog(QDialog):
    def __init__(self, parent=None, site_data=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # 다이얼로그 제목 설정
        self.setWindowTitle("임무장비 목록")
        
        # site 데이터 저장
        self.site_data = site_data
        
        # 초기화
        self.setup_connections()
        self.load_device_list()
    
    def setup_connections(self):
        """시그널 연결 설정"""
        # 필요한 시그널 연결을 여기에 추가
        pass
    
    def load_device_list(self):
        """장비 목록 로드"""
        if not self.site_data:
            print("Site 데이터가 없습니다.")
            return
            
        try:
            # 기존 콤보박스 아이템 모두 제거
            self.ui.combo_mission_device_list.clear()
            
            # site_data에서 name 값들을 추출하여 콤보박스에 추가
            if isinstance(self.site_data, list):
                # site_data가 리스트인 경우
                for item in self.site_data:
                    if isinstance(item, dict) and 'name' in item:
                        self.ui.combo_mission_device_list.addItem(item['name'])
                        print(f"콤보박스에 추가: {item['name']}")
            elif isinstance(self.site_data, dict):
                # site_data가 딕셔너리인 경우
                if 'name' in self.site_data:
                    self.ui.combo_mission_device_list.addItem(self.site_data['name'])
                    print(f"콤보박스에 추가: {self.site_data['name']}")
                # 또는 딕셔너리 안에 리스트가 있는 경우
                for key, value in self.site_data.items():
                    if isinstance(value, list):
                        for item in value:
                            if isinstance(item, dict) and 'name' in item:
                                self.ui.combo_mission_device_list.addItem(item['name'])
                                print(f"콤보박스에 추가: {item['name']}")
            
            print(f"총 {self.ui.combo_mission_device_list.count()}개 항목이 콤보박스에 추가되었습니다.")
            
        except Exception as e:
            print(f"장비 목록 로드 중 오류 발생: {str(e)}")
            QMessageBox.warning(self, "오류", f"장비 목록을 로드하는 중 오류가 발생했습니다:\n{str(e)}")
    
    def get_selected_device(self):
        """선택된 장비 정보 반환"""
        current_text = self.ui.combo_mission_device_list.currentText()
        if current_text:
            return current_text
        return None

# 테스트용 메인 함수
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    dialog = MissionDeviceListDialog()
    dialog.show()
    sys.exit(app.exec())