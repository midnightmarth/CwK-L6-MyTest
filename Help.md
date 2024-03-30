For me to get this to work via running into this error:
.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.
You will need to open Powershell as admin, type in Get-ExecutionPolicy to see what the policy is set to.
If it's set to Restricted, then use Set-ExecutionPolicy RemoteSigned, to enable script running if the script has been signed by a trusted publisher.