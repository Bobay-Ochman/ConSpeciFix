from config import *
from shutil import copyfile
from multiprocessing import Pool
import os


WEB_OUT = '/Volumes/ITDR/brian/websiteOutput/'

def copySpec(sp):
	os.mkdir(WEB_OUT+sp)
	os.mkdir(WEB_OUT+sp+'/align')
	os.mkdir(WEB_OUT+sp+'/BBH')
	os.mkdir(WEB_OUT+sp+'/genes')
	os.mkdir(WEB_OUT+sp+'/genomes')

	PATH_TO_OUTPUT = '/Volumes/ITDR/brian/a_website/'

	for file in os.listdir(PATH_TO_OUTPUT+sp+'/genes'):
		copyfile(PATH_TO_OUTPUT+sp+'/genes/'+file, WEB_OUT+sp+'/genes/'+file)
		
	copyfile(PATH_TO_OUTPUT+sp+'/orthologs.txt', WEB_OUT+sp+'/orthologs.txt')
	copyfile(PATH_TO_OUTPUT+sp+'/distrib.png', WEB_OUT+sp+'/distrib.png')
	copyfile(PATH_TO_OUTPUT+sp+'/input_'+sp+'.txt', WEB_OUT+sp+'/input_'+sp+'.txt')
	copyfile(PATH_TO_OUTPUT+sp+'/gno1.png', WEB_OUT+sp+'/hmGraph.png')

	os.chdir(PATH_TO_OUTPUT)
	command = "zip -r "+sp+'.zip '+sp
	print command
	os.system(command)
	os.system(' mv '+sp+'.zip ../websiteUploads/'+sp+'.zip')

def wrapper(sp):
	try:
		copySpec(sp)
	except Exception as e:
		print e 

if __name__ == '__main__':
	species = ['Acetobacter_pasteurianus', 'Achromobacter_xylosoxidans', 'Acinetobacter_calcoaceticus', 'Acinetobacter_pittii', 'Actinobacillus_pleuropneumoniae', 'Actinomyces_naeslundii', 'Actinomyces_oris', 'Aeromonas_hydrophila', 'Agrobacterium_tumefaciens', 'Aliivibrio_fischeri', 'Alteromonas_mediterranea', 'Anaplasma_phagocytophilum', 'Bacillus_amyloliquefaciens', 'Bacillus_coagulans', 'Bacillus_megaterium', 'Bacillus_pumilus', 'Bacillus_subtilis', 'Bacillus_velezensis', 'Bacillus_weihenstephanensis', 'Bacteroides_ovatus', 'Bacteroides_uniformis', 'Bartonella_henselae', 'Bifidobacterium_bifidum', 'Bifidobacterium_longum', 'Bifidobacterium_pseudocatenulatum', 'Bordetella_bronchiseptica', 'Borrelia_burgdorferi', 'Borrelia_garinii', 'Brachyspira_hyodysenteriae', 'Bradyrhizobium_japonicum', 'Buchnera_aphidicola', 'Burkholderia_cenocepacia', 'Burkholderia_cepacia', 'Burkholderia_multivorans', 'Burkholderia_stagnalis', 'Burkholderia_ubonensis', 'Chlamydia_trachomatis', 'Clostridium_beijerinckii', 'Clostridium_butyricum', 'Clostridium_perfringens', 'Clostridium_sporogenes', 'Comamonas_testosteroni', 'Corynebacterium_glutamicum', 'Corynebacterium_jeikeium', 'Corynebacterium_ulcerans', 'Cronobacter_sakazakii', 'Cutibacterium_acnes', 'Elizabethkingia_anophelis', 'Enterobacter_aerogenes', 'Enterobacter_asburiae', 'Enterococcus_faecalis', 'Escherichia_albertii', 'Flavobacterium_psychrophilum', 'Fusobacterium_necrophorum', 'Fusobacterium_nucleatum', 'Gallibacterium_anatis', 'Gardnerella_vaginalis', 'Gilliamella_apicola', 'Haemophilus_parainfluenzae', 'Haemophilus_parasuis', 'Helicobacter_pullorum', 'Kingella_kingae', 'Klebsiella_michiganensis', 'Klebsiella_variicola', 'Lactobacillus_aviarius', 'Lactobacillus_brevis', 'Lactobacillus_crispatus', 'Lactobacillus_delbrueckii', 'Lactobacillus_gasseri', 'Lactobacillus_helveticus', 'Lactobacillus_iners', 'Lactobacillus_kunkeei', 'Lactobacillus_reuteri', 'Lactobacillus_rhamnosus', 'Lactobacillus_salivarius', 'Lactococcus_lactis', 'Leptospira_noguchii', 'Lysinibacillus_sphaericus', 'Mesorhizobium_loti', 'Micrococcus_luteus', 'Microcystis_aeruginosa', 'Morganella_morganii', 'Mycobacterium_avium', 'Mycobacterium_chelonae', 'Mycobacterium_colombiense', 'Mycobacterium_fortuitum', 'Mycobacterium_kansasii', 'Porphyromonas_gingivalis', 'Prochlorococcus_marinus', 'Propionibacterium_freudenreichii', 'Pseudoalteromonas_luteoviolacea', 'Pseudomonas_amygdali', 'Pseudomonas_chlororaphis', 'Pseudomonas_denitrificans', 'Pseudomonas_fluorescens', 'Pseudomonas_protegens', 'Pseudomonas_putida', 'Pseudomonas_stutzeri', 'Pseudomonas_syringae', 'Rhizobium_leguminosarum', 'Rhodococcus_erythropolis', 'Rhodococcus_fascians', 'Rothia_mucilaginosa', 'Ruegeria_mobilis', 'Salinispora_pacifica', 'Sinorhizobium_meliloti', 'Staphylococcus_argenteus', 'Staphylococcus_equorum', 'Staphylococcus_hominis', 'Stenotrophomonas_maltophilia', 'Streptobacillus_moniliformis', 'Streptococcus_anginosus', 'Streptococcus_cristatus', 'Streptococcus_dysgalactiae', 'Streptococcus_equinus', 'Streptococcus_gallolyticus', 'Streptococcus_gordonii', 'Streptococcus_parasanguinis', 'Streptococcus_parauberis', 'Streptococcus_pseudopneumoniae', 'Streptococcus_pyogenes', 'Streptococcus_sanguinis', 'Streptomyces_griseus', 'Streptomyces_rimosus', 'Sulfolobus_islandicus', 'Treponema_denticola', 'Tropheryma_whipplei', 'Variovorax_paradoxus', 'Vibrio_anguillarum', 'Vibrio_campbellii', 'Vibrio_crassostreae', 'Vibrio_cyclitrophicus', 'Vibrio_nigripulchritudo', 'Vibrio_splendidus', 'Vibrio_vulnificus', 'Wolbachia_endosymbiont', 'Xanthomonas_arboricola', 'Xanthomonas_axonopodis']
	p = Pool(1)
	p.map(wrapper,species)