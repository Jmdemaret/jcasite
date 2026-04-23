@echo off
cd /d "%~dp0"
echo ============================================
echo  Synchronisation depuis GitHub
echo  (recupere les modifs publiees via l'admin)
echo ============================================
echo.
git pull
echo.
if errorlevel 1 (
  echo [X] Echec. Peut-etre que tu as des modifications locales non commitees.
  echo    Pour forcer : git fetch puis git reset --hard origin/main
) else (
  echo [OK] Dossier local synchronise avec le site en ligne.
)
echo.
pause
