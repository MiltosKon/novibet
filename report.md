
# Project Report

## 1. Framework Stability
- Added element waits.
- Modularized my code, making it easier to find the root cause of issues.
- Used `webdriver_manager` instead of a direct WebDriver executable to avoid manual updates whenever Chrome updates. This helps in overcoming the difficulty of disabling automatic Chrome updates.
- Implemented a global time setting to handle daylight saving time adjustments, which was initially overlooked.

## 2. Improved Performance
- Ran the Chrome instance in headless mode to avoid UI rendering, enhancing performance. Overcame challenges with Cloudflare checks in headless mode by setting a custom user-agent in ChromeDriver options.

## 3. Use of Page Object Model
- Implemented Page Object classes for each web page involved in the scraping process. This structure excluded the XML generation class, as it was not associated with a specific page.

## 4. Configuration File Utilization
- Created configuration files for locators and URLs, as these are the most likely to change, ensuring flexibility and easy maintenance.

## Extra Efforts and Challenges
- Attempted to create a scheduled GitHub Actions workflow but faced issues due to geoblocking on novibet.gr. Tried to bypass this by setting location coordinates in ChromeDriver options, but it was unsuccessful.
