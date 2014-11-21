#!/bin/sh
#------------------------------------------------------------
# Creacio dels tunels contra GuifiBaix per Gestio del node
#------------------------------------------------------------

# Dades a modificar
BPORT_HTTP=11180  # Port remot per accedir al entorn web Luci
BPORT_SSH=11122   # Port remot per accedir vía ssh


# -------------------------------------------------------------
# No modificar res d'aqui cap al final
# -------------------------------------------------------------
BADDR=10.1.40.14

# LOCAL: A donde queremos acceder en realidad
LADDR=127.0.0.1
LPORT_SSH=22
LPORT_HTTP=80

# SERVER: La connexion ssh que nos permite hacer el tunel
SPORT=2222
SUSER=tunel
SADDR=tunel.guifibaix.coop

log() {
	echo "$(date -Is)" - "$*"
}

checkTunnel() {
	SERVICE=$1
	LPORT=$2
	BPORT=$3

	# Controlem si els procesos dels tunels son funcionant. Si no, els tornem a llençar.
	pgrep -f "$BADDR:$BPORT:$LADDR:$LPORT" > /dev/null 2>&1 && log "SSH Tunnel is UP, no action taken" && return

	log "$SERVICE Tunnel is DOWN, relaunching it..."

	/usr/bin/ssh -K 60 -I 1200 -i /etc/dropbear/dropbear_rsa_host_key -f -g -N -p "$SPORT" "$SUSER@$SADDR" -R "$BADDR:$BPORT:$LADDR:$LPORT"

	if [ $? -eq 0 ]; then
		log "Tunnel for $SERVICE Service to $SADDR created successfully"
	else
		log "An error occurred creating a $SERVICE tunnel to $SADDR, return code was $?"
	fi
}

log "Checking tunels..."
checkTunnel SSH $LPORT_SSH $BPORT_SSH
checkTunnel HTTP $LPORT_HTTP $BPORT_HTTP



