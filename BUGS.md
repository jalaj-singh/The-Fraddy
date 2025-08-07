# Fraddy Bug Report

This document lists the identified bugs in the Fraddy personal assistant, categorized by severity.

## Critical Bugs

*   **C1: Hardcoded Credentials:** The application contains hardcoded credentials, including:
    *   Gmail username and password in the `sendEmail` function.
    *   SSH username and password for `paramiko` connections.
    *   This is a major security vulnerability that exposes user accounts and remote systems to unauthorized access.
*   **C2: Arbitrary Remote Code Execution:** The `linux` command feature allows any user to execute arbitrary commands on a remote server using hardcoded SSH credentials. This is an extremely dangerous vulnerability.

## High Bugs

*   **H1: Hardcoded API Keys:** The application has placeholder or hardcoded API keys for:
    *   WolframAlpha
    *   NewsAPI (in `NewsFromBBC`)
    *   OpenWeatherMap
    *   This prevents the features from working out-of-the-box and is poor security practice.
*   **H2: Hardcoded File Paths:** The script uses absolute, user-specific file paths for:
    *   Opening applications (Pycharm, VS Code).
    *   Saving screenshots.
    *   Accessing the local music folder.
    *   Finding the `chromedriver.exe` executable.
    *   This makes the script not portable and guaranteed to fail on other machines.

## Medium Bugs

*   **M1: Inadequate Error Handling:**
    *   The `myCommand` function uses unbounded recursion on speech recognition errors, which can lead to a stack overflow.
    *   External API calls, web requests, and file system operations lack proper `try...except` blocks, making the application prone to crashing.
    *   The Wikipedia search function does not handle disambiguation or page-not-found errors.
*   **M2: Lack of Dependency Management:** There is no `requirements.txt` file, making it very difficult to install the correct dependencies and set up the development environment.
*   **M3: Unsafe Shutdown Command:** The `shutdown` command logic is unsafe. It initiates a system shutdown for any voice command that isn't explicitly "no". It should require a clear "yes" to proceed.
*   **M4: Logical Flaw in YouTube Search:** The `WebDriverWait` timeout is set to 0 seconds, which will cause the search to fail before the page has a chance to load.

## Low Bugs

*   **L1: Monolithic Code Structure:** All application logic is contained in a single `fraddy.py` file within a `while` loop, making the code difficult to read, maintain, and test.
*   **L2: Poor Code Quality:**
    *   Functions are defined inside `if` statements.
    *   Redundant imports (e.g., `paramiko`).
    *   Presence of commented-out, non-functional code.
    *   Inconsistent naming conventions.
*   **L3: Redundant `paramiko` calls:** The `paramiko` library is imported and used in multiple `elif` blocks, when the connection could be established once.
