{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # description: \
from earsketch import *\
\
setTempo(120)\
#Main synth loud\
Synth1 = EIGHT_BIT_ATARI_PAD_002\
Synth2 = EIGHT_BIT_ATARI_PAD_003\
\
for measure in range (1, 17, 2):\
    if measure % 4 == 1:\
     fitMedia (Synth1,1,measure,measure+2)\
    else:    \
     fitMedia (Synth2,2,measure,measure +2)\
    \
# Main synth pt.2.\
fitMedia(EIGHT_BIT_ATARI_PAD_002,9,17,19)\
fitMedia(EIGHT_BIT_ATARI_PAD_003,10,19,21)\
fitMedia(EIGHT_BIT_ATARI_PAD_002,9,21,23)\
fitMedia(EIGHT_BIT_ATARI_PAD_003,10,23,25)\
fitMedia(EIGHT_BIT_ATARI_PAD_002,9,25,27)\
fitMedia(EIGHT_BIT_ATARI_PAD_003,10,27,29)\
#Percussion section below\
#kick drums below\
fitMedia(MILKNSIZZ_BOSSA_CLUBA_KICK, 3, 5, 50)\
# high hat time \
fitMedia (MILKNSIZZ_NORTENA_HI_HAT, 4,9,37)\
\
#claps\
for measure in range (9,21,2):\
 fitMedia(AK_UNDOG_CLAPS_SNAPS_4, 11, measure, measure + 1)\
for measure in range (21,24,1):\
 fitMedia(AK_UNDOG_CLAPS_SNAPS_4, 11, measure, measure + 2)\
for measure in range (26,37,2):\
 fitMedia(AK_UNDOG_CLAPS_SNAPS_4, 11, measure, measure + 1)\
for measure in range (38,43,1):\
 fitMedia(AK_UNDOG_CLAPS_SNAPS_4, 11, measure, measure + 2)\
for measure in range (45,48,2):\
 fitMedia(AK_UNDOG_CLAPS_SNAPS_4, 11, measure, measure + 1)\
\
#All of the vocals will be below here\
#backing vocals\
fitMedia (AK_UNDOG_OOHS_2, 5,13,29)\
fitMedia (AK_UNDOG_OOHS_2, 5,37,41)\
#Main vocals\
fitMedia(AK_UNDOG_OOHS_1,6,13,21)\
fitMedia(AK_UNDOG_OOHS_1,6,25,29)\
fitMedia(AK_UNDOG_OOHS_1,6,33,37)\
#trying to layer more vocals in now a.k.a choir\
fitMedia(AK_UNDOG_OOHS_AHHS_4,8,21,49)\
\
\
#String section below\
#building it out with bass\
fitMedia(AK_UNDOG_BASS_3,7,17,29)\
fitMedia (IRCA_BOMBA_SICA_ELEC_PIANO,12,29,49)\
\
\
#effects\
setEffect(9,VOLUME,GAIN,-17.0)\
setEffect(10,VOLUME,GAIN,-17.0)\
setEffect(6,VOLUME,GAIN,3)\
setEffect(8,VOLUME,GAIN,2)\
setEffect(4,VOLUME,GAIN,3)\
setEffect(5,VOLUME,GAIN,3)\
setEffect(11,VOLUME,GAIN,-8)\
setEffect(7,VOLUME,GAIN,5)\
}