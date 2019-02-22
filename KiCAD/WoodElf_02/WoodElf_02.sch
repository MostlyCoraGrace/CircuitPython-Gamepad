EESchema Schematic File Version 4
LIBS:WoodElf_02-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L WoodElf_01:Kailh_RGB_Switch S1
U 1 1 5C418754
P 6300 3150
F 0 "S1" H 6275 3637 60  0000 C CNN
F 1 "Kailh_RGB_Switch" H 6275 3531 60  0000 C CNN
F 2 "WoodElf_Lib:SW_Cherry_MX1A_1.00u_PCB" H 6300 3150 60  0001 C CNN
F 3 "" H 6300 3150 60  0001 C CNN
	1    6300 3150
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:WS2811 C1
U 1 1 5C4187B9
P 7750 3250
F 0 "C1" H 7750 3597 60  0000 C CNN
F 1 "WS2811" H 7750 3491 60  0000 C CNN
F 2 "WoodElf_Lib:WS2811" H 7750 3400 60  0001 C CNN
F 3 "" H 7750 3400 60  0001 C CNN
	1    7750 3250
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:Kailh_HotSwap_SwitchMount H1
U 1 1 5C418846
P 6100 2500
F 0 "H1" H 6100 2725 50  0000 C CNN
F 1 "Kailh_HotSwap_SwitchMount" H 6100 2634 50  0000 C CNN
F 2 "WoodElf_Lib:Kailh_HotSwap_Socket" H 6100 2500 50  0001 C CNN
F 3 "" H 6100 2500 50  0001 C CNN
	1    6100 2500
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D1
U 1 1 5C498866
P 7100 2950
F 0 "D1" H 7100 3215 50  0000 C CNN
F 1 "DIODE" H 7100 3124 50  0000 C CNN
F 2 "Diode_SMD:D_2010_5025Metric_Pad1.52x2.65mm_HandSolder" H 7100 2950 50  0001 C CNN
F 3 "~" H 7100 2950 50  0001 C CNN
	1    7100 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 2500 6850 2500
Wire Wire Line
	6850 2500 6850 2950
Wire Wire Line
	6850 2950 6800 2950
Wire Wire Line
	6850 2950 6900 2950
Connection ~ 6850 2950
Wire Wire Line
	5750 2950 5700 2950
Wire Wire Line
	5700 2950 5700 2600
Wire Wire Line
	5700 2600 5750 2600
Wire Wire Line
	7300 2950 7300 2500
Wire Wire Line
	5700 2600 5700 2500
Wire Wire Line
	5700 2500 5150 2500
Connection ~ 5700 2600
Wire Wire Line
	6050 3600 5450 3600
Wire Wire Line
	8200 3350 8300 3350
Wire Wire Line
	8300 3350 8300 3550
Wire Wire Line
	8300 3550 8800 3550
Wire Wire Line
	8200 3150 8200 3050
Wire Wire Line
	8200 3050 8800 3050
Wire Wire Line
	7300 2500 8800 2500
NoConn ~ 8200 3250
$Comp
L WoodElf_01:BlankThrough-Hole VDD1
U 1 1 5C699DC5
P 9300 3050
F 0 "VDD1" H 9250 3200 50  0000 L CNN
F 1 "BlankThrough-Hole" H 8950 2950 50  0000 L CNN
F 2 "WoodElf_Lib:BlankThrough-Hole" H 9300 3050 50  0001 C CNN
F 3 "" H 9300 3050 50  0001 C CNN
	1    9300 3050
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:BlankThrough-Hole SWIN1
U 1 1 5C699EEB
P 4850 2500
F 0 "SWIN1" H 4800 2650 50  0000 L CNN
F 1 "BlankThrough-Hole" H 4500 2400 50  0000 L CNN
F 2 "WoodElf_Lib:BlankThrough-Hole" H 4850 2500 50  0001 C CNN
F 3 "" H 4850 2500 50  0001 C CNN
	1    4850 2500
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:BlankThrough-Hole SWO1
U 1 1 5C69A5F3
P 9300 2500
F 0 "SWO1" H 9250 2650 50  0000 L CNN
F 1 "BlankThrough-Hole" H 8950 2400 50  0000 L CNN
F 2 "WoodElf_Lib:BlankThrough-Hole" H 9300 2500 50  0001 C CNN
F 3 "" H 9300 2500 50  0001 C CNN
	1    9300 2500
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:BlankThrough-Hole DIN1
U 1 1 5C69A757
P 9250 3550
F 0 "DIN1" H 9200 3700 50  0000 L CNN
F 1 "BlankThrough-Hole" H 8900 3450 50  0000 L CNN
F 2 "WoodElf_Lib:BlankThrough-Hole" H 9250 3550 50  0001 C CNN
F 3 "" H 9250 3550 50  0001 C CNN
	1    9250 3550
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:BlankThrough-Hole DO1
U 1 1 5C69A78B
P 9050 3950
F 0 "DO1" H 9000 4100 50  0000 L CNN
F 1 "BlankThrough-Hole" H 8700 3850 50  0000 L CNN
F 2 "WoodElf_Lib:BlankThrough-Hole" H 9050 3950 50  0001 C CNN
F 3 "" H 9050 3950 50  0001 C CNN
	1    9050 3950
	1    0    0    -1  
$EndComp
$Comp
L WoodElf_01:BlankThrough-Hole GND1
U 1 1 5C69B783
P 4900 4100
F 0 "GND1" H 4850 4250 50  0000 L CNN
F 1 "BlankThrough-Hole" H 4550 4000 50  0000 L CNN
F 2 "WoodElf_Lib:BlankThrough-Hole" H 4900 4100 50  0001 C CNN
F 3 "" H 4900 4100 50  0001 C CNN
	1    4900 4100
	1    0    0    -1  
$EndComp
Text Label 5450 3600 0    50   ~ 0
USB
Text Label 9150 3050 2    50   ~ 0
USB
Text Label 8800 3050 0    50   ~ 0
USB
Wire Wire Line
	8200 3450 8200 3950
Wire Wire Line
	8200 3950 8600 3950
Text Label 8800 2500 0    50   ~ 0
SWO
Text Label 9150 2500 2    50   ~ 0
SWO
Text Label 8800 3550 0    50   ~ 0
DIN
Text Label 9100 3550 2    50   ~ 0
DIN
Text Label 8900 3950 2    50   ~ 0
DO
Text Label 8600 3950 0    50   ~ 0
DO
Text Label 5200 4100 2    50   ~ 0
GND
Text Label 4750 4100 2    50   ~ 0
GND
Text Label 5150 2500 2    50   ~ 0
SWIN
Text Label 4700 2500 2    50   ~ 0
SWIN
Wire Wire Line
	5200 4100 6800 4100
Wire Wire Line
	6800 4100 6800 3450
Wire Wire Line
	6800 3450 7300 3450
Wire Wire Line
	6450 3800 6700 3800
Wire Wire Line
	6700 3800 6700 3150
Wire Wire Line
	6700 3150 7300 3150
Wire Wire Line
	6600 3600 6600 3250
Wire Wire Line
	6600 3250 7300 3250
Wire Wire Line
	6450 3600 6600 3600
Wire Wire Line
	6450 3400 6550 3400
Wire Wire Line
	6550 3400 6550 3350
Wire Wire Line
	6550 3350 7300 3350
$Comp
L WoodElf_01:LED_ARGB L1
U 1 1 5C705190
P 6250 3600
F 0 "L1" H 6250 3133 50  0000 C CNN
F 1 "LED_ARGB" H 6250 3224 50  0000 C CNN
F 2 "LED_SMD:LED_Cree-PLCC4_2x2mm_CW" H 6250 3550 50  0001 C CNN
F 3 "~" H 6250 3550 50  0001 C CNN
	1    6250 3600
	-1   0    0    1   
$EndComp
$EndSCHEMATC
