# Babel Web

![enonce](images/enonce.png)

```bash
$ dirb http://challenges2.france-cybersecurity-challenge.fr:5001/ -X .php

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Apr 24 19:07:17 2020
URL_BASE: http://challenges2.france-cybersecurity-challenge.fr:5001/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
EXTENSIONS_LIST: (.php) | (.php) [NUM = 1]

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://challenges2.france-cybersecurity-challenge.fr:5001/ ----
+ http://challenges2.france-cybersecurity-challenge.fr:5001/flag.php (CODE:200|SIZE:0)                                                                                                                                                    
+ http://challenges2.france-cybersecurity-challenge.fr:5001/index.php (CODE:200|SIZE:238)                                                                                                                                                 
                                                                                                                                                                                                                                          
-----------------
END_TIME: Fri Apr 24 19:10:50 2020
DOWNLOADED: 4612 - FOUND: 2
```

flag: `FCSC{}`