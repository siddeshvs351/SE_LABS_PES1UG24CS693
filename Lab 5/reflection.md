# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing the program to identify potential bugs, security vulnerabilities, code-quality problems, and style violations. In this lab, I used Pylint, Bandit, and Flake8 to analyze a digital wallet application.

## 2. What did I learn from Pylint?

Pylint helped identify code-quality problems, including missing docstrings, inconsistent naming conventions, mutable default arguments, unused parameters, and the use of a global statement.

I corrected these issues by improving documentation, following Python naming conventions, replacing the mutable default argument with `None`, and managing the daily limit through a settings dictionary.

The Pylint score improved from 5.69/10 to 10.00/10.

## 3. What did I learn from Bandit?

Bandit helped identify potential security vulnerabilities in the original program, including a hardcoded secret, weak SHA-1 hashing, insecure temporary-file creation, and predictable random-number generation.

I addressed these findings by using environment variables for secrets, PBKDF2-HMAC-SHA256 for PIN hashing, `NamedTemporaryFile()` for temporary-file creation, and the `secrets` module for OTP generation.

The final Bandit report stated that no issues were identified.

## 4. What did I learn from Flake8?

Flake8 helped identify violations of Python formatting conventions, including incorrect inline-comment spacing, missing whitespace around operators, missing whitespace after commas, and incorrect blank-line spacing.

I corrected the formatting violations and reran Flake8. The final report contained no formatting violations.

## 5. Why is static code analysis important?

Static code analysis helps developers identify potential problems early, before code is deployed. It improves readability, maintainability, consistency, and security. Using multiple tools is useful because each tool focuses on a different category of problems.

## 6. What challenges did I face?

The main challenges were understanding the warnings reported by each tool, correcting the source code without introducing syntax errors, and generating separate before-and-after reports.

I learned to interpret the reported issue codes, make targeted changes, rerun the tools, and verify the results instead of assuming that a code change had fixed every issue.

## 7. Does passing static analysis guarantee that the program is completely secure?

No. Static analysis can identify many common problems, but it cannot guarantee that the program is free from all bugs or vulnerabilities. Runtime testing, code review, and additional security checks are still necessary.

The wallet PIN hash in this lab uses a salt generated at startup, so the hash is not persistent across program restarts. A real application would need a carefully designed and tested persistent credential-storage mechanism.

## 8. Conclusion

This lab demonstrated how Pylint, Bandit, and Flake8 complement one another. After fixing the reported issues, the program achieved a Pylint score of 10.00/10, Bandit reported no findings, and Flake8 reported no formatting violations. I learned that static analysis is an important part of writing cleaner, more maintainable, and more secure Python code.
