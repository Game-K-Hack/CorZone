<p align="center" >
    <img src="https://cdn.discordapp.com/attachments/837345074877562892/893799068034285588/CorZone.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.2&color=blue" alt="Release - v1.2" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=unstable&color=red" alt="Version - Unstable" />
  </a>
  <a href="https://choosealicense.com/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GNU-yellow" alt="License" />
  </a>
  <a href="https://www.paypal.com/paypalme/gamekdonate">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate" />
  </a>
</div>

<h4 align="center">Synchronization program between Corsair LEDs and Warzone cutscenes</h4>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#supported-os">Supported OS</a> •
  <a href="#supported-devices">Supported devices</a> •
  <a href="#operating-diagram">Operating diagram </a>
</p>

<br>
<br>

## Installation

```
# clone the repo
$ git clone https://github.com/Game-K-Hack/CorZone.git

# change the working directory to sherlock
$ cd CorZone

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```
# start the program
$ python3 corzone.py
[+] Program is start
```

## Requirements

For this script to work, you must have Python in version 3.9 (or a higher version) and have installed the following libraries:

```
tkinter
win32api
win32con
pywintypes
pystray
CV2
time
queue
numpy
cuesdk
threading
datetime
PIL
pytesseract
```

### Supported OS
+ Windows 7 (32-bit and 64-bit)
+ Windows 8, 8.1 (32-bit and 64-bit)
+ Windows 10 (32-bit and 64-bit)
+ macOS 10.13
+ macOS 10.14
+ macOS 10.15


### Supported devices
+ Keyboards
  + CGK65 RGB
  + K55 RGB
  + K63
  + K65 LUX RGB
  + K65 RGB RAPIDFIRE
  + K68
  + K70 LUX
  + K70 LUX RGB
  + K70 RAPIDFIRE
  + K70 RGB
  + K70 RGB MK.2
  + K70 RGB RAPIDFIRE
  + K95 RGB
  + K95 RGB PLATINUM
  + K95 RGB PLATINUM XT
  + K100 RGB
  + STRAFE
  + STRAFE RGB
  + STRAFE RGB MK.2
+ Mice
  + GLAIVE RGB
  + HARPOON RGB
  + HARPOON RGB PRO
  + IRONCLAW RGB
  + KATAR
  + M65 ELITE RGB
  + M65 PRO RGB
  + M65 RGB
  + SABRE
  + SABRE RGB
  + SABRE RGB Laser
  + SABRE RGB Optical
  + Scimitar
  + Scimitar ELITE RGB
  + Scimitar PRO RGB
+ Mouse Mat
  + MM700
  + MM800 RGB
+ Headsets
  + VIRTUOSO RGB
  + VIRTUOSO RGB SE
  + VOID PRO USB
  + VOID PRO WIRELESS
  + VOID USB
  + VOID WIRELESS
+ Headset Stand
  + ST100 RGB
+ LED Controllers
  + Commander PRO
  + Lighting Node CORE
  + Lighting Node PRO
+ Memory module
  + DOMINATOR PLATINUM RGB
  + Vengeance RGB PRO
  + VENGEANCE RGB PRO SL
+ Coolers
  + CORSAIR ONE
  + CORSAIR ONE PRO
  + H100i Platinum
  + H100i PRO
  + H115i Platinum
  + H115i PRO
  + H150i PRO

                
## Operating diagram 

![](https://cdn.discordapp.com/attachments/879074487071539280/893814554994294784/unknown.png)
