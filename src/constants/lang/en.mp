Ç¶commonÇ§infoÇ§descπMarkdown to PDF converter•mottoŸ7For writing faster? No. For writing with *class*? Yusss¶promptÇ£yes√¢no¬£cliÑ§initÅØchoose_languageØChoose language¶promptÇ¶answer¶Answer∞list_instructionŸAUse up and down arrow keys to navigate, press enter key to chooseßgeneralÉ£kbi±Cancelled by userØbelow_min_widthŸÜYour terminal width is well below than the bare minimum

{terminal_width} instead of {min_terminal_width} and above

Consider resizing∞below_recc_widthŸnYour terminal width is below than the recommended

{terminal_width} instead of {recc_terminal_width} and above•katexÜ±not_installed_msgŸCKaTeX binary is not found and/or is not supported in this platform.πnot_installed_no_solution⁄\It seems that the program can not detect this machine's platform or is unable to find a way to install KaTeX in this machine. Fret not, as I have the following outline to follow on how to install KaTeX:

1. Install Node.js: https://nodejs.org/en/download/
2. Install KaTeX through Node.js Package Manager (npm): https://katex.org/docs/node.html#npm±not_installed_tplŸåFret not, the program detected that you are in {platform}, and you can follow the instructions below on how to install KaTeX.

{instruction}±not_installed_win⁄≥1. Copy the following text, excluding the three backticks (`) enclosing the text:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

---

2. Press `Windows` + `R` (Press `Windows` and `R` keys simultaneously)

---

3. A window with a title `Run` should appear. Focus to the said window in the `Open:` text field by hovering the mouse towards the said text field and left-clicking the mouse and type `powershell`.

---

4. Press `Ctrl` + `Shift` + `Enter` (Press `Ctrl`, `Shift`, and `Enter` keys simultaneously).

---

5. A window with a title `User Account Control` should appear.

---

6. Focus to the said window and press the `Yes` button by hovering the mouse towards the said button and left-clicking the mouse.

---

7. A window named `Administrator: Windows Powershell`. Focus to said window by hovering the mouse towards the said window and left-clicking the mouse. Then, press `Ctrl` + `V` (Press `Ctrl` and `V` keys simultaneously).

---

8. Restart your computer, then login to the user account to which you have done this instructions.

---

9. Copy the following text, excluding the three backticks (`) enclosing the text:
```
choco install nodejs -y; npm install katex
```

---

10. Repeat step 2-7.

---

If the window `Administrator: Windows Powershell` seems to hang up, focus to said window by hovering the mouse towards the said window and left-clicking the mouse, then press `Enter` until something happens.

If you have managed to install this program, but is not able to make this work, I apologize for the enormous effort you have made to make it through to this part. However, it seems that it is not enough. As a Linux user, I would not be able to help, nor would I want to even if I have the ability to do so. Windows has traumatized me to the point of despair, extreme paranoia, and mania. I do not wish for Windows to touch me ever again. Thank you for attempting to use this program, but it seems that this is our farewell. I wish you nothing but the best, kind stranger.±not_installed_mac⁄û1. Open your preferred terminal and run the following command:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

---

2. Next, for OS X 10.13 (High Sierra) or younger, run the following command:
```
echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.profile
```

And for OS X 10.12 (Sierra) or older, use the following command instead:
```
echo 'export PATH=/usr/local/bin:/usr/local/sbin:$PATH' >> ~/.profile
```

---

3. Afterwards, install the rest of the prerequisites by running the following command:
```
brew install node
```

---

4. Then, install katex with npm by running the following command:
```
npm install katex
```

---

If you have managed to install this program, but is not able to make this work, I apologize for the enormous effort you have made to make it through to this part. As a poor Linux user rocking an 11-year old thinkpad, I do not have access to any Mac machines that I can test this program in, along with problems that might come in the way. Thank you for attempting to use this program, but it seems that this is our farewell. I wish you nothing but the best, kind stranger.≥not_installed_linuxŸ…Lookie look, you are rocking a Linux machine, I know you can do it!

Prerequites:
- Node.js
    - npm

---

1. Open your preferred terminal and run the following command:
```
npm install katex
```

---