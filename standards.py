class Compound:
    def __init__(self, poolset, typeset):
        self.pool = poolset
        self.type = typeset


iStandards = {
 'Alanine': 4.9973323200599,
 'Arginine': 4.9973323200599,
 'Asparagine': 4.9973323200599,
 'Aspartate': 4.9973323200599,
 'Carnitine': 4.9973323200599,
 'Citrulline': 4.9973323200599,
 'Cystine': 4.9973323200599,
 'Glutamate': 4.9973323200599,
 'Glutamine': 4.9973323200599,
 'Glycine': 4.9973323200599,
 'Histidine': 4.9973323200599,
 'Hydroxyproline': 4.9973323200599,
 'Isoleucine': 4.9973323200599,
 'Leucine': 4.9973323200599,
 'Lysine': 4.9973323200599,
 'Methionine': 4.9973323200599,
 'Ornithine': 4.9973323200599,
 'Phenylalanine': 4.9973323200599,
 'Proline': 4.9973323200599,
 'Serine': 4.9973323200599,
 'Taurine': 4.9973323200599,
 'Threonine': 4.9973323200599,
 'Tryptophan': 4.9973323200599,
 'Tyrosine': 4.9973323200599,
 'Valine': 4.9973323200599,
 'Lactate': 4.9973323200599,
 'Glucose': 4.9973323200599,

 '2-hydroxybutyric-acid': 5.03371238789826,
 '2-hydroxybutyrate': 5.03371238789826,
 '2-hb': 5.03371238789826,
 '2-HB': 5.03371238789826,
 '2-aminobutyric-acid': 4.89745241834741,
 '2-aminobutyrate': 4.89745241834741,
 'AMP': 5.11475870671235,
 'Argininosuccinate': 5.4982796774196,
 'Betaine': 5.20181643450854,
 'Biotin': 5.0009674869335,
 'Carnosine': 5.20583900447515,
 'Choline': 5.26063705657136,
 'CMP': 4.99977889657934,
 'Creatine': 5.73630755282233,
 'Cytidine': 5.01095359923515,
 'dTMP': 5.14194908918635,
 'Fructose': 5.63733670609336,
 'Glucose-1-phosphate': 2.37819470020133,
 'Glutathione': 4.83430741321902,
 'GMP': 4.79076702775531,
 'IMP': 4.9547551940203,
 'O-phosphoethanolamine': 6.77246148542287,
 'Pyridoxal': 5.68687607201649,
 'Thiamine': 5.39395319822864,
 'trans-Urocanate': 4.74708085511279,
 'Trans-Urocanate': 4.74708085511279,
 'trans-urocanate': 4.74708085511279,
 'UMP': 5.02485964323421,
 'Xanthine': 4.69547267577355,
 'gsh': 4.834307413,

 '3-hydroxybutyric-acid': 6.56063790844972,
 '3-hydroxybutyrate': 6.56063790844972,
 '3-hb': 6.56063790844972,
 '3-HB': 6.56063790844972,
 'Acetylalanine': 6.48239580378873,
 'Acetylaspartate': 6.5016100832747,
 'Acetylcarnitine': 6.32225449097143,
 'Acetylglutamine': 6.217089090769,
 'ADP': 6.08133629016981,
 'Allantoin': 5.7690563204682,
 'CDP': 6.22859708578781,
 'CDP-choline': 6.21968459917267,
 'Coenzyme-A': 0.266189623415126,
 # 'Coenzyme A': 0.266189623415126,
 'CoA': 0.266189623415126,
 'Coa': 0.266189623415126,
 'Creatinine': 6.08392474902252,
 'gamma-aminobutyric-acid': 6.28916773673274,
 'gamma-aminobutyrate': 6.28916773673274,
 'GDP': 1.86226634424516,
 'Glutathione-disulfide': 6.16402250105486,
 'Glycerate': 6.12355335674695,
 'Hypoxanthine': 6.06841626513394,
 'Myo-Inositol': 6.00659351922984,
 'myo-inositol': 6.00659351922984,
 'NAD+': 6.28488430272438,
 'NAD': 6.28488430272438,
 'p-aminobenzoate': 5.96832154504145,
 'p-Aminobenzoate': 5.96832154504145,
 'P-aminobenzoate': 5.96832154504145,
 'p-Aminobenzoate': 5.96832154504145,
 'PABA': 5.96832154504145,
 'Phosphocholine': 6.65384896797157,
 'Sorbitol': 5.8580049819876,
 'UDP': 3.11617564423192,
 'UDP-glucose': 4.30509468476358,
 'UDP-Glucose': 4.30509468476358,

 'Phenylacetylglutamine': 6.81937018127754,
 'Acetylglutamate': 6.27209601415435,
 'Acetylglycine': 6.02705430204503,
 'Acetylmethionine': 5.22107355914313,
 'Asymmetric dimethylarginine': 5.55851202965197,
 'ATP': 5.17765379787911,
 'CTP': 4.37907508244845,
 'dATP': 2.93064582646428,
 'dCTP': 1.92012974473456,
 'Deoxycytidine': 5.91817773787924,
 'Folic acid': 4.45022751515758,
 'Folate': 4.45022751515758,
 'GTP': 0.664577069553957,
 'Hypotaurine': 5.14586792835667,
 'Methionine sulfoxide': 4.15514585262757,
 'Methylthioadenosine': 5.00481166218895,
 'Phosphocreatine': 4.74455307053837,
 'Pyridoxine': 6.01891256794748,
 'Ribose-5-phosphate': 5.91520712752139,
 'SAH': 4.42772913509151,
 'Thymidine': 4.66196277763184,
 'Trimethyllysine': 4.35056308333532,
 'Uridine': 4.77641590500994,
 'UTP': 5.68472798702442,

 '3-phosphoglycerate': 5.57472131952464,
 '3-PG': 5.57472131952464,
 'Cis-aconitic-acid': 5.80174278010217,
 'Cis-aconitate': 5.80174278010217,
 'Citrate': 5.90141906570882,
 'DHAP': 5.56560284692072,
 'Fructose-1,6-bisphosphate': 5.48174545090222,
 'Fructose-1, 6-bisphosphate': 5.48174545090222,
 'Fructose-1-6-bisphosphate': 5.48174545090222,
 'Fumarate': 5.62061665044703,
 'Glucose-6-phosphate': 5.57511554222458,
 'Glycerol-3-phosphate': 5.33721255279593,
 'Guanidinoacetate': 5.81897514318511,
 'Kynurenine': 5.50671969712946,
 'Malate': 5.76598967178601,
 'NADP+': 5.33123052322962,
 'NADP': 5.33123052322962,
 'Niacinamide': 5.77526137101027,
 '2-oxoglutarate': 5.47020082348949,
 'A-Ketoglutaric-acid': 5.47020082348949,
 'A-Ketoglutarate': 5.47020082348949,
 'Akg': 5.47020082348949,
 'Phosphoenolpyruvate': 5.92250730443154,
 'Pyruvate': 4.87450282209293,
 'Succinate': 5.48602815869483,
 'Uracil ': 5.66239136209295,

 '3-hydroxyisobutyric-acid': 6.52080737407328,
 '3-hydroxyisobutyrate': 6.52080737407328,
 '2-hydroxyglutarate': 6.57580113121367,
 'Aminoadipate': 6.26147455331714,
 'beta-alanine': 6.33421352719945,
 'Carbamoylaspartate': 6.64163904460056,
 'Cystathionine': 6.47370481431716,
 'Cysteic-acid': 5.7663654922986,
 'FAD': 2.80689234345067,
 'Glycerophosphocholine': 6.68363051131634,
 'Inosine': 6.2839127524751,

 'Orotate': 6.37030853556671,
 'Orotic-acid': 6.37030853556671,
 'Pantothenate': 6.16428231735162,
 'Pantothenic-acid': 6.16428231735162,
 'Phosphoserine': 6.72461683781487,
 'Riboflavin': 6.48423388378493,
 'UDP-GlcNAc': 1.56075172997463,
 'Uric acid': 3.40670961125,
 'Uric-acid': 3.40670961125,
 'Urate': 3.40670961125,

 'Itaconic-acid': 5.08007558404486,
 'Itaconate': 5.08007558404486,
 'Homocysteine': 4.99275824856602,
 '2-oxobutyric-acid': 5.1615509544801,
 'Ascorbate': 4.83667504704076,
 'Ascorbic-Acid': 4.83667504704076,
 'Sarcosine': 5.48508277939468,
 'Dimethylglycine': 5.61728319933955,
 'N6-acetyllysine': 4.88067735117641,
 'Pipecolate': 5.1960231698648,
 'Indolelactate': 5.14808132889391,
 'Picolinate': 5.35809714062023,
 '3-methyl-2-oxobutyrate': 5.38627158334742,
 '3-methyl-2-oxopentanoic-acid': 4.94017517805416,
 'Formyl-methionine': 4.50686938856642,
 'Homocitrulline': 5.01697828201313,
 'Gamma-glutamyl-alanine': 4.76536675422449,
 'Mannose': 5.39647251340844,
 'Cysteine-glycine (dipeptide)': 4.91140125298772,
 'Cysteine-glycine': 4.91140125298772,
 'cys-gly': 4.91140125298772,

 # other:
 'Gaba': 6.289167737,
 'gssg': 6.164022501,
 'sah': 4.427729135,
 'S-adenosyl-l-homocysteine': 4.427729135,
 'Methionine-sulfoxide': 4.155145853,
 'Oxoglutarate': 5.47020082348949,
 '2HG': 6.575801131,
 '3-methyl-2-oxopentanoic-acid-ketoisoleucine': 4.940175178,
 '3-methyl-2-oxobutyrate-keto-isovaleric-acid': 5.386271583,
 'Pyroglutamate-5-oxoproline': 5.237401941,
 'gly-gly': 4.364989878,
 'Trans-urocanate': 4.747080855,
 'a-aminobutyrate': 4.897452418,
 'Asymmetric-dimethylarginine': 5.55851203,
 'Kynurinenine': 1865.211047903980,
 'Uracil': 152.149153954228,
 'AKB': 3.19503110738,
 'AHB': 146.69290684797,

 'asymmetric-dimethylarginin_1': 5.55851202965197,
 'asymmetric-dimethylarginin_2': 5.55851202965197,
 '3-methyl-2-oxopentanoic-ac_1': 4.94017517805416,
 '3-methyl-2-oxopentanoic-ac_2': 4.94017517805416,
 '3-methyl-2-oxopentanoic-acid': 4.94017517805416,
 '3-methyl-2-oxobutyrate-ket_3': 5.38627158334742,
 '3-methyl-2-oxobutyrate-ket_4': 5.38627158334742,
 '3-methyl-2-oxobutyrate-keto': 5.38627158334742,
 '3-methyl-2-oxobutyrate-ket_5': 5.38627158334742,
 '3-methyl-2-oxopentanoic-ac_1': 4.94017517805416,
 '3-methyl-2-oxopentanoic-ac_2': 4.94017517805416,
 '3-methyl-2-oxobutyrate-ket_3': 5.38627158334742,
 '3-methyl-2-oxobutyrate-ket_4': 5.38627158334742,
 '3-methyl-2-oxobutyrate-ket_5': 5.38627158334742,

}
