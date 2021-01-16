behave -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/
allure serve ./reports/report/
