# Installing Compiz On Kali

### Step 1: 

`sudo <text-editor-of-your-choice> /etc/apt/sources.list`

I use `vim`, thus 

```bash
sudo vim /etc/apt/sources.list
```

### Step 2

Add this '**deb http://ftp.us.debian.org/debian/ sid main non-free contrib**' to the repository

```
# For information about how to configure apt package sources,
 11 # see the sources.list(5) manual.
 12 deb http://http.kali.org/kali kali-rolling main contrib non-free
 13 deb http://ftp.us.debian.org/debian/ sid main non-free contrib

```

### Step 3

```bash
sudo apt-get update
apt-get -t sid install compiz
```



####  Step 4

Congratulations, you have successfully installed compiz

