# -*- coding: utf-8 -*-
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'elements.json')

# n, sym, name_pt, mass, category, group(x 1-18), period(y), electron config, desc_pt
# category codes: alkali, alkaline, translm(transition metal), postm(post-transition), metalloid,
# nonmetal, halogen, noble, lanth, actin, unknown
E = [
(1,"H","Hidrogênio",1.008,"nonmetal",1,1,"1s1","Elemento mais abundante do universo. Combustível de estrelas e futura matriz energética."),
(2,"He","Hélio",4.0026,"noble",18,1,"1s2","Gás nobre inerte, segundo mais abundante do cosmos. Usado em criogenia e balões."),
(3,"Li","Lítio",6.94,"alkali",1,2,"[He]2s1","Metal alcalino leve. Coração das baterias que movem a eletrificação global."),
(4,"Be","Berílio",9.0122,"alkaline",2,2,"[He]2s2","Metal leve e rígido, usado em ligas aeroespaciais e janelas de raios-X."),
(5,"B","Boro",10.81,"metalloid",13,2,"[He]2s2 2p1","Metaloide usado em vidros borossilicato, fibras e semicondutores."),
(6,"C","Carbono",12.011,"nonmetal",14,2,"[He]2s2 2p2","Base da química orgânica e da vida. Do grafeno ao diamante."),
(7,"N","Nitrogênio",14.007,"nonmetal",15,2,"[He]2s2 2p3","78% da atmosfera. Essencial para fertilizantes e proteínas."),
(8,"O","Oxigênio",15.999,"nonmetal",16,2,"[He]2s2 2p4","Sustenta a respiração e a combustão. Segundo mais eletronegativo."),
(9,"F","Flúor",18.998,"halogen",17,2,"[He]2s2 2p5","O elemento mais reativo. Halogênio usado em teflon e flúor dental."),
(10,"Ne","Neônio",20.180,"noble",18,2,"[He]2s2 2p6","Gás nobre que brilha em vermelho-alaranjado nos letreiros luminosos."),
(11,"Na","Sódio",22.990,"alkali",1,3,"[Ne]3s1","Metal alcalino reativo. Componente do sal e de fluidos biológicos."),
(12,"Mg","Magnésio",24.305,"alkaline",2,3,"[Ne]3s2","Metal leve estrutural, essencial à clorofila e ao metabolismo."),
(13,"Al","Alumínio",26.982,"postm",13,3,"[Ne]3s2 3p1","Metal leve mais abundante na crosta. Base da indústria aeroespacial."),
(14,"Si","Silício",28.085,"metalloid",14,3,"[Ne]3s2 3p2","O metaloide da era digital. Alma dos chips e das células solares."),
(15,"P","Fósforo",30.974,"nonmetal",15,3,"[Ne]3s2 3p3","Essencial ao DNA e ao ATP. Insubstituível na agricultura."),
(16,"S","Enxofre",32.06,"nonmetal",16,3,"[Ne]3s2 3p4","Usado em ácido sulfúrico, o químico industrial mais produzido."),
(17,"Cl","Cloro",35.45,"halogen",17,3,"[Ne]3s2 3p5","Halogênio desinfetante. Trata água e produz PVC."),
(18,"Ar","Argônio",39.948,"noble",18,3,"[Ne]3s2 3p6","Gás nobre inerte usado em soldas e lâmpadas."),
(19,"K","Potássio",39.098,"alkali",1,4,"[Ar]4s1","Metal alcalino vital para nervos e músculos. Fertilizante-chave."),
(20,"Ca","Cálcio",40.078,"alkaline",2,4,"[Ar]4s2","Estrutura de ossos e conchas. Base do cimento e do calcário."),
(21,"Sc","Escândio",44.956,"translm",3,4,"[Ar]3d1 4s2","Metal de transição leve usado em ligas aeroespaciais de alta performance."),
(22,"Ti","Titânio",47.867,"translm",4,4,"[Ar]3d2 4s2","Metal forte, leve e biocompatível. Próteses, aviões e foguetes."),
(23,"V","Vanádio",50.942,"translm",5,4,"[Ar]3d3 4s2","Endurece aços e habilita baterias de fluxo para armazenamento de energia."),
(24,"Cr","Cromo",51.996,"translm",6,4,"[Ar]3d5 4s1","Dá o brilho ao aço inox e proteção anticorrosiva."),
(25,"Mn","Manganês",54.938,"translm",7,4,"[Ar]3d5 4s2","Essencial ao aço e às baterias de íon-lítio. Brasil é grande produtor."),
(26,"Fe","Ferro",55.845,"translm",8,4,"[Ar]3d6 4s2","O metal da civilização. Espinha dorsal do aço e do minério brasileiro."),
(27,"Co","Cobalto",58.933,"translm",9,4,"[Ar]3d7 4s2","Mineral crítico para baterias e superligas. Alta concentração geopolítica."),
(28,"Ni","Níquel",58.693,"translm",10,4,"[Ar]3d8 4s2","Essencial ao aço inox e às baterias. Mineral estratégico da transição."),
(29,"Cu","Cobre",63.546,"translm",11,4,"[Ar]3d10 4s1","Condutor por excelência. Termômetro da eletrificação mundial."),
(30,"Zn","Zinco",65.38,"translm",12,4,"[Ar]3d10 4s2","Protege o aço da corrosão (galvanização) e é vital à saúde."),
(31,"Ga","Gálio",69.723,"postm",13,4,"[Ar]3d10 4s2 4p1","Derrete na mão. Base de semicondutores como GaN e GaAs."),
(32,"Ge","Germânio",72.630,"metalloid",14,4,"[Ar]3d10 4s2 4p2","Metaloide usado em fibra óptica e infravermelho. Mineral crítico."),
(33,"As","Arsênio",74.922,"metalloid",15,4,"[Ar]3d10 4s2 4p3","Metaloide tóxico usado em semicondutores e ligas."),
(34,"Se","Selênio",78.971,"nonmetal",16,4,"[Ar]3d10 4s2 4p4","Usado em fotocélulas e vidros. Micronutriente essencial."),
(35,"Br","Bromo",79.904,"halogen",17,4,"[Ar]3d10 4s2 4p5","Halogênio líquido usado em retardantes de chama."),
(36,"Kr","Criptônio",83.798,"noble",18,4,"[Ar]3d10 4s2 4p6","Gás nobre usado em iluminação de alta performance e lasers."),
(37,"Rb","Rubídio",85.468,"alkali",1,5,"[Kr]5s1","Metal alcalino usado em relógios atômicos e pesquisa."),
(38,"Sr","Estrôncio",87.62,"alkaline",2,5,"[Kr]5s2","Dá a cor vermelha aos fogos de artifício. Usado em ímãs cerâmicos."),
(39,"Y","Ítrio",88.906,"translm",3,5,"[Kr]4d1 5s2","Terra rara usada em fósforos, lasers e supercondutores."),
(40,"Zr","Zircônio",91.224,"translm",4,5,"[Kr]4d2 5s2","Resistente à corrosão e ao calor. Usado em reatores nucleares."),
(41,"Nb","Nióbio",92.906,"translm",5,5,"[Kr]4d4 5s1","O metal do Brasil: 90% da reserva mundial. Superligas e supercondutores."),
(42,"Mo","Molibdênio",95.95,"translm",6,5,"[Kr]4d5 5s1","Endurece aços para altas temperaturas. Catalisador industrial."),
(43,"Tc","Tecnécio",98,"translm",7,5,"[Kr]4d5 5s2","Primeiro elemento sintético. Usado em imagens médicas."),
(44,"Ru","Rutênio",101.07,"translm",8,5,"[Kr]4d7 5s1","Metal do grupo da platina. Catalisador e eletrônica."),
(45,"Rh","Ródio",102.91,"translm",9,5,"[Kr]4d8 5s1","Um dos metais mais caros. Catalisadores automotivos."),
(46,"Pd","Paládio",106.42,"translm",10,5,"[Kr]4d10","Metal precioso essencial a catalisadores e eletrônica."),
(47,"Ag","Prata",107.87,"translm",11,5,"[Kr]4d10 5s1","Melhor condutor elétrico. Joias, eletrônica e fotovoltaico."),
(48,"Cd","Cádmio",112.41,"translm",12,5,"[Kr]4d10 5s2","Metal tóxico usado em baterias e pigmentos."),
(49,"In","Índio",114.82,"postm",13,5,"[Kr]4d10 5s2 5p1","Base do ITO das telas touch. Mineral crítico."),
(50,"Sn","Estanho",118.71,"postm",14,5,"[Kr]4d10 5s2 5p2","Metal antigo do bronze. Usado em soldas e revestimentos."),
(51,"Sb","Antimônio",121.76,"metalloid",15,5,"[Kr]4d10 5s2 5p3","Metaloide usado em retardantes de chama. Mineral crítico."),
(52,"Te","Telúrio",127.60,"metalloid",16,5,"[Kr]4d10 5s2 5p4","Metaloide de painéis solares CdTe e termoelétricos."),
(53,"I","Iodo",126.90,"halogen",17,5,"[Kr]4d10 5s2 5p5","Halogênio essencial à tireoide. Antisséptico clássico."),
(54,"Xe","Xenônio",131.29,"noble",18,5,"[Kr]4d10 5s2 5p6","Gás nobre de faróis e propulsão iônica de satélites."),
(55,"Cs","Césio",132.91,"alkali",1,6,"[Xe]6s1","Define o segundo nos relógios atômicos. Metal alcalino reativo."),
(56,"Ba","Bário",137.33,"alkaline",2,6,"[Xe]6s2","Usado em contraste de raios-X e perfuração de poços."),
(57,"La","Lantânio",138.91,"lanth",3,9,"[Xe]5d1 6s2","Terra rara de lentes ópticas e baterias NiMH."),
(58,"Ce","Cério",140.12,"lanth",4,9,"[Xe]4f1 5d1 6s2","Terra rara mais abundante. Catalisadores e polimento."),
(59,"Pr","Praseodímio",140.91,"lanth",5,9,"[Xe]4f3 6s2","Terra rara de ímãs potentes e vidros especiais."),
(60,"Nd","Neodímio",144.24,"lanth",6,9,"[Xe]4f4 6s2","Ímã de neodímio: o mais forte. Motores elétricos e turbinas eólicas."),
(61,"Pm","Promécio",145,"lanth",7,9,"[Xe]4f5 6s2","Terra rara radioativa usada em baterias nucleares e luminosos."),
(62,"Sm","Samário",150.36,"lanth",8,9,"[Xe]4f6 6s2","Ímãs de samário-cobalto resistentes ao calor. Defesa e aeroespacial."),
(63,"Eu","Európio",151.96,"lanth",9,9,"[Xe]4f7 6s2","Fósforo vermelho de telas. Terra rara de segurança em cédulas."),
(64,"Gd","Gadolínio",157.25,"lanth",10,9,"[Xe]4f7 5d1 6s2","Contraste de ressonância magnética e blindagem nuclear."),
(65,"Tb","Térbio",158.93,"lanth",11,9,"[Xe]4f9 6s2","Terra rara de ímãs de alta temperatura e fósforos verdes."),
(66,"Dy","Disprósio",162.50,"lanth",12,9,"[Xe]4f10 6s2","Crítica para ímãs de motores EV e turbinas. Alto risco de suprimento."),
(67,"Ho","Hólmio",164.93,"lanth",13,9,"[Xe]4f11 6s2","Maior momento magnético. Lasers médicos e ímãs."),
(68,"Er","Érbio",167.26,"lanth",14,9,"[Xe]4f12 6s2","Amplifica sinais em fibras ópticas. Lasers e vidros rosa."),
(69,"Tm","Túlio",168.93,"lanth",15,9,"[Xe]4f13 6s2","Terra rara rara usada em lasers portáteis e raios-X."),
(70,"Yb","Itérbio",173.05,"lanth",16,9,"[Xe]4f14 6s2","Relógios atômicos ópticos e ligas de aço inox."),
(71,"Lu","Lutécio",174.97,"lanth",17,9,"[Xe]4f14 5d1 6s2","Terra rara mais densa. Catalisadores e PET scans."),
(72,"Hf","Háfnio",178.49,"translm",4,6,"[Xe]4f14 5d2 6s2","Absorve nêutrons em reatores. Chips avançados e superligas."),
(73,"Ta","Tântalo",180.95,"translm",5,6,"[Xe]4f14 5d3 6s2","Capacitores de eletrônicos. Mineral de conflito monitorado."),
(74,"W","Tungstênio",183.84,"translm",6,6,"[Xe]4f14 5d4 6s2","Maior ponto de fusão dos metais. Filamentos e ferramentas de corte."),
(75,"Re","Rênio",186.21,"translm",7,6,"[Xe]4f14 5d5 6s2","Superligas de turbinas a jato. Um dos metais mais raros."),
(76,"Os","Ósmio",190.23,"translm",8,6,"[Xe]4f14 5d6 6s2","O elemento mais denso. Pontas de caneta e contatos elétricos."),
(77,"Ir","Irídio",192.22,"translm",9,6,"[Xe]4f14 5d7 6s2","Extremamente resistente à corrosão. Velas de ignição e telas OLED."),
(78,"Pt","Platina",195.08,"translm",10,6,"[Xe]4f14 5d9 6s1","Metal precioso catalisador. Joias e células de hidrogênio."),
(79,"Au","Ouro",196.97,"translm",11,6,"[Xe]4f14 5d10 6s1","Reserva de valor milenar. Eletrônica e reserva monetária."),
(80,"Hg","Mercúrio",200.59,"translm",12,6,"[Xe]4f14 5d10 6s2","Único metal líquido à temperatura ambiente. Tóxico, uso em declínio."),
(81,"Tl","Tálio",204.38,"postm",13,6,"[Xe]4f14 5d10 6s2 6p1","Metal tóxico usado em eletrônica e detectores de infravermelho."),
(82,"Pb","Chumbo",207.2,"postm",14,6,"[Xe]4f14 5d10 6s2 6p2","Denso e tóxico. Baterias automotivas e blindagem radioativa."),
(83,"Bi","Bismuto",208.98,"postm",15,6,"[Xe]4f14 5d10 6s2 6p3","Metal pesado atóxico. Substitui chumbo e cria cristais coloridos."),
(84,"Po","Polônio",209,"postm",16,6,"[Xe]4f14 5d10 6s2 6p4","Radioativo intenso descoberto por Marie Curie."),
(85,"At","Astato",210,"halogen",17,6,"[Xe]4f14 5d10 6s2 6p5","O elemento natural mais raro. Radioativo, pesquisa em radioterapia."),
(86,"Rn","Radônio",222,"noble",18,6,"[Xe]4f14 5d10 6s2 6p6","Gás nobre radioativo. Risco em porões e minas."),
(87,"Fr","Frâncio",223,"alkali",1,7,"[Rn]7s1","Metal alcalino raríssimo e radioativo. Meia-vida de minutos."),
(88,"Ra","Rádio",226,"alkaline",2,7,"[Rn]7s2","Radioativo luminescente. Usado historicamente em mostradores."),
(89,"Ac","Actínio",227,"actin",3,10,"[Rn]6d1 7s2","Primeiro actinídeo. Radioativo, estudado em radioterapia alvo."),
(90,"Th","Tório",232.04,"actin",4,10,"[Rn]6d2 7s2","Combustível nuclear alternativo. Abundante e menos proliferante."),
(91,"Pa","Protactínio",231.04,"actin",5,10,"[Rn]5f2 6d1 7s2","Actinídeo raro e radioativo. Uso restrito à pesquisa."),
(92,"U","Urânio",238.03,"actin",6,10,"[Rn]5f3 6d1 7s2","Combustível nuclear por excelência. Físsil e estratégico."),
(93,"Np","Netúnio",237,"actin",7,10,"[Rn]5f4 6d1 7s2","Primeiro transurânico. Subproduto de reatores nucleares."),
(94,"Pu","Plutônio",244,"actin",8,10,"[Rn]5f6 7s2","Combustível e material de armas. Gerador de sondas espaciais."),
(95,"Am","Amerício",243,"actin",9,10,"[Rn]5f7 7s2","Usado em detectores de fumaça domésticos."),
(96,"Cm","Cúrio",247,"actin",10,10,"[Rn]5f7 6d1 7s2","Actinídeo sintético usado como fonte de energia em pesquisa."),
(97,"Bk","Berquélio",247,"actin",11,10,"[Rn]5f9 7s2","Elemento sintético raro, produzido em quantidades mínimas."),
(98,"Cf","Califórnio",251,"actin",12,10,"[Rn]5f10 7s2","Fonte de nêutrons para detecção de ouro e petróleo."),
(99,"Es","Einstênio",252,"actin",13,10,"[Rn]5f11 7s2","Sintético descoberto em testes nucleares. Só pesquisa."),
(100,"Fm","Férmio",257,"actin",14,10,"[Rn]5f12 7s2","Último elemento produzível por captura de nêutrons."),
(101,"Md","Mendelévio",258,"actin",15,10,"[Rn]5f13 7s2","Sintético produzido átomo a átomo. Homenagem a Mendeleev."),
(102,"No","Nobélio",259,"actin",16,10,"[Rn]5f14 7s2","Actinídeo sintético de vida curta. Só pesquisa."),
(103,"Lr","Laurêncio",262,"actin",17,10,"[Rn]5f14 7s2 7p1","Último actinídeo. Existe apenas em laboratório."),
(104,"Rf","Rutherfórdio",267,"translm",4,7,"[Rn]5f14 6d2 7s2","Transurânico sintético superpesado. Vida ultracurta."),
(105,"Db","Dúbnio",268,"translm",5,7,"[Rn]5f14 6d3 7s2","Elemento superpesado sintético. Só pesquisa."),
(106,"Sg","Seabórgio",269,"translm",6,7,"[Rn]5f14 6d4 7s2","Sintético nomeado em honra a Glenn Seaborg."),
(107,"Bh","Bóhrio",270,"translm",7,7,"[Rn]5f14 6d5 7s2","Superpesado sintético, apenas alguns átomos já criados."),
(108,"Hs","Hássio",269,"translm",8,7,"[Rn]5f14 6d6 7s2","Elemento superpesado sintético de vida curtíssima."),
(109,"Mt","Meitnério",278,"unknown",9,7,"[Rn]5f14 6d7 7s2","Sintético nomeado em honra a Lise Meitner."),
(110,"Ds","Darmstácio",281,"unknown",10,7,"[Rn]5f14 6d8 7s2","Superpesado sintético produzido em aceleradores."),
(111,"Rg","Roentgênio",282,"unknown",11,7,"[Rn]5f14 6d9 7s2","Elemento sintético nomeado em honra a Röntgen."),
(112,"Cn","Copernício",285,"translm",12,7,"[Rn]5f14 6d10 7s2","Superpesado, possivelmente volátil como o mercúrio."),
(113,"Nh","Nihônio",286,"unknown",13,7,"[Rn]5f14 6d10 7s2 7p1","Primeiro elemento descoberto na Ásia (Japão)."),
(114,"Fl","Fleróvio",289,"unknown",14,7,"[Rn]5f14 6d10 7s2 7p2","Superpesado sintético, próximo da 'ilha de estabilidade'."),
(115,"Mc","Moscóvio",290,"unknown",15,7,"[Rn]5f14 6d10 7s2 7p3","Sintético nomeado pela região de Moscou."),
(116,"Lv","Livermório",293,"unknown",16,7,"[Rn]5f14 6d10 7s2 7p4","Superpesado sintético de vida ultracurta."),
(117,"Ts","Tennesso",294,"unknown",17,7,"[Rn]5f14 6d10 7s2 7p5","Halogênio sintético teórico, um dos últimos criados."),
(118,"Og","Oganessônio",294,"unknown",18,7,"[Rn]5f14 6d10 7s2 7p6","O elemento mais pesado já criado. Nomeado em vida a Oganessian."),
]


# ---- camadas eletrônicas (aufbau), prótons/nêutrons e flag radioativo ----
_ORDER=[(1,'s'),(2,'s'),(2,'p'),(3,'s'),(3,'p'),(4,'s'),(3,'d'),(4,'p'),(5,'s'),
(4,'d'),(5,'p'),(6,'s'),(4,'f'),(5,'d'),(6,'p'),(7,'s'),(5,'f'),(6,'d'),(7,'p')]
_CAP={'s':2,'p':6,'d':10,'f':14}
def _shells(Z):
    per={}; left=Z
    for n,l in _ORDER:
        if left<=0: break
        e=min(_CAP[l],left); per[n]=per.get(n,0)+e; left-=e
    return [per[n] for n in sorted(per)]

data = [dict(n=e[0],sym=e[1],name=e[2],mass=e[3],cat=e[4],x=e[5],y=e[6],cfg=e[7],desc=e[8]) for e in E]
for _e in data:
    _Z=_e['n']
    _e['shells']=_shells(_Z)
    _e['protons']=_Z
    _e['neutrons']=max(0, round(_e['mass'])-_Z)
    _e['radioactive']=(_Z in (43,61)) or (_Z>=84)
print("count:", len(data))
assert len(data)==118
with open(OUT,"w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False)
print("ok")
