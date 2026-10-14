# Lab 5: Static Code Analysis — Issues and Fixes

## Objective

To improve the quality, security, and formatting of the digital wallet Python program using Pylint, Bandit, and Flake8.

## Issue Documentation Table

The line numbers below refer to the original source and reports. Verify the exact Flake8 line numbers against `flake8_before.txt` before submission.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Hardcoded gateway secret | Security — Bandit B105 | 6 | The gateway secret was stored directly in the source code. | Read the secret from the `GATEWAY_SECRET` environment variable. |
| Weak SHA-1 hashing | Security — Bandit B324 | 14 | SHA-1 is not appropriate for securely hashing wallet PINs. | Replaced SHA-1 with PBKDF2-HMAC-SHA256 using a salt and 100,000 iterations. |
| Insecure temporary-file creation | Security — Bandit B306 | 60 | `tempfile.mktemp()` can introduce a race condition. | Used `tempfile.NamedTemporaryFile()` instead. |
| Predictable random number generation | Security — Bandit B311 | 64 | `random.randint()` is not intended for security-sensitive random values. | Used the `secrets` module to generate the OTP. |
| Mutable default argument | Code quality — Pylint W0102 | 17 | The default argument `log=[]` could share the same list across function calls. | Changed the default to `None` and initialized the list inside the function. |
| Missing docstrings | Code quality — Pylint C0114, C0116 | 1, 13, 17, 27, 32, 45, 50, 54, 58, 63 | The module and functions lacked documentation strings. | Added a module docstring and function docstrings. |
| Naming convention violations | Code quality — Pylint C0103 | 9, 13, 17, 27, 32, 45, 50, 54, 58, 78 | Names such as `hashPin`, `addMoney`, and `creditAmounts` did not follow Python naming conventions. | Renamed functions and variables using `snake_case`; constants use uppercase names where appropriate. |
| Use of global statement | Code quality — Pylint W0603 | 28 | The daily limit was modified using a global variable. | Stored the daily limit in a settings dictionary and updated the dictionary value. |
| Unused function parameter | Code quality — Pylint W0613 | 50 | The merchant-type parameter was not used in the cashback calculation. | Renamed it `_merchant_type` to indicate that it is intentionally unused. |
| Inline comment spacing | Formatting — Flake8 E261 | See original Flake8 report | An inline comment did not have the required spacing. | Corrected the spacing before the inline comment. |
| Missing whitespace around operator | Formatting — Flake8 E225 | See original Flake8 report | An operator did not have the required surrounding whitespace. | Added the required whitespace around the operator. |
| Missing whitespace after comma | Formatting — Flake8 E231 | See original Flake8 report | A comma was not followed by the required whitespace. | Corrected comma spacing. |
| Incorrect blank lines after a function | Formatting — Flake8 E305 | See original Flake8 report | A function definition was not followed by the required blank lines. | Corrected blank-line spacing between function definitions and subsequent code. |

## Before-and-After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.69/10 | 10.00/10 |
| Bandit | 4 reported findings | No issues identified |
| Flake8 | 4 reported formatting violations | No formatting violations reported |

## Conclusion

The digital wallet program was improved by addressing security vulnerabilities, code-quality warnings, and formatting violations. The final reports showed a Pylint score of 10.00/10, no Bandit findings, and no Flake8 formatting violations.

### Bandit Verification
All Bandit findings were addressed, and the after-scan reported no remaining issues.
