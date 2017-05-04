import os, math
import sys
import itertools
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class CTBL():
    def __init__(self,nwck_tree):
        self.ru = RosalindUtilities()
        self.ru.load_edges_of_newick_tree(nwck_tree)
        self.root_nodes_visited = []
        self.result = []
        pass

    def get_taxa_lexicographically_sorted(self):
        return sorted([edge for edge in self.ru.Newick_edges if not edge.isdigit()])

    def get_character_table(self):
        taxa = self.get_taxa_lexicographically_sorted()
        local_root_node = str(self.ru.GUID - 1)
        return self.get_characters_row_at_branch(taxa,local_root_node)

    def assert_all_results_valid(self,results):
        for result in results:
            if result.count('1') < 2 or result.count('0') < 2:
                print ('errror at: ' + result)

    def get_characters_row_at_branch(self,taxa,local_root_node):
        if local_root_node in self.root_nodes_visited:
            return []
        self.root_nodes_visited.append(local_root_node)

        edges = self.ru.Newick_edges[local_root_node]

        taxa_at_level = [edge[0] for edge in edges if not edge[0].isdigit()]
        root_nodes = [edge[0] for edge in edges if edge[0].isdigit()]

        for node in root_nodes:
            taxa_at_level += self.get_characters_row_at_branch(taxa,node)

        if 1 < len(taxa_at_level) < len(taxa) - 1:
            self.result.append(''.join(['1' if taxum in taxa_at_level else '0' for taxum in taxa]))

        return taxa_at_level





def Main():
    #nwck_tree = '(dog,((elephant,mouse),robot),cat);'
    #nwck_tree = '((((((((((((((Acanthogonatus_dulkeitiana,(Eutamias_licin,Rhynchophis_vulpes)),Procellaria_veredus),Nemorhaedus_pallasii),Kassina_heliaca),(Arenaria_leucogaster,Aythya_semipalmatus)),Cervus_iankowskii),(((Hemiscorpius_vastus,Upupa_felderi),(Natriciteres_chrysaetos,Ptychozoon_nyroca)),Rhinolophus_ciliatus)),(((Boa_stagnalis,Sturnus_solitaria),Emydura_maldivarum),Otocoris_savignii)),(Phrynohyas_flavigularis,Rhamphiophis_femoralis)),Ptyodactylus_dominicus),((((((((((((Alopex_scalaris,Porphyrio_hodgsoni),Coregonus_medici),Asthenodipsas_eburnea),((((Balaena_colubrinus,Ethmostigmus_gallinago),Sturnus_sudanensis),Boiga_pugnax),Coregonus_garullus)),Oceanodroma_isabellina),Eucratoscelus_cancerides),Alpes_geniculata),Lycaenopsis_perdix),Circaetus_grupus),((((((((((((Arctomys_platycephala,Monodon_baibacina),Ctenosaura_fallax),(Bombycilla_capra,(Hemitheconyx_ridibundus,(Larus_piscator,Pleurodeles_daurica)))),Damon_iguana),Teratoscincus_moschata),(Gallinago_barroni,(Lamprolepis_limosa,Salamandra_maurus))),(Calidris_boschas,Passer_alpina)),Totanus_mehelyi),Caiman_armata),Ketupa_chrysaetos),Crotaphytus_fuscatus),Eremophila_jaculus)),Falco_plathyrhychos),Euspiza_leucorodia)),(((Alpes_dauricus,(Eudrornias_peregrinus,Sceloporus_striatus)),Limosa_chukar),((((Cervus_mexicana,Macrorhamphus_sarasinorum),Kinixys_campestris),(Hottentotta_pica,Sceloporus_fernandi)),Clemmys_querquedula))),(((((((((((Aix_vertebralis,Rhodostethia_sibilans),((((((((((Aplopeltura_crucigera,Mergus_hypoleucos),(Pleurodeles_unicolor,Vipera_pallidus)),((((((((Circaetus_tolai,Mogera_mexicana),Terpsihone_dispar),Nipponia_strepera),Corallus_graeca),Synthliboramphus_picta),(Oenanthe_Anas,Pachydactylus_kraepelini)),Lycaenopsis_haliaetus),Natriciteres_fimbriatus)),Latastia_caelebs),Philothamnus_himalayanus),((Geochelone_prasina,Ketupa_campestris),Lanius_chukar)),Saxicola_chrysaetos),Coenobita_casualis),(((((((Burhinus_jubata,Pogona_venulosa),Prunella_ferina),Rhacodactylus_gallinago),Upupa_trigonopodus),(Capella_sibirica,Perdix_circia)),(Chondropython_squamatus,Gavia_brongersmai)),((((Buthacus_mongolica,(Capreolus_moschata,Furcifer_chukar)),((((Caiman_turneri,(((Gypaetus_fusca,Pelecanus_turneri),(Osteopilus_pendulinus,Passer_vastus)),Hyperoodon_paradisi)),Milvus_uluguruensis),(Dipsosaurus_vipio,Myotis_dominicus)),Pelodytes_sujfunensis)),Gekko_pallidus),Dendrobates_saxatilis))),Geochelone_ion)),(((((Ambystoma_longipes,(Calotes_interpres,Vulpes_murinus)),((Chrysopelea_calligaster,Pterocles_lineatus),Meles_cristatellus)),Natriciteres_vitticeps),((((((Balaena_apus,((Damon_dubius,Rosalia_picta),Heterodon_striatus)),(Querquedula_scincus,Scolopendra_duplus)),(Haliaetus_difficilis,Spermophilus_galeatus)),Streptopelia_ruficollis),Terpsihone_ichthyaetus),Oceanodroma_pygargus)),Grus_prasina)),Kassina_ornata),Lycodon_americanus),(Allactaga_chamaeleontinus,(Branta_veredus,(Colaeus_cepediana,Oenanthe_docilis)))),Rhynchophis_viridescens),Burhinus_unicus),(Hemitheconyx_erythropus,Kassina_davidiana)),((Phormictopus_indicus,Rhinolophus_infrafrenata),Vanellus_saxatilis)),Uncia_amethistina)),(((Accipiter_clinatus,Hadogenes_campestris),Corallus_classicus),(((((((Alaus_mandarina,(Mesoplodon_meles,Nemorhaedus_aceras)),Spizaetus_bimaculata),((((Charadrius_fiber,Theloderma_bicoloratum),(Eublepharis_longicollis,Nyroca_situla)),Dyscophus_avicularia),Gongylophis_tarda)),Neolycaena_bairdii),((Gecarcinus_lavaretus,Thymallus_tetrax),Ingerophrynus_carinata)),(Balaenoptera_platyrhinos,Limnodromus_enydris)),(((Asthenodipsas_vitulina,((Buteo_quinquestriatus,Strepsilas_graeca),Grampus_ampullatus)),Pachydactylus_oxycephalum),Vulpanser_iguana))),((((Aegypius_jubata,Bubulcus_fernandi),Pratincola_tetrax),Nhandu_tricolor),(Eudramias_leptochelis,Saiga_holbrooki)));'
    nwck_tree = '(((((((Acanthoceros_colombianus,Rhombomys_monacha),Sus_leucomystax),Zosterops_Anas),(Pleurodeles_Jankowskii,Tupinambus_means)),(Acheron_africanus,Limnaeus_aureostriata)),(((((Bombina_alpestris,(Halichoerus_wogura,Hemitheconyx_arizonensis)),Lamprophis_arizonensis),(Crocodylus_medirostris,Hysterocrates_tristis)),Norops_ampullatus),Haliaeetus_caerulea)),((((((((((((((Acanthosaura_standingii,(Sphenurus_pica,Tylototriton_karelini)),((Eudramias_soloensis,Xenochrophis_tenuirostris),Oxyura_sauromates)),Ahaetulla_flavomaculatus),(((((((Ameiva_picta,Androctonus_dispar),Thecla_cyanogaster),(Bradypterus_dione,Eudramias_rapax)),Sternotherus_tadorna),Procellaria_orientalis),((((Androctonus_naumanni,Aquila_means),Thymallus_odoratus),Enhudra_longipes),Nyroca_oedicnemus)),Circus_geyri)),Mochlus_viridis),(((Candoia_dominus,Porzana_bukhunensis),Lobipes_serpentina),Megophrys_spaldingi)),(((((((((((Androctonus_cyanogenys,(((Apalone_godlewskii,Tadarida_calyptratus),Dafila_monacha),Eucratoscelus_duplus)),(Certhia_baeri,Porphyrio_govinda)),Phasianus_truncatus),(((Anthropoides_flava,Notophthalmus_rutila),Uncia_mitratus),Scaphiophryne_laticauda)),Mareca_bicoloratum),Leiopython_hendersoni),Bos_avicularia),Corytophanes_marmoratus),Pica_albicilla),(Oligodon_viridescens,Sphenurus_karelini)),Asthenodipsas_citreola)),(Ambystoma_cioides,Cypselus_chrysaetus)),((((((Aegialifes_exanthematicus,Euspiza_musicus),Hyperoodon_limosa),((((Ambystoma_barroni,(Hysterocrates_rufus,Pachydactylus_gigas)),Macrorhamphus_galactonotus),((((Ameiva_morinellus,Thamnophis_thibetanus),(((((((Babycurus_flavescens,((Cyclemys_insignis,Phoca_sujfunensis),((Kinosternon_unicolor,Telescopus_tadorna),Paraphysa_sibirica))),Megaptera_taeniura),Oligodon_jacksoni),Ceratophrys_brevirostris),Dyscophus_piscator),Trapelus_heterolepidotus),((Cuora_licin,Epicrates_serpentina),Megaloperdix_parahybana))),Gambelia_merganser),(((((Boiga_lavaretus,Phalaropus_percnopterus),(Capra_ochropus,Ovis_acanthinura)),Scolopax_ladogensis),(Gonocephalus_boyciana,(Ninox_amboinensis,Sturnus_cepediana))),Citharacanthus_serpentina))),(Anas_subminiatus,Tamias_piscator))),((Hottentotta_galericulata,Ninox_leuconotus),Psalmopoeus_dexter)),Aix_guineti),Eryx_dendrophila)),Pandion_undulata),(Lycaenopsis_spilota,(Nyctaalus_crocodilus,Scaphiophryne_macrops))),Dipsosaurus_clarus),(((Aegialifes_eburnea,Leptobrachium_citreola),(Epicrates_edulis,(Minipterus_lutris,Otocoris_pictus))),Turdus_kraepelini)),(((((((((((((((((Actitis_pulcher,((((Aegialites_nebularia,(Lamprophis_scabra,Telescopus_insularis)),Gongylophis_marcianus),Polypedates_kingii),Panthera_lavaretus)),Porphyrio_monorhis),(((((((((((Ameiva_melleri,Iguana_maldivarum),(((Antilope_apus,Canis_vastus),(Nemorhaedus_fuellebornii,Xenopeltis_mexicana)),((Ciconia_carnifex,Phrynocephalus_boschas),((Ketupa_marcianus,(Kinixys_scrofa,(Pusa_melonotis,Teratoscincus_turneri))),Totanus_cyanogenys)))),(Erpeton_chrysargos,Phoca_blakistoni)),Oligodon_sieboldii),(Basiliscus_ferina,Falco_fischeri)),Litoria_flava),((((Buteo_punctatus,(Sceloporus_femoralis,Squaterola_peregrinus)),Eutamias_cavimanus),Meles_lepturus),Pelusios_homeana)),Coenobita_pelagicus),Siniperca_leucotus),((Capra_caudata,Rhamphiophis_tuberculosus),Elaphe_casualis)),Parnassius_onocrotalus)),((Anolis_pallidus,((Heteroscodra_picta,Ingerophrynus_shadini),Megaptera_plumipes)),Net_deserti)),Tadarida_climacophora),Eirenis_standingii),(Allobates_argali,(((Epipedobates_hemilasius,((Eubalaena_aleutica,Odobenus_pardus),Himantopus_niloticus)),Gavia_flammea),Teratolepis_crassicauda))),(Syrrhaptes_boschas,Varanus_japonensis)),Rhombomys_rufina),((Androctonus_crassicauda,((Falco_mutabilis,Pandion_heterolepidotus),(Hysterocrates_clypeatus,Minipterus_lutra))),Buthus_walti)),Lasiodora_giganteus),(Monachus_dignus,Uroplatus_marmorata)),Scolopendra_acuta),Chelodina_cenchria),(Anser_musicus,((Capeila_edulis,Neophron_subrufa),(Nucifraga_taeniura,Upupa_bellii)))),(Burhinus_arcticus,Eublepharis_helvetica)),Zosterops_dominus)),(((Accipiter_aegyptia,Scorpio_aleutica),Anthropoidae_eximia),Capeila_carnifex));'
    #nwck_tree = '(((C,D),(E,F)),A,B);'
    solver = CTBL(nwck_tree)
    #print(solver.ru.nwck_tree)
    #print(solver.ru.Newick_edges)
    #print(solver.ru.GUID - 1)
    solver.get_character_table()
    print(len(solver.result))
    print(len(set(solver.result)))
    with open('output','w') as output_data:
        #for edge in sorted(solver.ru.Newick_edges):
#            output_data.write(edge + '\n')
        for result in set(solver.result):
            output_data.write(result + '\n')
    solver.assert_all_results_valid(solver.result)

if __name__ == '__main__':
    Main()