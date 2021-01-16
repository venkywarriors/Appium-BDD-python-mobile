### Appium-BDD-python-mobile-app-testing

#### This is a smoke test for an Android mobile App

Write your own script

1. Write feature file : /features/yourown.feature 
2. Implement the step files: /features/steps/steps.py
3. Define page object and action in page files: /pages/android/newpage.py
4. If you have some common action on all pages, then add them in: /utils/base_page.py
5. The report and screenshot are generated: /reports/report/ 
Allure test report (http://allure.qatools.ru/)

Tips:
1. How to write feature file:
   Try to use consise words or phrase, avoid use UX words like button or string or text, because that might be changed frequently.
   Gherkin standard: https://cucumber.io/docs/reference,
2. How to implement step function:
   In step function, we implement the specific operation on the page.
   Try to reuse existing steps if they are applicable to your new case.
 
#### What does the report look like

Final Report:
![Report-dashboard](https://github.com/julialiuliu/Appium-BDD-python-mobile-app-testing/blob/master/doki/img/dashboard2.png)

#### TODO
1. Integrate to cloud test farm (ex:Amazon test farm or Sourcelabs)
2. Send out output report to emailbox
3. Integrate to Jenkin or Bamboo

#### How to run this script
./run.sh

Note: before you run the script, make sure you change the configure for device.

#### Moreinfo

* [Documentation](https://github.com/julialiuliu/Appium-BDD-python-mobile-app-testing/wiki)
* [Issue Tracking](https://github.com/julialiuliu/Appium-BDD-python-mobile-app-testing/issues)
* Contact me: [jiuboliu@gmail.com](jiuboliu@gmail.com)
