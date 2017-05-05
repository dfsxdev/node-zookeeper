. ..\scripts\env.ps1

$platform = $args[0];
$configuration = $args[1];

Write-Host 'building zookeeper client library...'

Write-Host "msbuild `"$ZK_DEPS\src\c\zookeeper.vcxproj`" /p:`"Platform=$platform;Configuration=$configuration`" /clp:errorsonly /fl /flp:errorsonly"

msbuild "$ZK_DEPS\src\c\zookeeper.vcxproj" /p:"Platform=$platform;Configuration=$configuration" /clp:errorsonly /fl /flp:errorsonly

Write-Host 'done'