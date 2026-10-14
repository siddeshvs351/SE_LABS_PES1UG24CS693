# Static Analysis Issues and Fixes

## 1. Pylint

**Before:** 5.69/10

**After:** 10.00/10

Issues fixed:
- Added module and function docstrings.
- Renamed functions and variables to follow snake_case conventions.
- Removed the mutable default argument.
- Removed the global statement by using a settings dictionary.
- Addressed unused parameters and naming warnings.

## 2. Bandit

**Before:** 4 security findings.

**After:** No issues identified.

Issues addressed:
- Removed the hardcoded gateway secret.
- Replaced SHA-1 PIN hashing with PBKDF2-HMAC-SHA256.
- Replaced insecure temporary-file creation.
- Replaced predictable random-number generation with the secrets module.

## 3. Flake8

**Before:** 4 formatting violations.

**After:** No formatting violations reported.

Issues addressed:
- Corrected whitespace around operators.
- Corrected whitespace after commas.
- Fixed inline comment spacing.
- Corrected blank-line formatting.

## Conclusion

Static analysis helped improve code quality, formatting, and security. The corrected program achieved a Pylint score of 10.00/10, and Bandit and Flake8 reported no findings.
