@echo off
if not exist "user_data/password.txt" (
	if not exist "user_data/username.txt" (
		.\run_me_first.py
	)
) else (
	.\main.py
)