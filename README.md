<div align="center">
    <h1>Espressif PowerShell script Checker</h1>
</div>

**Welcome to the Espressif PWSH Checker!**

This repository serves as a PowerShell script checker such as a pre-commit hook for Espressif's projects.

It is based on [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer?tab=readme-ov-file) from [PowerShell](https://github.com/PowerShell).

---

- [Usage](#usage)
- [CHANGELOG](#changelog)
- [License](#license)
- [Contributing](#contributing)

---

## Usage
1. First of all, Docker needs to be installed on the machine ([Docker](https://www.docker.com/#build)).
2. Then add this hook into `.pre-commit-config.yaml` in your project.
```
  - repo: https://github.com/espressif/esp-pwsh-check
    rev: v1.0.0
    hooks:
    -   id: check-powershell-scripts
```
3. After this pre-commit should run this hook on all modified `.ps1` scripts.

---

## CHANGELOG
In this document, the main changes for this project will be documented.
- The [`CHANGELOG.md`](CHANGELOG.md) file.

## License

This document and the attached source code are released as Free Software under MIT license. See the accompanying [LICENSE](LICENSE) file for a copy.


## Contributing

📘 If you are interested in contributing to this project, see the [project Contributing Guide](CONTRIBUTING.md).
