<#
PowerShell helper to initialize a git repo, create a GitHub repo (via `gh`), and push.
Run this from the project root (where your index.html lives).

Usage: Open PowerShell in the project folder and run:
  ./scripts/setup_github_pages.ps1

This script attempts to use the GitHub CLI `gh` if available. If you prefer to create the repo on GitHub manually, skip the `gh` steps and run the git commands shown.
#>

Set-StrictMode -Version Latest
cd (Split-Path -Path $MyInvocation.MyCommand.Path -Parent) | Out-Null
cd ..

function Exec([string]$cmd) { Write-Host "> $cmd"; iex $cmd }

if (-not (Test-Path .git)) {
  Write-Host "Initializing git repository..."
  Exec 'git init'
} else {
  Write-Host "Git repo already initialized."
}

Exec 'git add --all'
Exec 'git commit -m "Initial commit: site files"' 2>$null

$useGh = $false
try { gh --version > $null; $useGh = $true } catch { $useGh = $false }

if ($useGh) {
  $defaultName = "$(gh api user -q .login).github.io"
  $repoName = Read-Host "Enter GitHub repo name (default: $defaultName)"
  if ([string]::IsNullOrWhiteSpace($repoName)) { $repoName = $defaultName }

  Write-Host "Creating repository '$repoName' and pushing..."
  Exec "gh repo create $repoName --public --source=. --remote=origin --push"
  Write-Host "If this succeeds, GitHub Pages will serve from the main branch. Allow a minute after first push."
} else {
  Write-Host "gh CLI not found. To finish manually, create a repo on GitHub, then run these commands (replace <URL>):"
  Write-Host "---"
  Write-Host "git remote add origin <URL>"
  Write-Host "git branch -M main"
  Write-Host "git push -u origin main"
  Write-Host "---"
}

Write-Host "Done. If you want the repository name to be username.github.io for user pages, create it using that exact name."
