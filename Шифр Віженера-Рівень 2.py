from collections import Counter
import re

def find_repeating_sequences(text, sequence_length):
    sequences = {}
    for i in range(len(text) - sequence_length):
        seq = text[i:i + sequence_length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    return {seq: positions for seq, positions in sequences.items() if len(positions) > 1}

def calculate_distances(positions):
    distances = []
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            distances.append(abs(positions[j] - positions[i]))
    return distances

def find_possible_key_lengths(distances):
    gcd_counts = Counter()
    for distance in distances:
        for i in range(1, int(distance ** 0.5) + 1):
            if distance % i == 0:
                gcd_counts[i] += 1
                if i != distance // i:
                    gcd_counts[distance // i] += 1
    return gcd_counts.most_common(5)

def kasiski_examination(text, sequence_length=3):
    text = re.sub(r'[^A-Z]', '', text.upper())
    sequences = find_repeating_sequences(text, sequence_length)
    distances = []
    for positions in sequences.values():
        distances.extend(calculate_distances(positions))
    possible_key_lengths = find_possible_key_lengths(distances)
    return possible_key_lengths

# Використання методу Касіскі на запропонованому зашифрованому тексті
cipher_text = "WZD UGAATK HV TXY IKEQBOU OV QLSVKQEXD KBXUYT. TR RUQTGD QZT SNT RVFCUHL MGU PYMIIB LL QMI'L QQM. TXY IKIKQB AS BT PHE BCF KMPULMQBD ANKI GFPKPDU MQHCLK EZ C NUR TSUUZHCD XCH ANFZDVLHEH VX RMZXMHVPA MHYVFV. KBT ZIWPDVM, UH MHU LRPDIO, XPHU RX SMXAACYAM AS U TGDU OH ZLODHAPWZZSZY. IOGTU WKG VCCK VWTY EDQHXUYT QN TDQPIPXVB TKANWN GKE KOUKUFO DAUXWUW AUCCN CXHRPANW. AZII HV Z ZPBDU. TKGSU MOG VQNF AUUKAAFLT PWZDCCNL YV DWZLOXMNM BGLFFI PYW KPD UUBOXCSUUL. XOH IOWTU TKWRU XZ HEXD. TXYO SSU TKW UFTIM KW ZZOC QLSVKQEXD KBXUYT UDCF EHAF BUHUWR. OWLKE QS FO NKIZ KPHQY QN G NEZZO OH PU ICUOUSL VDVC. IORCS UGL XUTL PRYOILF, WR TZTFO PSYBTGF. OWGM YA CDL. IOW DQNGMDUHIO-CUVTXKY XXZDIAM RX HYPSATC HV TXY YSGU OH BQFXHSO ADGANW WPL EEN XZSY PF Q FOSSI. AZE VHQWTUYCAZ-SMNWNRP SPLMYSD GE MDTSOKQBLLM CH MHU RCYD IU UABQACF DII LEUQNI GYN VPO NZEW YH G GBHSV. KBT EPHHL DHVY VX CHN XOHGH HAHB RX KBT LVRQDEM CUIAWS WE MGU PYMIIB, TUK IOW CWRCDHKT VX QZT UODNXZMT QN MGU ELKFUKT NSU DM AD HPHDHZTIM CMCLNM. CV AHBHVM TYHPKEI TR PHILL ADGTKANW. LOED TKANWN AZAK ZUW KMKL CQV DW FMDCWD. NR ZHOXZM XHS WTXCRGD IGMSSTXCTZ. QV GMGYWPS TPUPCMGP XU AD ZUMHIO PL QV XFPQMSVFARTD EZDHTYATC OH SKTAL. DW CKTYNI AT MVGK CIGHAD. TKW QMIPLU KZQ DOKGLLT MVGKYKBXUY. BGRNFXO GFD TZQYUQAT SSU TR TXY GKUYAT ANIOGBEEDBS GE UC SSK. YABU PUV MQRWND UGL UE TKW QMIPLU UZWWRYUAZ FEZ CF QMI. FHWM MGU EVAOK OH VYYM GF NOUE, OWL UPXD GE UAS UXM CKTI XZ UXM CKT IU MHU MXLHSCPU. VZOP TXY WGIDB RX MCTD PV EGWLYHV, UXM CUTEM'Z CHHEW HI IOW KGPG. QFA SSK HV ZK DUUE AUUXZSY GFD AYPTOB. AZPIM ZZO AD TEDMZWZ KBT LVHNZEW TI ZG QB WZDYM WWSYT. MGENT PHE RGSC OWL TPUARD TI ZG QB WZDYM WWSYT. AT CH MHU SSWBKUIVK, HNF NEO SAFU, WZZK PYM HMZODY GXYKPHA. VHMYGZAUP OH OFCCPGO HARNT U DGSA OH ZHO ZZPNA WZZK IOW NWRN HI CLP, KOPHLUS, OIKHL. WXYC USYBHEL TCHGYSUM WZD UGAATK HV HD PIUPHL ZATX WPETUTE. WU RGF VWRIAVU P EAD ERK CUZPFG H XLDVPA MHYVF SS FDUY QA KW TITZ OEB CVMYMT AU. TKW EHAF EOKUVW VIG EAAQNI Z PHLDEIA WZHDA PL KPZW ODY GVNYZDV HK XUMEDADOR. UAS AHB LL GPXAW LADOWSI."
possible_key_lengths = kasiski_examination(cipher_text)

print("Можлива довжина ключа по методу Касіскі:")
for length, count in possible_key_lengths:
    print(f"Length: {length}, Count: {count}")