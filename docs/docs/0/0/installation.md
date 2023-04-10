<h1 align="center" style="font-weight: bold">
    Developing md2pdf
</h1>


<div class="toc"><h2 id="toc"><b><a href="#toc">Table of Contents</a></b></h2>
<ul><li><a href="#installing-prerequisites">Installing Prerequisites</a><ul><li><a href="#installing-prerequisites-windows">Windows</a></li><li><a href="#installing-prerequisites-mac">Mac</a></li><li><a href="#installing-prerequisites-linux">Linux</a><ul><li><a href="#installing-prerequisites-linux-debian">Debian</a></li><li><a href="#installing-prerequisites-linux-arch">Arch</a></li></ul></li></ul></li></ul></div>

<h2 id="installing-prerequisites"><b><a href="#installing-prerequisites">Installing Prerequisites</a></b></h2>

<h2 id="installing-prerequisites-windows"><b><i><a href="#installing-prerequisites-windows">Windows</a></i></b></h2>

1. Copy the following text:

    ```ps1
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

2. Press `Win`. An interface should pop up as shown below:

    ![1](/docs/assets/images/prerequisites/python/windows/1.png)

3. Search for settings by typing "`Settings`" in the text field as shown below:

    ![2](/docs/assets/images/prerequisites/python/windows/2.png)

    Press `Enter`.

4. A window should pop up as shown below:

    ![3](/docs/assets/images/prerequisites/python/windows/3.png)

    Press "`Apps`" in the selection below.

5. You should be redirected to "`Apps & Features`" as shown below:

    ![4](/docs/assets/images/prerequisites/python/windows/4.png)

    Below the subtitle "`Apps & Features`", press the hyperlink "`App execution aliases`".

6. You should be redirected to "`App execution aliases`" as shown below:

    ![5](/docs/assets/images/prerequisites/python/windows/5.png)

    Toggle the "`App installer`" for both "`python.exe`" and "`python3.exe`". Exit the settings app.

7. Press `Windows` + `R` (Press `Windows` and `R` keys simultaneously)

8. A window with a title `Run` should appear. Focus to the said window in the `Open:` text field by hovering the mouse towards the said text field and left-clicking the mouse and type `powershell` as shown below:

    ![](/docs/assets/images/run_box_ps.png)

9. Press `Ctrl` + `Shift` + `Enter` (Press `Ctrl`, `Shift`, and `Enter` keys simultaneously).

10. A window with a title `User Account Control` should appear as shown below:

    ![](/docs/assets/images/UAC_ps.png)

11. Focus to the said window and press the `Yes` button by hovering the mouse towards the said button and left-clicking the mouse. A window named `Administrator: Windows Powershell` should pop-up.

12. Focus to the window named `Administrator: Windows Powershell` window by hovering the mouse towards the said window and left-clicking the mouse. Then, press `Ctrl` + `V` (Press `Ctrl` and `V` keys simultaneously), and `Enter` afterwards.

    If the window `Administrator: Windows Powershell` seems to hang up, focus to said window by hovering the mouse towards the said window and left-clicking the mouse, then press `Enter` five times every minute or so until something happens.

13. Restart your computer, then login to the user account to which you have done the above instructions at.

14. Copy the following text:

    ```ps1
    choco install -y python
    ```

    Then, repeat step 7-12.

15. Copy the following text:

    ```sh
    python3 -m pip install wh-m2p
    ```

    Then, repeat step 12.

Congratulations, you can now use md2pdf by copying the following text:

```sh
m2p
```

OR this:

```sh
python3 -m md2pdf
```

Then doing the following steps:

1. Press `Windows` + `R` (Press `Windows` and `R` keys simultaneously)

2. A window with a title `Run` should appear. Focus to the said window in the `Open:` text field by hovering the mouse towards the said text field and left-clicking the mouse and type `powershell` as shown below:

    ![](/docs/assets/images/run_box_ps.png)

3. Press `Enter`.

4. Focus to the window named `Administrator: Windows Powershell` window by hovering the mouse towards the said window and left-clicking the mouse. Then, press `Ctrl` + `V` (Press `Ctrl` and `V` keys simultaneously), and `Enter` afterwards.

<h2 id="installing-prerequisites-mac"><b><i><a href="#installing-prerequisites-mac">Mac</a></i></b></h2>

1. Open your preferred terminal and run the following command:

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```

2. Next, for OS X 10.13 (High Sierra) or younger, run the following command:

    ```sh
    echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.profile
    ```

    And for OS X 10.12 (Sierra) or older, use the following command instead:

    ```sh
    echo 'export PATH=/usr/local/bin:/usr/local/sbin:$PATH' >> ~/.profile
    ```

3. Afterwards, install the rest of the prerequisites by running the following command:

    ```sh
    brew install python
    ```

4. Install md2pdf by running the following command:

    ```sh
    python3 -m pip install wh-m2p
    ```

Congratulations, you can now use md2pdf by running the following:

```sh
m2p
```

OR

```sh
python3 -m md2pdf
```

<h2 id="installing-prerequisites-linux"><b><i><a href="#installing-prerequisites-linux">Linux</a></i></b></h2>

<h2 id="installing-prerequisites-linux-debian"><a href="#installing-prerequisites-linux-debian">Debian</a></h2>

1. Open your preferred terminal and run the following command to install the prerequisites:

    ```sh
    sudo apt update -y
    sudo apt install -y python3-pip
    ```

2. Finally, install md2pdf by running the following command:

    ```sh
    python3 -m pip install wh-m2p
    ```

Congratulations, you can now use md2pdf by running the following:

```sh
m2p
```

OR

```sh
python3 -m md2pdf
```

<h2 id="installing-prerequisites-linux-arch"><a href="#installing-prerequisites-linux-arch">Arch</a></h2>

1. Open your preferred terminal and run the following command to install the prerequisites:

    ```sh
    sudo pacman -Syyu --noconfirm python
    ```

2. Finally, install md2pdf by running the following command:

    ```sh
    python3 -m pip install wh-m2p
    ```

Congratulations, you can now use md2pdf by running the following:

```sh
m2p
```

OR

```sh
python3 -m md2pdf
```
