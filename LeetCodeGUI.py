from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLineEdit, QPushButton, QTextEdit, 
                           QLabel, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor
import sys
from LeetCodeCrawler import LeetCodeCrawler

class LeetCodeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.crawler = LeetCodeCrawler()
        self.initUI()
        
    def initUI(self):
        # Window properties
        self.setWindowTitle('LeetCode Problem Downloader')
        self.setMinimumSize(800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create input area
        input_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter problem slug (e.g., two-sum)")
        self.url_input.setMinimumHeight(35)
        
        download_btn = QPushButton("Download")
        download_btn.setMinimumHeight(35)
        download_btn.clicked.connect(self.download_problem)
        
        input_layout.addWidget(self.url_input)
        input_layout.addWidget(download_btn)
        
        # Create preview area
        preview_label = QLabel("Preview:")
        preview_label.setStyleSheet("color: #f8f8f2;")
        self.preview_area = QTextEdit()
        self.preview_area.setReadOnly(True)
        
        # Set Dracula theme style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #282a36;
            }
            QWidget {
                background-color: #282a36;
                color: #f8f8f2;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #6272a4;
                border-radius: 4px;
                font-size: 14px;
                background-color: #44475a;
                color: #f8f8f2;
                selection-background-color: #bd93f9;
            }
            QPushButton {
                background-color: #bd93f9;
                color: #282a36;
                border: none;
                border-radius: 4px;
                padding: 5px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ff79c6;  /* Dracula pink */
            }
            QTextEdit {
                border: 1px solid #6272a4;
                border-radius: 4px;
                padding: 10px;
                font-family: "Consolas", monospace;
                background-color: #44475a;
                color: #f8f8f2;
                selection-background-color: #bd93f9;
            }
            QScrollBar:vertical {
                border: none;
                background: #282a36;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #6272a4;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QMessageBox {
                background-color: #282a36;
                color: #f8f8f2;
            }
            QMessageBox QPushButton {
                min-width: 80px;
                min-height: 24px;
            }
        """)
        
        # Add all components to the main layout
        layout.addLayout(input_layout)
        layout.addWidget(preview_label)
        layout.addWidget(self.preview_area)
        
        # Set layout spacing
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

    def download_problem(self):
        problem_slug = self.url_input.text().strip()
        if not problem_slug:
            QMessageBox.warning(self, "Warning", "Please enter the problem slug!")
            return
            
        markdown_content = self.crawler.get_problem_content(problem_slug)
        if markdown_content:
            # Show preview with basic markdown formatting
            formatted_content = self.format_markdown(markdown_content)
            self.preview_area.setHtml(formatted_content)
            
            # Save file
            with open(f"{problem_slug}.md", 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            QMessageBox.information(self, "Success", f"The problem has been saved to {problem_slug}.md")
        else:
            QMessageBox.critical(self, "Error", "Failed to get the problem!")

    def format_markdown(self, text):
        """Basic markdown to HTML conversion"""
        # Convert code blocks
        lines = text.split('\n')
        in_code_block = False
        formatted_lines = []
        
        for line in lines:
            if line.startswith('```'):
                if in_code_block:
                    line = '</code></pre>'
                    in_code_block = False
                else:
                    line = '<pre><code>'
                    in_code_block = True
            elif in_code_block:
                line = line.replace('<', '&lt;').replace('>', '&gt;')
            else:
                # Basic markdown formatting
                line = line.replace('**', '<b>').replace('**', '</b>')  # Bold
                line = line.replace('*', '<i>').replace('*', '</i>')    # Italic
                line = line.replace('`', '<code>').replace('`', '</code>')  # Inline code
                
            formatted_lines.append(line)
        
        return '<br>'.join(formatted_lines)

