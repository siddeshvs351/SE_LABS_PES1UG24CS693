# Lab Reflection

This lab helped me understand the importance of static analysis in Python development.

- **Pylint** helped identify naming, documentation, and code-quality problems.
- **Bandit** identified security risks such as hardcoded secrets, weak hashing, and insecure random-number generation.
- **Flake8** identified formatting and whitespace violations.

I corrected the reported problems and ran the tools again to verify the improvements. The final Pylint score was 10.00/10, Bandit reported no issues, and Flake8 reported no formatting violations.

I learned that static analysis can detect potential problems before code is deployed. However, passing these tools does not guarantee that a program is completely secure or free of logical bugs.
