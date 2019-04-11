1. `private.pem` which is a *private RSA key*.
2. `flag.end` which is an *encoded RSA file*.

we use `rsautl` from `openssl` in command line:

```shell
$ openssl rsautl -decrypt -inkey private.pem -in flag.enc
FLAG-vOAM5ZcReMNzJqOfxLauakHx
```

