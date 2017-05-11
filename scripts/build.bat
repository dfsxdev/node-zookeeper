set platform=%1%
set configuration=%2%
echo building zookeeper client library...

msbuild "..\deps\zookeeper\src\c\zookeeper.vcxproj" /p:Platform=%platform%;Configuration=%configuration% /clp:errorsonly /fl /flp:errorsonly

echo done