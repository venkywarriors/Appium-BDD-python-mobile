###  Appium ENV Setup on mac OS
Note: Make sure you have full permissions to the file system

1. Java
java -version
2. Git
git --version
3. ruby
ruby -v
4. brew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
brew -v
5. node
brew install node
6. npm
npm -v
7. appium
npm install -g appium
appium -v
8. wd
npm install -g wd
9. pip & selenium
sudo easy_install pip
pip install -U selenium
10. update "~/.bash_profile"
Add ANDROID_HOME and JAVA_HOM
source .bash_profile
11. Install Appium Python Client
pip install appium-python-client
12. appium-doctor
npm install -g appium-doctor
appium-doctor (Check appium environment)
13. BDD
(sudo su)
pip install behave
Note:
Fix the error while install behave
(sudo su)
pip install --ignore-installed six
14. pyenv
(brew update)
brew install pyenv
15. ALLURE - demonstrate the report on a nice GUI
brew install allure
(sudo su)
pip install allure-behav
16. For SauceLabs remote connection
pip install sauceclient

90.Others (install all dependencies)
pip install -r requirements.txt

### Python Code Guide

https://www.python.org/dev/peps/pep-0008/#package-and-module-names
- packages (directories) should have short, all-lowercase names, preferably without underscores;
- modules (filenames) should have short, all-lowercase names, and they can contain underscores;
- classes should use the CapWords convention.


### Write Automation Script
1. UIautomatorviewer - a GUI tool to scan and analyze the UI components of an android application
   Moreinfo: https://www.guru99.com/uiautomatorviewer-tutorial.html

2. behave
   https://github.com/behave/behave


### Debug
behave ./features/ --no-capture -f plain


###  Cloud test farm
1. amazon (first 1000 minutes free)
https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-appium-python.html
2. firebase
3. sourceslabs (15days trial)
