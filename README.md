# PyDictionary by ne0mesys 
*This is my first script, I hope you guys enjoy it :)* 

## Welcome

This is my first made ethical hacking tool that allows users to generate dictionaries for cybersecurity purposes. 

The software enables penetration testers to input personal data of a target in order to create a massive number of combinations, resulting in a comprehensive custom dictionary. It currently allows users to enter input for ***name***, ***surname***, ***second_surname***, ***nickname***, ***second_nickname***, ***day_of_birth***, ***month_of_birth*** & ***year_of_birth***. This software also includes, a large amount of pre-defined data stored in several lists in order to create a more sophisticated dictionary. However, it will soon be updated in order to allow more and more inputs, since the more inputs it has, the bigger and more precise the dictionary is. All the libraries used in this software are part of the Python standard library. Therefore, no individual installation is required. 

You are welcome to taste it, download it and improve it yourself! However, REMEMBER to stay tuned for the next updates... 

This tool is developed strictly for educational and ethical purposes. I DO NOT take any responsibility for the misuse of this tool. 

By ne0mesys

## Requirements

### For Linux 

Python 3 is required to run this software. In case you don't have it installed it, you can find the installation instructions below. 
```
sudo apt update && sudo apt upgrade
sudo apt install python3
 ```

### For Windows 

Here's a short documentation about how to install the requirements for Windows users:

* Download Python 3 in the Microsoft Store.

### For Arch Linux

Here's a short documentation about how to install the requirements for Arch Linux users:

First, verify whether you have Python installed or not: 
```
python --version
```
or 
```
python3 --version
```

If you have **Python** installed, just download the **PyDictionary.py** file.

if you **DON'T** have it, install it using these commands:
```
sudo pacman -S python
sudo pacman -S python-pip
```

## Installation 

### For Linux & Arch Linux

Here's a short documentation about how to install the software for Linux users: 
```
sudo apt install git 
sudo git clone https://github.com/ne0mesys/PyDictionary.git
cd PyDictionary
```

### For Windows

Download the **PyDictionary.py** file. 

## Execution

### For Linux & Arch Linux

Once we are in the same folder of the software, we can proceed to enable its execution for Linux users. 

The software includes the Shebang line  ``` #!/usr/bin/env python3 ``` which allows the user to execute it directly, here's a quick guide about the two different ways to execute the software:
* Firstly, we give execution permissions to the file: 
```
sudo chmod +x PyDictionary.py
```
* Secondly, we execute the program:

```
./PyDictionary.py
python3 PyDictionary.py
```

### For Windows

*Right-click* over the **PyDictionary.py** file, and open with the Python 3 software. 


## Usage 

The usage of this software is quite simple. However, for those who prefer reading the documentation first, here is a quick guide ;)

* Type 'none' when there is no data to enter, so the software does not take the input. 
* Press 'Ctrl + C' to exit. 
* Press 'Enter' after each input to submit it.
* After execute it, press 'Enter' to continue.

## Version & Updates

### v1.0 
The current version of the software is the v1.0 which includes:

[+] Features: 
  * Name
  * Surname
  * Second_Surname
  * Nickname
  * Second_Nickname
  * Day_Of_Birth
  * Month_Of_Birth
  * Year_Of_Birth

### v1.5 
It is estimated that the version v1.5 will include the following features:

[+] Features

[+] New:
  * Pet_name
  * Pet_age


## Author:

* Ne0mesys

Feel free to open an Issue...
```
E-Mail at: ne0mesys.acc@gmail.com
```
