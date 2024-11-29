from PyQt5.QtWidgets import QApplication
import sys
from LeetCodeGUI import LeetCodeGUI

def main():
    app = QApplication(sys.argv)
    window = LeetCodeGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 