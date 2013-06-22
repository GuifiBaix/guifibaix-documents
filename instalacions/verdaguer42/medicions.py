#!/usr/bin/python
# -*- coding: utf-8 -*- 

# Estado de mediciones de Verdaguer 42
# Distancias en m

AntenaTerradillo = 2.00 # Distancia de la antena hasta el suelo del terradillo
AltoCornisa = .50 # Grosor de la cornisa
VoladoCornisa = .20 # La parte de la cornisa del tejadillo que esta volada más allá de la pared
AntenaCornisa = AntenaTerradillo + AltoCornisa + VoladoCornisa # 2.70   # Distancia para llegar de la antena al interior de la cornisa
CasetaLadoPatio = 5.10 # Longitud de la pared de la caseta que está dando al patio.
EsquinaPuertaACaja = 1.25 # Longitud de la caja a la esquina de la caseta mas cercana.
EsquinaAntenaACajaPorCornisa = CasetaLadoPatio - EsquinaPuertaACaja # 3.75
VerticalCornisaACajaPatio = 1.60 # Distancia vertical de la cornisa a la caja estanca del patio
AntenaACajaPatio = AntenaCornisa + EsquinaAntenaACajaPorCornisa + VerticalCornisaACajaPatio # 8.15
print "Cable de la antena a la caja del patio:", AntenaACajaPatio

GrosorMuroPatio = 0.17
CajaPatioABajada = 1.40 # Distancia de la esquina de la caja a el punto de bajada vertical
AlturaDelMuroDelPatioRespectoElPrimerBalcon = 1.20 #
MinimoALaVertical = GrosorMuroPatio + CajaPatioABajada + AlturaDelMuroDelPatioRespectoElPrimerBalcon # 2.80

AlturaEntrePisos = 2.85
HorizontalAVentana1o = 1.10
VerticalAVentana1o = 2.00
GrosorParedVentana = 0.20
PatioAncho = 4.00 #
PatioLargo = 3.40 #

AcometidaPatio1o = VerticalAVentana1o + HorizontalAVentana1o + GrosorParedVentana
AcometidaPatio4o = VerticalAVentana1o + PatioLargo + PatioAncho + GrosorParedVentana

print "Cable de la caja al 4o 4a:", MinimoALaVertical + AcometidaPatio4o + 0 * AlturaEntrePisos
print "Cable de la caja al 4o 1a:", MinimoALaVertical + AcometidaPatio1o + 0 * AlturaEntrePisos
print "Cable de la caja al 3o 4a:", MinimoALaVertical + AcometidaPatio4o + 1 * AlturaEntrePisos
print "Cable de la caja al 3o 1a:", MinimoALaVertical + AcometidaPatio1o + 1 * AlturaEntrePisos
print "Cable de la caja al 2o 4a:", MinimoALaVertical + AcometidaPatio4o + 2 * AlturaEntrePisos
print "Cable de la caja al 2o 1a:", MinimoALaVertical + AcometidaPatio1o + 2 * AlturaEntrePisos
print "Cable de la caja al 1o 4a:", MinimoALaVertical + AcometidaPatio4o + 3 * AlturaEntrePisos
print "Cable de la caja al 1o 1a:", MinimoALaVertical + AcometidaPatio1o + 3 * AlturaEntrePisos
print "Cable de la caja al local:", MinimoALaVertical + AcometidaPatio4o + 4 * AlturaEntrePisos
print "Cable de la caja al bj 1a:", MinimoALaVertical + AcometidaPatio1o + 4 * AlturaEntrePisos

print "Total cable para el patio:", 10*MinimoALaVertical + 5*AcometidaPatio1o + 5*AcometidaPatio4o + 20*AlturaEntrePisos + AntenaACajaPatio

CasetaParedVerdaguer = 5.10
CasetaEsquinaVerdagerTorresABarra = 1.60
BarraTramoHorizontal = 4.50
BarraTramoVertical = 0.66
AntenaACajaFachada = CasetaParedVerdaguer + CasetaEsquinaVerdagerTorresABarra + BarraTramoHorizontal + BarraTramoVertical

print "Cable de la antena a la caja de la fachada", AntenaACajaFachada

GrosorMuroFachada = 0.30
FachadaHastaElPrimerBalcon = 1.58
BalconABalcon = 0.30 + 0.90 + 5.80 + 0.90 + 0.30
TechoBalcon = 2.90 # Curandonos en salud atraversar todo el balcon
TechoBalconApuntoDeEntrada = 2.60
ParedFachada = 0.30 # Atravesar la pared para entrar en el domicilio
Comun2os = BalconABalcon + GrosorMuroFachada + FachadaHastaElPrimerBalcon + TechoBalcon + TechoBalconApuntoDeEntrada
Comun3os = GrosorMuroFachada + FachadaHastaElPrimerBalcon + TechoBalcon + TechoBalconApuntoDeEntrada

print "Cable de la caja al 4o 2a:", Comun2os + 0*AlturaEntrePisos
print "Cable de la caja al 4o 3a:", Comun3os + 0*AlturaEntrePisos
print "Cable de la caja al 3o 2a:", Comun2os + 1*AlturaEntrePisos
print "Cable de la caja al 3o 3a:", Comun3os + 1*AlturaEntrePisos
print "Cable de la caja al 2o 2a:", Comun2os + 2*AlturaEntrePisos
print "Cable de la caja al 2o 3a:", Comun3os + 2*AlturaEntrePisos
print "Cable de la caja al 1o 2a:", Comun2os + 3*AlturaEntrePisos
print "Cable de la caja al 1o 3a:", Comun3os + 3*AlturaEntrePisos
print "Cable de la caja al local 2a:", Comun2os + 4*AlturaEntrePisos
print "Cable de la caja al local 3a:", Comun3os + 4*AlturaEntrePisos

print "Total cable para fachada:", 5* Comun3os + 5 * Comun2os + 20*AlturaEntrePisos






