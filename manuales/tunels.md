# Com accedir als dispositius darrera d'una antena


Si volem fer servir un dispositiu que està darrera d'una antena wifi,
ho podem fer mitjançant un tunel SSH, sempre  que tinguem accés SSH a l'antena.

Si l'antena tingués IP 10.1.49.6 a la xarxa qMp,
i l'element intern accessible des de l'antena es 172.30.0.20,
el tunel es crea així:

	$ ssh -N -L 4906:172.30.0.20:80 root@10.1.49.6

> L'opció -N fa que no s'obri un shell com pasaría amb un ssh normal.
> Tanquem el túnel fent Control+C.

En aquest cas, apuntant el navegador a http://localhost:4106 entrem al port 80 del dispositiu intern.
S'en diu un tunnel local perque el port per accedir el tunel esta en localhost.

## Tunnels remot

Un tunnel remot serveix per crear un tunel cap a la maquina on estas.
Es ideal per fer visible una maquina al teu 
Obrir un port en una màquina accessible que sigui un tunel cap al port local que vulguis.






