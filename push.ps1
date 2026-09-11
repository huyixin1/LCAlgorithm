# 一键推送刷题笔记到 GitHub
# 用法：双击运行，或右键"使用 PowerShell 运行"
# 前提：已完成 git init 和 git remote add origin（见 README.md）

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# 1. 检查是否已初始化 git
if (-not (Test-Path ".git")) {
    Write-Host "❌ 尚未初始化 git。请先执行：" -ForegroundColor Red
    Write-Host "   git init"
    Write-Host "   git remote add origin https://github.com/<你的用户名>/<仓库名>.git"
    Read-Host "按回车退出"
    exit 1
}

# 2. 提交所有变更
git add -A
$msg = "daily notes: $(Get-Date -Format 'yyyy-MM-dd')"
git commit -m $msg

# 3. 推送
git push
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 推送成功！" -ForegroundColor Green
} else {
    Write-Host "⚠️ 推送失败，请检查网络或登录状态" -ForegroundColor Yellow
}

Read-Host "按回车退出"
