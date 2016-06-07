from math import sqrt

#https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement/blob/master/MELA/src/Mela.cc#L307
CJLSTg4decay_mix = 2.521
CJLSTg2decay_mix = 1.638
CJLSTg1prime2decay_mix = 12046.01

#https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement/blob/master/MELA/src/Mela.cc#L630
CJLSTg4decay_pure = [sqrt(7.0), sqrt(7.0), sqrt(6.0)]#0 is 4mu, 1 is 4e, 2 is 2e2mu
CJLSTg2decay_pure = [sqrt(2.3), sqrt(2.3), sqrt(2.1)]
CJLSTg1prime2decay_pure = 12046.01#?

g4decay = 2.55052
g2decay = 1.65684
g1prime2decay_gen = -12100.42
g1prime2decay_reco = 12100.42

#https://twiki.cern.ch/twiki/pub/LHCPhysics/LHCHXSWG/Higgs_XSBR_YR4_update.xlsx
SMXSggH = 44.14        #'YR4 SM 13TeV'!B24   (ggH cross section, m=125)
SMBR2L2l = (5.897E-05  #'YR4 SM BR'!CO25     (2e2mu BR, m=125)
             *3)       #                     (include 2e2tau, 2mu2tau)
SMXS2L2l = SMXSggH * SMBR2L2l
