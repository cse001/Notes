# Hacker 101

## Heading 1

### Flag 0

I don't really remember

### Flag 1

So for this the first thing was to find a sub-directory on the page that would allow me to login as admin.

So using some tools I was able to get **login** as the  sub-directory.

After that we needed to brute-force for which the following command was used by me using Hydra

```bash
hydra challenge_instance_ip -s 5001 -L /path/to/list -p "password" http-post-form "/instance-number/login:username=^USER^&password=^PASS^:F=Invalid username" -v
```

After this I got the username as `nike`. Now I had to go looking for the password.

So I used the same command as above. 

```bash
hydra challenge_instance_ip -s 5001 -l "nike" -P /path/to/list http-post-form "/instance-number/login:username=^USER^&password=^PASS^:F=Invalid password" -v
```

The password was `rick`

This thing really took a lot of time. 

And there is only one person I can thank.

As soon as we login, We get the flag

## Flag 2

`^FLAG^006bbe21c75fb831004758d27a10aa9e2c350cf71dd8982f516afb653a20318b$FLAG$`

#### HInts 

````
Flag2 -- Found
Always test every input
Bugs don't always appear in a place where the data is entered
````

So after logging in, I was able to edit all the items 

I checked all the input fields. One by one. The price field was the one that was needed. 

The flag appears on the checkout field.