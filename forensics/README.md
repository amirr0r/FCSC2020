# Forensic

```bash
root@kali:/usr/share/volatility/tools/linux $ apt install build-essential dwarfdump
root@kali:/usr/share/volatility/tools/linux $ make
root@kali:/usr/share/volatility/tools/linux $ zip Kali2020.zip module.dwarf /boot/System.map-5.4.0-kali4-amd64 
  adding: module.dwarf (deflated 91%)
  adding: boot/System.map-5.4.0-kali4-amd64 (deflated 79%)
root@kali:/usr/share/volatility/tools/linux $ cp Kali2020.zip /usr/lib/python2.7/dist-packages/volatility/plugins/linux/
root@kali:/usr/share/volatility/tools/linux $ volatility --info | grep Kali
Volatility Foundation Volatility Framework 2.6
LinuxKali2020x64      - A Profile for Linux Kali2020 x64
root@kali:/usr/share/volatility/tools/linux $ # test it
root@kali:/usr/share/volatility/tools/linux $ volatility -f dmp.mem --profile=LinuxKali2020x64 linux_bash
Volatility Foundation Volatility Framework 2.6
Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    1523 bash                 2020-03-26 23:24:18 UTC+0000   rm .bash_history 
    1523 bash                 2020-03-26 23:24:18 UTC+0000   exit
    1523 bash                 2020-03-26 23:24:18 UTC+0000   vim /home/Lesage/.bash_history 
    1523 bash                 2020-03-26 23:24:27 UTC+0000   ss -laupt
    1523 bash                 2020-03-26 23:26:06 UTC+0000   rkhunter -c
    1523 bash                 2020-03-26 23:29:19 UTC+0000   nmap -sS -sV 10.42.42.0/24
    1523 bash                 2020-03-26 23:31:31 UTC+0000   ?+??U
    1523 bash                 2020-03-26 23:31:31 UTC+0000   ip -c addr
    1523 bash                 2020-03-26 23:38:00 UTC+0000   swapoff -a
    1523 bash                 2020-03-26 23:38:05 UTC+0000   swapon -a
    1523 bash                 2020-03-26 23:40:18 UTC+0000   ls
    1523 bash                 2020-03-26 23:40:23 UTC+0000   cat LiME.txt 
    1523 bash                 2020-03-26 23:40:33 UTC+0000   cd LiME/src/
    1523 bash                 2020-03-26 23:40:54 UTC+0000   
    1523 bash                 2020-03-26 23:40:54 UTC+0000   insmod lime-5.4.0-4-amd64.ko "path=/dmp.mem format=lime timeout=0"
```

## Liens utiles

- https://adel-allam.fr/ctf/2019/07/23/forensic.html#linux