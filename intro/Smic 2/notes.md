![enonce](images/enonce.png)

Meme chose que pour **SMIC 1**, en allant sur ce [site](https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html), on trouve la formule suivante:

## Tentative 1

![formule](images/formule.png)

Par consequent, si on fait le calcul:

```bash
Python 3.8.2 (default, Apr  1 2020, 15:52:55) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> c = 63775417045544543594281416329767355155835033510382720735973
>>> n = 632459103267572196107100983820469021721602147490918660274601
>>> e = 65537
>>> 
>>> 
>>> m = (c ** e) % n
>>> m
25962168794090271209460257543802326200359078643230397438572
>>>
```

flag: `FCSC{25962168794090271209460257543802326200359078643230397438572}` ? **Non**

## Tentative 2

```bash
$ python3 /opt/RsaCtfTool/RsaCtfTool.py -n 632459103267572196107100983820469021721602147490918660274601 -e 65537 --uncipher 63775417045544543594281416329767355155835033510382720735973

[*] Testing key /tmp/tmprp6yt48m.
Can't load qicheng because sage is not installed
Can't load boneh_durfee because sage is not installed
Can't load ecm2 because sage is not installed
Can't load smallfraction because sage is not installed
Can't load ecm because sage is not installed
[*] Performing primefac attack on /tmp/tmprp6yt48m.
[*] Performing comfact_cn attack on /tmp/tmprp6yt48m.
[*] Performing mersenne_primes attack on /tmp/tmprp6yt48m.
[*] Performing smallq attack on /tmp/tmprp6yt48m.
[*] Performing noveltyprimes attack on /tmp/tmprp6yt48m.
[*] Performing partial_q attack on /tmp/tmprp6yt48m.
[*] Performing cube_root attack on /tmp/tmprp6yt48m.
[*] Performing pollard_p_1 attack on /tmp/tmprp6yt48m.
[*] Performing pastctfprimes attack on /tmp/tmprp6yt48m.
[*] Performing factordb attack on /tmp/tmprp6yt48m.

Results for /tmp/tmprp6yt48m:

Unciphered data :
b'Y\xcd?\x8cBo\xf5s*\x1b\xd0\x84\xe5\xa5\x99\xbd\x88\n=\xdd\x86Ho\x7f\x93'
```

[asecuritysite](https://asecuritysite.com/encryption/factors?n=1034776851837418228051242693253376923)

```
Factors
-------
1,034,776,851,837,418,228,051,242,693,253,376,923 = 952,809,000,096,560,291 x 1,086,027,579,223,696,553
```

## Liens utiles

- https://sidsbits.com/RSA-Tool/
- https://medium.com/asecuritysite-when-bob-met-alice/cracking-rsa-a-challenge-generator-2b64c4edb3e7