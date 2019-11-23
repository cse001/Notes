# List of Forensic Tools and methods 

This is how to create a dd of a loaded drive for data recovery

```bash
sudo dcfldd if=/dev/sdb of=/home/pi/usb.dd
```

Another way is to grep the required file from a block device 

```bash
grep -a '[a-z0-9]\{32\}' /dev/sdb
```

We did this to get all the strings of length 32 since we know the requirements. 

We can also get lines above and below in the following way 

```bash
grep -a -A2 -B2 '[a-z0-9]\{32\}' /dev/sdb
```

This gets us 2 lines after and 2 lines before the matched pattern



### Other tools used

1. Strings 
2. xxd  {This is a hex editor} can be combined with grep
3. The above grep method
4. binwalk
5. dcfldd
6. dd
7. testdisk
8. photorec







