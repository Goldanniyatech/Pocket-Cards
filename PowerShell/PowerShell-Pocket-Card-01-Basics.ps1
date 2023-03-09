

# Generating list of cmdlets & functions 
# Get-Command

Write-Host "Power Shell Starting Script"

# Give Free Virtual Memory 
Get-WmiObject -Class Win32_OperatingSystem -ComputerName localhost  

# # # # # # # # # # # # # # #
# 
#  Variables
# 
# # # # # # # # # # # # # # #

$player_name = "Jonesy"
$total_player_count = 100
$current_player_count = 58

# Introduction Message 
Write-Host "Hello, $player_name! You will be against $current_player_count players in the map! Good luck!"

# # # # # # # # # # # # # # #
# 
#  Conditions
# 
# # # # # # # # # # # # # # #

if ($current_player_count -gt $total_player_count) {
    Write-Host "One player has been rejected: there are too many players"
}
elseif ($current_player_count -eq $total_player_count) {
    Write-Host "The game has reached the maximum amount of players"
}
else {
    Write-Host "The game has enough players! Go!"
}

