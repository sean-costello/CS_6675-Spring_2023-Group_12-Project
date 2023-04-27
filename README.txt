*******************************************************************************************************************

Georgia Institute of Technology
Spring 2023
CS 6675
Group 12: Ritvik Chandrashekhar, Sean Costello, Christian Duetemeyer, Sam Wong
A More Secure Torrenting: Sandboxing, VPN, and Malware Detection Torrent Package

*******************************************************************************************************************

Welcome:
This is the README file for Group 12's semester-long project. This README file will instruct you on
how to set up the Hyper-V virtual machine (VM). This Hyper-V VM is the core deliverable of our
project. We have two main Python scripts that run inside this Hyper-V VM, along with other important
features such as Windows Defender, Shared Folders, ClamAV, Windows Sandbox, etc. The two main Python
scripts are called monitor.py and sandbox_monitor.py.

*******************************************************************************************************************

The following instructions are adapted from Microsoft Learn's website on this topic, as well as having
personally imported this ourselves. For more information, please refer to Microsoft's instructions:
https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines

Downloading the Hyper-V VM zip folder:
Step 1: Open a web browser and navigate to: https://drive.google.com/file/d/1asnSBF0xCl8a_jRB2etA5Ry630Q-YpBH/view?usp=share_link
Step 2: Download the "Hyper-V VM" folder.
Step 3: Once downloaded, unzip the contents. Leave everything inside of the "CS 6675" folder.

Importing the Hyper-V VM to Hyper-V Manager on Windows 10 Pro / Windows 11 Pro Host:
Step 1: Click the "Action" tab at the top of the menu bar and then click "Import Virtual Machine...".
Step 2: Once the wizard opens, click "Next".
Step 3: Select the folder that contains the Hyper-V VM. 





