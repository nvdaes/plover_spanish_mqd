import os
import sys
sys.path.append(os.path.dirname(__file__))
import spanish_mqd_single
del sys.path[-1]

LONGEST_KEY = 2

VOWELS = ("a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú")

doubleStrokes = {
	"Ccn": "camina",
	"Ccs": "categoriza",
	"Ccsn": "aconseja",
	"Ccsp": "calla",
	"Cct": "activa",
	"Cctn": "indica",
	"CNc": "cono",
	"CNcn": "condiciona",
	"CNct": "encanta",
	"CNctn": "conciencia",
	"CNRcn": "elimina",
	"CNRcnp": "marcha",
	"CNRcs": "imagina",
	"CNRcsn": "mejora",
	"CNRcstn": "minimiza",
	"CNRcstnp": "maximiza",
	"CNRctn": "modera",
	"CNRsn": "comercializa",
	"CNRst": "mostra",
	"CNRstn": "matiza",
	"CNsn": "economiza",
	"CNstp": "encomenda",
	"CNt": "concreta",
	"CNVc": "convoca",
	"CNVRc": "compara",
	"CNVRcn": "emociona",
	"CNVRct": "motiva",
	"CNVRctn": "recorda",
	"CNVRn": "enamora",
	"CNVRsn": "moviliza",
	"CNVRst": "contrarresta",
	"CNVRstn": "cerra",
	"CNVRt": "comporta",
	"CNVRtn": "dura",
	"CNVs": "conversa",
	"Cp": "culpa",
	"CRc": "acaricia",
	"CRcn": "circula",
	"CRcp": "incrementa",
	"CRcs": "carga",
	"CRcstn": "encariña",
	"CRct": "celebra",
	"CRctn": "acorda",
	"CRsn": "caracteriza",
	"CRstn": "democratiza",
	"CRt": "certa",
	"CRtn": "coordina",
	"Csn": "comenza",
	"Cstn": "considera",
	"Ct": "actua",
	"CTc": "toca",
	"CTcn": "centra",
	"CTcs": "castiga",
	"CTcsn": "centraliza",
	"CTcsnp": "coteja",
	"CTcstn": "conquista",
	"CTct": "cultiva",
	"CTctn": "acata",
	"CTctnp": "percata",
	"CTctp": "acostumbra",
	"CTn": "continua",
	"CTNc": "comunica",
	"CTNcn": "concentra",
	"CTNcsn": "adjudica",
	"CTNcst": "coadyuva",
	"CTNcstn": "ataca",
	"CTNct": "incentiva",
	"CTNctn": "adecua",
	"CTNn": "denomina",
	"CTNp": "cuida",
	"CTNRc": "califica",
	"CTNRcn": "concilia",
	"CTNRcs": "colegia",
	"CTNRcsn": "indemniza",
	"CTNRctn": "declara",
	"CTNREOsn": "culpabiliza",
	"CTNRn": "termina",
	"CTNRs": "clausura",
	"CTNRsn": "moderniza",
	"CTNRst": "demostra",
	"CTNRstn": "automatiza",
	"CTNRt": "maltrata",
	"CTNsn": "contextualiza",
	"CTNt": "contesta",
	"CTNtn": "encuaderna",
	"CTNtp": "dificulta",
	"CTNVc": "financia",
	"CTNVct": "notifica",
	"CTNVn": "confia",
	"CTNVR": "forma",
	"CTNVRc": "modifica",
	"CTNVRcs": "homologa",
	"CTNVRcsn": "homogeneiza",
	"CTNVRct": "cualifica",
	"CTNVRctn": "damnifica",
	"CTNVRn": "formula",
	"CTNVRsn": "formaliza",
	"CTNVRst": "manifesta",
	"CTNVRstn": "traumatiza",
	"CTNVRt": "facilita",
	"CTNVRtn": "fundamenta",
	"CTNVs": "confesa",
	"CTNVsn": "afianza",
	"CTRc": "critica",
	"CTRct": "decreta",
	"CTRctn": "aclara",
	"CTRn": "controla",
	"CTRst": "contrasta",
	"CTRt": "contrata",
	"CTRtn": "acredita",
	"CTsn": "actualiza",
	"CTt": "anticipa",
	"CTtn": "comenta",
	"CTVc": "certifica",
	"CTVcs": "configura",
	"CTVct": "cuantifica",
	"CTVp": "enfoca",
	"CTVRc": "fortale",
	"CTVRct": "ratifica",
	"CTVRsn": "forza",
	"CTVsn": "inflama",
	"CTVt": "infecta",
	"CVc": "equivoca",
	"CVctp": "cautiva",
	"CVn": "vincula",
	"CVRc": "condu",
	"CVsn": "civiliza",
	"CVtn": "avecina",
	"Nc": "inicia",
	"Ncnp": "sanciona",
	"Ncs": "negocia",
	"Ncsnp": "maneja",
	"Nctn": "encontra",
	"Nctp": "nombra",
	"NRcn": "relaciona",
	"NRcnp": "alenta",
	"NRcsp": "alegra",
	"NRctn": "levanta",
	"NRctp": "libera",
	"NRp": "emplea",
	"NRs": "legisla",
	"NRsn": "alcanza",
	"NRstn": "idealiza",
	"NRt": "altera",
	"NRtnp": "idea",
	"Nsn": "numera",
	"Nsnp": "enlaza",
	"Nstn": "narra",
	"Nstp": "enmenda",
	"Ntn": "anda",
	"NVc": "involucra",
	"NVcs": "navega",
	"NVct": "innova",
	"NVctn": "evidencia",
	"NVn": "inventa",
	"NVRc": "para",
	"NVRcn": "evoluciona",
	"NVRcnp": "arranca",
	"NVRcs": "vigila",
	"NVRcstn": "arraiga",
	"NVRct": "evalua",
	"NVRctn": "erradica",
	"NVRp": "alivia",
	"NVRs": "pasa",
	"NVRsn": "interioriza",
	"NVRstn": "aterroriza",
	"NVRstnp": "aterra",
	"NVRt": "porta",
	"NVRtn": "olvida",
	"NVsn": "individualiza",
	"NVt": "invita",
	"PCcs": "agrupa",
	"PCcstn": "acompaña",
	"PCctp": "goberna",
	"PCNc": "diagnostica",
	"PCNcs": "iguala",
	"PCNcstn": "engaña",
	"PCNct": "averigua",
	"PCNn": "ignora",
	"PCNRc": "implica",
	"PCNRcn": "emancipa",
	"PCNRcs": "regula",
	"PCNRcsn": "agiliza",
	"PCNRcstn": "empequeñe",
	"PCNRctn": "dialoga",
	"PCNRn": "inaugura",
	"PCNRp": "premia",
	"PCNRs": "ingresa",
	"PCNRsn": "regulariza",
	"PCNRstn": "implementa",
	"PCNs": "compensa",
	"PCNt": "aguanta",
	"PCNtn": "agranda",
	"PCNVRc": "preocupa",
	"PCNVRcn": "promociona",
	"PCNVRn": "manipula",
	"PCNVRsn": "vulgariza",
	"PCNVRst": "molesta",
	"PCp": "propicia",
	"PCRc": "ocupa",
	"PCRcn": "recapitula",
	"PCRcs": "migra",
	"PCRcsn": "impregna",
	"PCRcstn": "engrande",
	"PCRct": "comproba",
	"PCRctn": "graba",
	"PCRn": "genera",
	"PCRp": "logra",
	"PCRs": "progresa",
	"PCRsn": "generaliza",
	"PCRst": "registra",
	"PCRstn": "recupera",
	"PCRt": "apropia",
	"PCRtn": "guarda",
	"PCRtp": "refugia",
	"Pcs": "pregunta",
	"PCsn": "organiza",
	"PCsnp": "goza",
	"Pcst": "apoya",
	"PCst": "gusta",
	"PCstn": "arregla",
	"PCstnp": "agarra",
	"PCt": "agota",
	"PCTcs": "juga",
	"PCTcsn": "enjuicia",
	"PCTcsnp": "juzga",
	"PCTcst": "justifica",
	"PCTcstn": "pacta",
	"PCTct": "ejecuta",
	"PCTNc": "agrade",
	"PCTNcst": "dignifica",
	"PCTNct": "enveje",
	"PCTNctn": "agrada",
	"PCTNp": "empeña",
	"PCTNRc": "multiplica",
	"PCTNRcsn": "empuja",
	"PCTNRcstn": "impacta",
	"PCTNRn": "aglutina",
	"PCTNRsn": "digitaliza",
	"PCTNRt": "argumenta",
	"PCTNsn": "garantiza",
	"PCTNt": "capacita",
	"PCTNtn": "degrada",
	"PCTNVc": "enrique",
	"PCTNVRcstn": "equipara",
	"PCTNVRctn": "queda",
	"PCTNVRctp": "equilibra",
	"PCTRn": "jura",
	"PCTRt": "ejercita",
	"PCTst": "ajusta",
	"PCTstn": "conceptualiza",
	"PCTt": "junta",
	"PCTVc": "publica",
	"PCTVct": "colabora",
	"PCTVctp": "cambia",
	"PCTVn": "combina",
	"PCTVRc": "fabrica",
	"PCTVRct": "elucubra",
	"PCTVRsn": "burocratiza",
	"PCTVRstn": "coopera",
	"PCTVRtp": "alerta",
	"PCTVsn": "compatibiliza",
	"PCVcn": "acumula",
	"PCVct": "grava",
	"PCVRcn": "lucha",
	"PCVRcs": "llega",
	"PCVRcsn": "aloja",
	"PCVRct": "lleva",
	"PCVRn": "llena",
	"PCVRsn": "llama",
	"PCVRt": "alimenta",
	"PNc": "incorpora",
	"PNcn": "coloca",
	"PNctn": "pondera",
	"PNn": "opina",
	"PNnp": "apena",
	"PNRc": "aplica",
	"PNRcp": "complementa",
	"PNRcs": "promulga",
	"PNRcsn": "peligra",
	"PNRcstn": "polariza",
	"PNRctn": "contempla",
	"PNRp": "completa",
	"PNRs": "pulsa",
	"PNRsn": "reemplaza",
	"PNRstn": "limita",
	"PNRt": "implanta",
	"PNs": "pensa",
	"PNsn": "puntualiza",
	"PNt": "plantea",
	"PNtp": "apunta",
	"PNVRc": "prepara",
	"PNVRn": "recopila",
	"PNVRs": "repasa",
	"PNVRstn": "empeora",
	"PNVRt": "aporta",
	"PRc": "produ",
	"PRcn": "proporciona",
	"PRcs": "programa",
	"PRcsn": "perjudica",
	"PRcst": "proyecta",
	"PRct": "proba",
	"PRsn": "aproxima",
	"PRstnp": "procura",
	"PRt": "presenta",
	"Psn": "empeza",
	"Pt": "opta",
	"PTcn": "potencia",
	"PTct": "acepta",
	"PTctnp": "patenta",
	"PTNc": "pertene",
	"PTNcn": "decepciona",
	"PTNRc": "pronostica",
	"PTNRct": "cumplimenta",
	"PTNRn": "perdona",
	"PTNRt": "interpreta",
	"PTNs": "dispersa",
	"PTNsn": "prioriza",
	"PTNstn": "inspira",
	"PTNstp": "desperta",
	"PTNt": "adapta",
	"PTNVcsn": "dibuja",
	"PTNVn": "deambula",
	"PTNVRc": "estable",
	"PTNVRcsn": "globaliza",
	"PTNVRcsnp": "engloba",
	"PTNVRcstn": "restable",
	"PTNVRct": "elabora",
	"PTNVRp": "alberga",
	"PTNVRsn": "estabiliza",
	"PTNVRstn": "horripila",
	"PTNVRt": "entabla",
	"PTNVt": "habita",
	"PTNVtn": "abandona",
	"PTp": "tapa",
	"PTRc": "practica",
	"PTRcn": "patrocina",
	"PTRsn": "protagoniza",
	"PTRstn": "dinamiza",
	"PTRt": "protesta",
	"PTs": "posibilita",
	"PTsn": "optimiza",
	"PTsp": "aposta",
	"PTt": "participa",
	"PTVc": "planifica",
	"PTVcn": "perfecciona",
	"PTVcs": "obliga",
	"PTVcsn": "baja",
	"PTVcstn": "bloquea",
	"PTVRcstn": "vibra",
	"PTVRctn": "abrevia",
	"PTVRp": "abarca",
	"PTVRsn": "urbaniza",
	"PTVRstn": "opera",
	"PTVRtn": "aborda",
	"PTVs": "basa",
	"PTVt": "objeta",
	"PTVtnp": "habitua",
	"PTVtp": "beneficia",
	"PVc": "provoca",
	"PVRc": "prevale",
	"PVRt": "evita",
	"Rcn": "reacciona",
	"Rcp": "recalca",
	"Rcstn": "armoniza",
	"Rct": "renova",
	"Rctn": "recomenda",
	"Rsn": "realiza",
	"Rsnp": "rechaza",
	"Rsp": "usa",
	"Rst": "resulta",
	"Rstn": "teoriza",
	"Rt": "tira",
	"Rtn": "ordena",
	"Rtnp": "remedia",
	"Sc": "sindica",
	"SCc": "asocia",
	"SCcn": "oscila",
	"SCn": "necesita",
	"SCNc": "escucha",
	"SCNcsn": "consigna",
	"SCNct": "conserva",
	"SCNn": "ocasiona",
	"SCNRcn": "menciona",
	"SCNRcsn": "margina",
	"SCNRctn": "manda",
	"SCNRp": "ayuda",
	"SCNRsn": "materializa",
	"SCNRstn": "amortiza",
	"SCNs": "cansa",
	"SCNsn": "normaliza",
	"SCNst": "consulta",
	"SCNt": "conecta",
	"SCNtnp": "consensua",
	"SCNtp": "contacta",
	"SCNVRc": "complica",
	"SCNVRs": "concursa",
	"SCNVRt": "medita",
	"SCNVRtn": "madura",
	"Scp": "saca",
	"SCRc": "marca",
	"SCRctn": "decora",
	"SCRsn": "clama",
	"SCRst": "incrusta",
	"SCRt": "secreta",
	"SCs": "cusa",
	"Scs": "asegura",
	"Scsn": "signa",
	"SCsn": "socializa",
	"SCstp": "encuesta",
	"SCt": "cita",
	"SCTcn": "acciona",
	"SCTct": "oculta",
	"Sctn": "distancia",
	"SCTn": "cuestiona",
	"SCtn": "acomoda",
	"SCTNc": "dedica",
	"SCTNctn": "conta",
	"SCTNn": "domina",
	"SCTNp": "disculpa",
	"SCTNRc": "clasifica",
	"SCTNRcn": "matricula",
	"SCTNRcs": "cataloga",
	"SCTNRctn": "demanda",
	"SCTNRn": "determina",
	"SCTNRsn": "escolariza",
	"SCTNRsp": "colapsa",
	"SCTNRstn": "sistematiza",
	"SCTNRt": "estimula",
	"SCTNs": "descansa",
	"SCTNst": "consta",
	"SCTNstn": "consterna",
	"SCTNt": "constata",
	"SCTNtnp": "dictamina",
	"SCTNtp": "dicta",
	"SCTNVc": "codifica",
	"SCTNVRctn": "humilla",
	"SCTNVRn": "informa",
	"SCTRt": "incita",
	"SCTt": "suscita",
	"SCTtn": "custodia",
	"SCTVc": "sacrifica",
	"SCTVRct": "rectifica",
	"SCVRsn": "firma",
	"SNcn": "nuncia",
	"SNcsn": "asigna",
	"SNcstn": "enseña",
	"SNctn": "reanuda",
	"SNnp": "ausenta",
	"SNRcn": "soluciona",
	"SNRcnp": "selecciona",
	"SNRcsn": "aleja",
	"SNRcstn": "señala",
	"SNRct": "eleva",
	"SNRctn": "asimila",
	"SNRn": "instala",
	"SNRnp": "lesiona",
	"SNRp": "impulsa",
	"SNRs": "aisla",
	"SNRsn": "solidariza",
	"SNRst": "insulta",
	"SNRstn": "saluda",
	"SNRt": "solicita",
	"SNRtn": "consolida",
	"SNsn": "remunera",
	"SNstn": "analiza",
	"SNVRc": "separa",
	"SNVRct": "releva",
	"SNVRsn": "visualiza",
	"SNVRtn": "valida",
	"SPCcs": "paga",
	"SPcn": "inspecciona",
	"SPCn": "gestiona",
	"SPCNn": "gana",
	"SPCNRc": "permane",
	"SPCNRcn": "almacena",
	"SPCNRcs": "lega",
	"SPCNRcsn": "legitima",
	"SPCNRcsp": "regala",
	"SPCNRn": "impresiona",
	"SPCNRsn": "legaliza",
	"SPCNVRc": "simplifica",
	"SPCNVRcn": "alucina",
	"SPCNVRt": "importa",
	"SPCp": "escapa",
	"SPCRct": "aproba",
	"SPCRn": "origina",
	"SPCRs": "procesa",
	"SPcs": "pega",
	"SPCs": "causa",
	"SPCsn": "estigmatiza",
	"SPCTcsn": "semeja",
	"SPCTn": "gesticula",
	"SPCTNcn": "examina",
	"SPCTNcs": "exagera",
	"SPCTNn": "reflexiona",
	"SPCTNRcs": "delega",
	"SPCTNRcstn": "extraña",
	"SPCTNRn": "explora",
	"SPCTNRs": "expulsa",
	"SPCTNRsn": "amenaza",
	"SPCTNsn": "exterioriza",
	"SPCTNt": "explota",
	"SPCTNVc": "empobre",
	"SPCTNVRctp": "asombra",
	"SPCTNVRsn": "memoriza",
	"SPCTNVRstn": "memora",
	"SPCTNVsn": "flexibiliza",
	"SPCTt": "sujeta",
	"SPCTVc": "ubica",
	"SPCTVctp": "acaba",
	"SPCTVsn": "obstaculiza",
	"SPCVRcn": "consola",
	"SPCVRn": "ilusiona",
	"SPCVRsn": "simula",
	"SPCVRt": "lamenta",
	"SPCVsn": "esquematiza",
	"SPn": "especula",
	"SPNRc": "explica",
	"SPNRcn": "amplifica",
	"SPNRctn": "apela",
	"SPNRn": "amplia",
	"SPNRs": "expresa",
	"SPNRsn": "especializa",
	"SPNRt": "experimenta",
	"SPNs": "dispensa",
	"SPNVRc": "pare",
	"SPNVRct": "persevera",
	"SPRc": "aprecia",
	"SPRct": "preserva",
	"SPRs": "precisa",
	"SPRsn": "populariza",
	"SPRsp": "prospera",
	"SPRstn": "respira",
	"SPRt": "presta",
	"SPRtn": "respalda",
	"SPs": "espera",
	"SPsn": "personaliza",
	"SPsp": "pesa",
	"SPstn": "empatiza",
	"SPt": "respeta",
	"SPTc": "apete",
	"SPTcstn": "señaliza",
	"SPTn": "estipula",
	"SPTNc": "discrepa",
	"SPTNcsnp": "despoja",
	"SPTNcstn": "desempeña",
	"SPTNRcs": "desplega",
	"SPTNRcstn": "mentaliza",
	"SPTNRsn": "localiza",
	"SPTNRt": "deposita",
	"SPTNs": "desespera",
	"SPTNsn": "desplaza",
	"SPTNstp": "despista",
	"SPTNt": "adopta",
	"SPTNVRc": "apare",
	"SPTNVRcstn": "visibiliza",
	"SPTNVRsn": "independiza",
	"SPTNVRtp": "aparenta",
	"SPTNVt": "debilita",
	"SPTRc": "mere",
	"SPTRcp": "influencia",
	"SPTRn": "razona",
	"SPTsn": "anima",
	"SPTVc": "especifica",
	"SPTVcn": "subvenciona",
	"SPTVcs": "busca",
	"SPTVcstn": "simboliza",
	"SPTVcstp": "subraya",
	"SPTVct": "observa",
	"SPTVn": "subsana",
	"SPTVsn": "sensibiliza",
	"SPTVsp": "abusa",
	"SPTVstn": "subsidia",
	"SPTVt": "subtitula",
	"SPVRsn": "responsabiliza",
	"SPVs": "supervisa",
	"SRc": "acerca",
	"SRcs": "arriesga",
	"SRcsn": "relaja",
	"SRct": "reserva",
	"SRctn": "archiva",
	"SRp": "supera",
	"SRs": "asesora",
	"SRt": "inserta",
	"SRtp": "resalta",
	"Sstn": "aspira",
	"St": "situa",
	"STc": "satisfa",
	"STcnp": "sentencia",
	"STctn": "destaca",
	"STn": "destina",
	"STNcsn": "designa",
	"STNcsnp": "despeja",
	"STNcstn": "diseña",
	"STNctn": "estudia",
	"STNRc": "dedu",
	"STNRcs": "deroga",
	"STNRcsn": "interroga",
	"STNRn": "discrimina",
	"STNRt": "titula",
	"STNRtn": "adelanta",
	"STNs": "sustenta",
	"STNsp": "desea",
	"STNst": "suministra",
	"STNstn": "desarrolla",
	"STNt": "administra",
	"STNtp": "disfruta",
	"STNRctn": "tradu",
	"STNVRc": "diversifica",
	"STNVRs": "retrasa",
	"STNVRt": "falta",
	"STNVsn": "finaliza",
	"STRc": "entriste",
	"STRcn": "estrecha",
	"STRctn": "introdu",
	"STRs": "atrasa",
	"STRsn": "autoriza",
	"STRstn": "estandariza",
	"STRt": "tramita",
	"STRtn": "traslada",
	"STRtp": "sortea",
	"STsn": "institucionaliza",
	"STst": "ostenta",
	"STstn": "sintetiza",
	"STstp": "asusta",
	"STVc": "significa",
	"STVcn": "fascina",
	"STVct": "intensifica",
	"STVctn": "indu",
	"STVRc": "ofre",
	"STVRsn": "inferioriza",
	"STVsn": "esforza",
	"STVstn": "enfatiza",
	"STVtn": "intimida",
	"SVn": "adivina",
	"SVsn": "universaliza",
	"SVt": "solventa",
	"Tcn": "contamina",
	"Tcs": "mitiga",
	"Tcsn": "cotiza",
	"Tcstn": "etiqueta",
	"Tcstp": "atisba",
	"Tctn": "detecta",
	"TNcn": "condena",
	"TNcsn": "deja",
	"TNcstp": "entusiasma",
	"TNctn": "edita",
	"TNRc": "redu",
	"TNRcs": "integra",
	"TNRcstn": "entraña",
	"TNRct": "deriva",
	"TNRctn": "redacta",
	"TNRn": "interna",
	"TNRp": "educa",
	"TNRs": "interesa",
	"TNRsn": "utiliza",
	"TNRst": "ilustra",
	"TNRstn": "tolera",
	"TNRt": "orienta",
	"TNRtn": "intenta",
	"TNRtp": "derrota",
	"TNstnp": "deteriora",
	"TNstp": "desafia",
	"TNt": "entera",
	"TNVcs": "divulga",
	"TNVcsn": "homenajea",
	"TNVcsp": "halla",
	"TNVct": "identifica",
	"TNVctn": "edifica",
	"TNVctp": "habla",
	"TNVRc": "diferencia",
	"TNVRcs": "otorga",
	"TNVRcsn": "focaliza",
	"TNVRcstn": "eterniza",
	"TNVRct": "felicita",
	"TNVRctp": "derriba",
	"TNVRsn": "familiariza",
	"TNVRsnp": "horroriza",
	"TNVRstn": "hospitaliza",
	"TNVRt": "rehabilita",
	"TNVRtn": "hereda",
	"TNVsn": "humaniza",
	"TNVstn": "ahorra",
	"TNVt": "habilita",
	"TRcn": "articula",
	"TRcs": "entrega",
	"TRcstn": "tranquiliza",
	"TRctn": "entra",
	"TRctp": "trabaja",
	"TRsn": "industrializa",
	"TRsnp": "atemoriza",
	"TRstn": "trastorna",
	"TRt": "trata",
	"TRtn": "reitera",
	"TRtnp": "tarda",
	"TRtp": "tortura",
	"Tsn": "aumenta",
	"Tsnp": "toma",
	"Tt": "estructura",
	"TVRc": "favore",
	"TVcn": "funciona",
	"TVcnp": "confecciona",
	"TVcp": "fomenta",
	"TVcsn": "fija",
	"TVcsp": "falla",
	"TVctn": "afecta",
	"TVRcsn": "refleja",
	"TVRcsp": "fracasa",
	"TVRcst": "fragmenta",
	"TVRctn": "defrauda",
	"TVRs": "atravesa",
	"TVRsn": "afirma",
	"TVRstp": "entrevista",
	"TVRt": "afronta",
	"TVRtn": "enfrenta",
	"TVsn": "profundiza",
	"TVstn": "alfabetiza",
	"TVt": "efectua",
	"Vc": "voca",
	"Vcn": "aprovecha",
	"Vcs": "investiga",
	"Vcsn": "viaja",
	"Vcstn": "aventaja",
	"Vctn": "reivindica",
	"VRc": "verifica",
	"VRcn": "revoluciona",
	"VRct": "valora",
	"VRn": "vulnera",
	"VRs": "revisa",
	"VRsn": "verbaliza",
	"VRt": "vota",
	"Vs": "avisa",
	"Vsn": "avanza",
	"Vst": "visita",
	"Vstn": "varia"
}


adjs = {
	"respeta": "respetuo",
	"numera": "numero",
	"genera": "genero",
	"beneficia": "beneficio",
	"trabaja": "trabajo",
	"aprovecha": "provecho",
	"estudia": "estudio",
	"afecta": "afectuo",
	"desea": "deseo",
	"infecta": "infeccio",
	"engaña": "engaño",
	"aventaja": "ventajo",
	"forza": "forzo",
	"goza": "gozo",
	"peligra": "peligro",
	"apena": "peno",
	"decora": "decoro",
	"asombra": "asombro"
}

irregular = {
	"acorda": "acuerd",
	"aproba": "aprueb",
	"aposta": "apuest",
	"comproba": "comprueb",
	"consola": "consuel",
	"conta": "cuent",
	"demostra": "demuestr",
	"encontra": "encuentr",
	"esforza": "esfuerc",
	"forca": "fuerc",
	"juga": "juegu",
	"proba": "prueb",
	"recorda": "recuerd",
	"renova": "renuev"
}

def lookup(key):
	if doubleStrokes.get(key[0]) is None:
		raise KeyError
	spanish_mqd_single.lastValue = doubleStrokes.get(key[0])
	if len(key) == 1 or key[1] == "*":
		return " "
	value = spanish_mqd_single.searchKey(spanish_mqd_single.dict, key[1])
	if spanish_mqd_single.lastValue.endswith("a") and value[0] in VOWELS:
		if irregular.get(spanish_mqd_single.lastValue) and value in ("en ", "es "):
			value = irregular[spanish_mqd_single.lastValue] + value
		elif spanish_mqd_single.lastValue.endswith("ga") and value[0] == "e":
			value = spanish_mqd_single.lastValue[:-1] + "u" + value
		elif spanish_mqd_single.lastValue.endswith("za") and value[0] == "e":
			value = spanish_mqd_single.lastValue[:-2] + "c" + value
		else:
			value = spanish_mqd_single.lastValue[:-1] + value
	elif adjs.get(spanish_mqd_single.lastValue) is not None and value[:2] in ("sa", "si", "sí", "so"):
		value = adjs.get(spanish_mqd_single.lastValue) + value
	elif spanish_mqd_single.lastValue[-1] in ("e", "o") and value[0] == "a":
		value = spanish_mqd_single.lastValue + "zc" + value
	else:
		value = spanish_mqd_single.lastValue + value
	if not value.endswith(" "):
		value = value + "{^}"
	return value
