```python
#!/usr/bin/python3
import sys
if len(sys.argv)==2:
    print ('Knock,knock',sys.argv[1])
else:
    sys.stderr.write('Usage: {0} <name> \n'.format(sys.argv[0]))
```

Note:

We do not need to specify the `\n` with print statements but `sys.stderr` is low level and thus the `\n` has to be specified.