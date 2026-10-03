# Running the browser tests and viewing the Allure report

These instructions are for the current Behave/Selenium tests on macOS.

## Set up the project

From the project root, create and activate a virtual environment, then install
the dependencies:

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install Google Chrome if it is not already installed. Selenium Manager, included
with the project's Selenium dependency, resolves the matching browser driver.

The tests need `APP_USERNAME` and `APP_PASSWORD` for an authorized test account.
Create or edit a local `.env` file in the project root:

```dotenv
APP_USERNAME=your-test-username
APP_PASSWORD=your-test-password
```

The app URL is optional. It defaults to `https://devcloud.connectedio.com`;
to use a different authorized test environment, add `APP_BASE_URL` to `.env`.
Keep `.env` private; it is excluded from Git.

## Run the tests

Run Behave from the project root:

```shell
python -m behave --format allure_behave.formatter:AllureFormatter --outfile test_results/ features/
```

For headless Chrome, prefix the command with `HEADLESS=true`:

```shell
HEADLESS=true python -m behave --format allure_behave.formatter:AllureFormatter --outfile test_results/ features/
```

The test target must be reachable for the browser scenarios to pass. The run
writes Allure result files to `test_results/`.

## View the Allure report

Install Allure Commandline with Homebrew if needed:

```shell
brew install allure
```

After running the tests, serve the report from the project root:

```shell
allure serve test_results/
```

Allure starts a local web server and opens the report in a browser. Stop the
server with Ctrl+C in the terminal.
