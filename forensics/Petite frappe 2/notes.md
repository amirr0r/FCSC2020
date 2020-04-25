# Petite frappe 2

![enonce](images/enonce.png)


## Tentative 1

```bash
$ showkey -k # similaire au fichier petite_frappe_2.txt -> essayons de taper 'a' pour voir
kb mode was ?UNKNOWN?
[ if you are trying this under X, it might not work
since the X server is also reading /dev/console ]

press any key (program terminates 10s after last keypress)...
keycode  28 release
akeycode  30 press
keycode  30 release
keycode  97 press
^Ccaught signal 2, cleaning up...
$ xinput test 8 # similaire au fichier petite_frappe_2.txt -> essayons de taper 'a' pour voir
key release 36 
key press   38 
akey release 38 
key press   54 
ckey release 54 
key press   105 
key press   54 
^C
```

Ok donc      soit `38`.

```
$ for n in $(cat petite_frappe_2.txt | awk '{print $3}'); do node getKey.js $n; done > keys.txt
$ cat keys.txt | uniq | tr 'A-Z' 'a-z' | tr -d '\n'
LQSOLUTIONQVECXINPUTNESE;BLEPQSUPERPRQTIAUEQDEDECODER,LEFLQGESTUN8CLQVIER8QWERTY8EN8VQUT8DEUX
```

## Tentative 2

```
$ setxkbmap fr
$ cat petite_frappe_2.txt | python xinput-decoder.py | tr -d ' ' | sed 's/space/\ /g' | sed 's/underscore/_/g'
la solution avec xinput ne semble pas super pratique a decoderShift_Rsemicolon le flag est un_clavier_azerty_en_vaut_deux
```

flag: `FCSC{un_clavier_azerty_en_vaut_deux}`

## Liens utiles

- https://blog.rom1v.com/2011/11/keylogger-sous-gnulinux-enregistrer-les-touches-tapees-au-clavier/
- https://www.craoc.fr/articles/gestion-du-clavier-sous-gnu-linux/
- https://gist.github.com/rickyzhang82/8581a762c9f9fc6ddb8390872552c250