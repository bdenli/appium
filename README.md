# appium

Steps for creating Appium framework from scratch:
- Java
- set up JAVA_HOME >> see copy_zshrc.sh file
- Node.js
- npm
- Xcode
- Xcode command line tools >>
    terminal command: xcode-select --install
- Apple ID set in Xcode >> Xcode > preferences > Accounts > Add account using +
- carthage >>
    terminal command: brew install carthage
- libimobiledevice >>
    terminal command: brew install libimobiledevice
- ios-deploy >>
    terminal command: brew install ios-deploy
- ios-webkit-debug-proxy >>
    terminal command: brew install ios-webkit-debug-proxy
- Appium Server package >>
    terminal command: sudo npm install -g appium
- Appium doctor >>
    terminal command: npm install -g appium-doctor
- xcuitest >>
    terminal command: appium driver install xcuitest
- appium-python client >>
    terminal command: pip install Appium-Python-Client
- write test case in VS code >> see test.py
