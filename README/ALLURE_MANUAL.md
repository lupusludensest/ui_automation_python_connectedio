## Current setup

Use Python 3.11 or newer in a virtual environment. From the project root:

```shell
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
python -m behave --format allure_behave.formatter:AllureFormatter --outfile test_results/ features/
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1` and copy the template using
`Copy-Item .env.example .env`. In Command Prompt, use
`.venv\Scripts\activate.bat` and `copy .env.example .env`.

Edit `.env` with the authorized test site's URL and credentials. Keep `.env`
local; commit only `.env.example`, which contains variable names and safe
defaults, not credentials.

Install Google Chrome separately. Selenium 4.50+ uses Selenium Manager to
resolve the matching browser driver; do not add a platform-specific driver
binary such as `chromedriver.exe` to the repository.

To view the generated report, install Allure Commandline separately (on macOS,
run `brew install allure`) and then run:

```shell
allure serve test_results/
```

For a headless Chrome run, set `HEADLESS=true` before running Behave. On macOS
or Linux:

```shell
HEADLESS=true python -m behave --format allure_behave.formatter:AllureFormatter --outfile test_results/ features/
```

On Windows Command Prompt, use `set HEADLESS=true` before the Behave command.

The test target configured in `pages/base_page.py` must be reachable for
browser scenarios to pass.

Сборка html-отчета на локальной машине

Для сборки html–отчета необходима утилита, которая называется allure–commandline. Получить отчет можно несколькими способами:

Способ 1:
1. Скачать последнюю версию allure–commandline по ссылке;

2. Распаковать архив;

3. Добавить путь до директории bin из распакованного архива в системную переменную окружения.

Чтобы убедиться в корректности установки, выполните в командной строке команду

allure --version

Должно появиться сообщение вида:

$ allure --version
2.6.0

После установки allure–commandline откройте в проводнике папку с исходными для построения отчета файлами 
(в нашем примере target/allure-results) и в окне команд (терминале) выполните команду

allure serve

После этого должен сформироваться сам html–отчет, который откроется в браузере по умолчанию автоматически.

C:\Webdrivers\allure-2.13.0\bin>allure --version
2.13.0
C:\Webdrivers\allure-2.13.0\bin>allure serve
Generating report to temp directory...
allure-results does not exists
Report successfully generated to C:\Users\GUROVV~1\AppData\Local\Temp\1112192896526047821\allure-report
Starting web server...
2019-11-19 23:17:38.593:INFO::main: Logging initialized @9785ms to org.eclipse.jetty.util.log.StdErrLog
Server started at <http://192.168.56.1:53498/>. Press <Ctrl+C> to exit

http://192.168.56.1:53498/index.html

##########
1. Configure the project environment with the `requirements.txt` file at the repository root.
2. Run the Behave command documented in the current setup section above.

##########
Renew git to the latest version
git update-git-for-windows

##########
Ignore some file/s when committing/pushing
npm install touch-cli -g
touch .gitignore
Write in the body of the .gitignore names of the files you want to exclude from committing and pushing to GitHub

##########
# ran in parallel, you need to be in the same directory where there are files you are going to run
python 001_main_page_text_here.py & 002_main_page_logo_here.py & 003_main_page_phone_here.py & 004_address_here.py 
& 005_email_here.py & 006_search_product.py & 007_shopbybrand_numbers_oneshot.py & 008_captcha_works.py & 009_checkout_buy.py 
& 010_cart_is_emthy.py & 011_shop_by_brands_have_nine_submenu.py & 012_cart_has_one_item.py & 013_register_and_enter.py & 014_payments_logopics_here.py          
# ran one after another, you need to be in the same directory where there are files you are going to run
python 001_main_page_text_here.py;002_main_page_logo_here.py;003_main_page_phone_here.py;004_address_here.py;005_email_here.py;
006_search_product.py;007_shopbybrand_numbers_oneshot.py;008_captcha_works.py;009_checkout_buy.py;010_cart_is_emthy.py;
011_shop_by_brands_have_nine_submenu.py;012_cart_has_one_item.py;013_register_and_enter.py;014_payments_logopics_here.py

##########
# Install or refresh the framework dependencies in the active virtual environment.
python -m pip install -r requirements.txt

##########
# retrieve the version of Selenium currently installed, from Python
python -c "import selenium; print(selenium.__version__)"

##########
Вебхук/ГитХаб побежден. 
Ход: при генерации урла в утилите ngrok нужно посылать команду  местного урла полностью 
http 192.168.12.130:8080, а не ngrok http 8080, тогда генерится урл/вебхук принимаемый 
ГитХабом: https://4d30-2607-fb90-9b95-b3e4-e9cd-c44f-a4ec-7f53.ngrok.io. 
Добавляем к нему /github-webhook/ и готово: 
https://4d30-2607-fb90-9b95-b3e4-e9cd-c44f-a4ec-7f53.ngrok.io/github-webhook/

##########
Allure with Jenkins
https://www.youtube.com/watch?v=Zf7CJUSW5DA
https://www.qaautomation.co.in/2018/12/allure-report-integration-with-jenkins.html

##########
adb
adb start-server
adb kill-server
adb devices

##########
behave --verbose