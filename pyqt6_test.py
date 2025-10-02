#!/usr/bin/env python3
"""
PyQt6 설치 테스트용 간단한 Hello World 애플리케이션
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 설치 테스트")
        self.setGeometry(100, 100, 300, 200)
        
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # 라벨 추가
        label = QLabel("PyQt6 설치 완료! 🎉")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2e7d32;")
        layout.addWidget(label)
        
        info_label = QLabel("Base64 Converter 개발 준비 완료")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setStyleSheet("font-size: 14px; color: #555;")
        layout.addWidget(info_label)

def main():
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    window.show()
    
    print("PyQt6 테스트 애플리케이션이 실행되었습니다!")
    print("창을 닫으면 프로그램이 종료됩니다.")
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()