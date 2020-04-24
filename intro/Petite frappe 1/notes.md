# Petite frappe 1

![enonce](image/enonce.png)

```bash
$ cat petite_frappe_1.txt | grep -oE "KEY_.*" | cut -d ')' -f1 | sed 's/KEY_//' | tr -d '\n'
UUNNEEGGEENNTTIILLLLEEIINNTTRROODUDUCCTTIIOONN
$ cat petite_frappe_1.txt | grep -oE "KEY_.*" | cut -d ')' -f1 | sed 's/KEY_//' | uniq | tr -d '\n'
UNEGENTILEINTRODUDUCTION
```

flag: 
- `FCSC{UUNNEEGGEENNTTIILLLLEEIINNTTRROODUDUCCTTIIOONN}` ? **NON**
- `FCSC{UNEGENTILEINTRODUDUCTION}` ? **NON**
- `FCSC{UNEGENTILLEINTRODUCTION}` ? **YES**