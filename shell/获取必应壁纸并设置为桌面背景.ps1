Function Set-WallPaper {
<#
	.SYNOPSIS
	Applies a specified wallpaper to the current user's desktop
	
	.PARAMETER Image
	Provide the exact path to the image

	.PARAMETER Style
	Provide wallpaper style (Example: Fill, Fit, Stretch, Tile, Center, or Span)

	.EXAMPLE
	Set-WallPaper -Image "C:\Wallpaper\Default.jpg"
	Set-WallPaper -Image "C:\Wallpaper\Background.jpg" -Style Fit
#>

param (
	[parameter(Mandatory=$True)]
	# Provide path to image
	[string]$Image,
	# Provide wallpaper style that you would like applied
	[parameter(Mandatory=$False)]
	[ValidateSet('Fill', 'Fit', 'Stretch', 'Tile', 'Center', 'Span')]
	[string]$Style
)

$WallpaperStyle = Switch ($Style) {
	"Fill" {"10"}
	"Fit" {"6"}
	"Stretch" {"2"}
	"Tile" {"0"}
	"Center" {"0"}
	"Span" {"22"}
}

If($Style -eq "Tile") {
	Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name WallpaperStyle -Value $WallpaperStyle
	Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name TileWallpaper -Value 1
}
Else {
	Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name WallpaperStyle -Value $WallpaperStyle
	Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name TileWallpaper -Value 0
}

Add-Type -TypeDefinition @" 
using System; 
using System.Runtime.InteropServices;

public class WinApiUser32
{ 
	[DllImport("User32.dll",CharSet=CharSet.Unicode)] 
	public static extern int SystemParametersInfo (Int32 uAction, 
													Int32 uParam, 
													String lpvParam, 
													Int32 fuWinIni);
}
"@ 

	$SPI_SETDESKWALLPAPER = 0x0014
	$UpdateIniFile = 0x01
	$SendChangeEvent = 0x02

	$fWinIni = $UpdateIniFile -bor $SendChangeEvent

	[WinApiUser32]::SystemParametersInfo($SPI_SETDESKWALLPAPER, 0, $Image, $fWinIni)
}

$imageFolder = "$PSScriptRoot\.bingimg"
# 检查文件夹
if (Test-Path -Path $imageFolder -PathType Container) {
	$files = Get-ChildItem -Path $imageFolder
	if ($files.Count -gt 10) {
		$files | Sort-Object LastWriteTime | Select-Object -First 1 | ForEach-Object { Remove-Item $_.FullName }
	}
}
else {
	New-Item -ItemType Directory -Name $imageFolder
}

$filepath = "$imageFolder\$([guid]::NewGuid().ToString()).jpg"
Invoke-RestMethod "bing.com$((Invoke-RestMethod "bing.com/HPImageArchive.aspx?format=js&uhd=1&uhdwidth=3840&uhdheight=2160&n=1").images[0].url)" -OutFile $filepath
Set-WallPaper -Image $filepath -Style Fill
