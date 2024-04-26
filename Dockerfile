FROM mcr.microsoft.com/powershell:latest

# Add checker to Docker image
ADD /pwsh_checker.ps1 /usr/local/bin/pwsh_checker.ps1
RUN chmod +x /usr/local/bin/pwsh_checker.ps1 && \
    pwsh -Command \
    "Set-PSRepository PSGallery -InstallationPolicy Trusted -ErrorAction Stop; \
    Install-Module PSScriptAnalyzer -Scope AllUsers -ErrorAction Stop"

ENTRYPOINT ./usr/local/bin/pwsh_checker.ps1
