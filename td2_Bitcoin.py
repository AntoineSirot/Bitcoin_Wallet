import secrets
import hashlib
import binascii
import sys
import codecs
#!pip install ecdsa
import ecdsa





def padd_binary(bin_str: str, size: int) -> str:
    """
    Pads a binary string with zeros to the left
    :param bin_str: binary string to pad
    :param size: size of the padded string
    :return: padded binary string
    """
    for _ in range(size - len(bin_str)):
        bin_str = '0' + bin_str
    return bin_str

def byte_to_binary(b: bytes, size: int) -> str:
    """
    Converts a byte to a binary string
    :param byte: byte to convert
    :param size: size of the binary string
    :return: binary string
    """
    order = -1 if sys.byteorder == 'little' else 1
    bin_n = bin(int.from_bytes(b, byteorder='big'))[2:]
    return padd_binary(bin_n, size)

#### PRESENTATION ####
print("TD2_Blockchain_Programming\nRodrigues Thomas & Sirot Antoine\n")


# CREATION ENTIER ALEATOIRE #
print("\n Création de la Seed...\n")
seed = secrets.token_bytes(16)

# CONVERSION DE LA SEED EN BINAIRE #
binSeed = byte_to_binary(seed,128) # Renvoie nombre binaire aléatoire à 128bits
print("Valeur de la seed en binaire : " + binSeed)
print("Valeur de la seed en base 10 : " + str(int(binSeed,2))) # Conversion du nombre en base 10

print("\n\n Création du Hash de la Seed...")
hashSeed = hashlib.sha256(seed).digest() # Utilisation de Sha256 pour hasher la Seed
print("\nValeur du Hash de la seed : " + str(hashSeed))
binhashSeed = byte_to_binary(hashSeed, 256) # Conversion du hash en binaire
print("Valeur du Hash de la seed en binaire : " + binhashSeed)
EntCheck = binSeed + binhashSeed[:4]
print("Entropie + Checksum en binaire : " + EntCheck) # Ajout du Checksum à l'entropie
Splited = ['0','0','0','0','0','0','0','0','0','0','0','0']
for j in range(12) :
  Splited[j] = EntCheck[11*j:(j+1)*11] # Séparation de l'Entropie + Checksum en groupe de 11bits

# DICTIONNAIRE BIP39
bip39wordlist = [ "abandon",  "ability",  "able",     "about",    "above",    "absent",   "absorb",   "abstract", 
    "absurd",   "abuse",    "access",   "accident", "account",  "accuse",   "achieve",  "acid",     
    "acoustic", "acquire",  "across",   "act",      "action",   "actor",    "actress",  "actual",   
    "adapt",    "add",      "addict",   "address",  "adjust",   "admit",    "adult",    "advance",  
    "advice",   "aerobic",  "affair",   "afford",   "afraid",   "again",    "age",      "agent",    
    "agree",    "ahead",    "aim",      "air",      "airport",  "aisle",    "alarm",    "album",    
    "alcohol",  "alert",    "alien",    "all",      "alley",    "allow",    "almost",   "alone",    
    "alpha",    "already",  "also",     "alter",    "always",   "amateur",  "amazing",  "among",    
    "amount",   "amused",   "analyst",  "anchor",   "ancient",  "anger",    "angle",    "angry",    
    "animal",   "ankle",    "announce", "annual",   "another",  "answer",   "antenna",  "antique",  
    "anxiety",  "any",      "apart",    "apology",  "appear",   "apple",    "approve",  "april",    
    "arch",     "arctic",   "area",     "arena",    "argue",    "arm",      "armed",    "armor",    
    "army",     "around",   "arrange",  "arrest",   "arrive",   "arrow",    "art",      "artefact", 
    "artist",   "artwork",  "ask",      "aspect",   "assault",  "asset",    "assist",   "assume",   
    "asthma",   "athlete",  "atom",     "attack",   "attend",   "attitude", "attract",  "auction",  
    "audit",    "august",   "aunt",     "author",   "auto",     "autumn",   "average",  "avocado",  
    "avoid",    "awake",    "aware",    "away",     "awesome",  "awful",    "awkward",  "axis",     
    "baby",     "bachelor", "bacon",    "badge",    "bag",      "balance",  "balcony",  "ball",     
    "bamboo",   "banana",   "banner",   "bar",      "barely",   "bargain",  "barrel",   "base",     
    "basic",    "basket",   "battle",   "beach",    "bean",     "beauty",   "because",  "become",   
    "beef",     "before",   "begin",    "behave",   "behind",   "believe",  "below",    "belt",     
    "bench",    "benefit",  "best",     "betray",   "better",   "between",  "beyond",   "bicycle",  
    "bid",      "bike",     "bind",     "biology",  "bird",     "birth",    "bitter",   "black",    
    "blade",    "blame",    "blanket",  "blast",    "bleak",    "bless",    "blind",    "blood",    
    "blossom",  "blouse",   "blue",     "blur",     "blush",    "board",    "boat",     "body",     
    "boil",     "bomb",     "bone",     "bonus",    "book",     "boost",    "border",   "boring",   
    "borrow",   "boss",     "bottom",   "bounce",   "box",      "boy",      "bracket",  "brain",    
    "brand",    "brass",    "brave",    "bread",    "breeze",   "brick",    "bridge",   "brief",    
    "bright",   "bring",    "brisk",    "broccoli", "broken",   "bronze",   "broom",    "brother",  
    "brown",    "brush",    "bubble",   "buddy",    "budget",   "buffalo",  "build",    "bulb",     
    "bulk",     "bullet",   "bundle",   "bunker",   "burden",   "burger",   "burst",    "bus",      
    "business", "busy",     "butter",   "buyer",    "buzz",     "cabbage",  "cabin",    "cable",    
    "cactus",   "cage",     "cake",     "call",     "calm",     "camera",   "camp",     "can",      
    "canal",    "cancel",   "candy",    "cannon",   "canoe",    "canvas",   "canyon",   "capable",  
    "capital",  "captain",  "car",      "carbon",   "card",     "cargo",    "carpet",   "carry",    
    "cart",     "case",     "cash",     "casino",   "castle",   "casual",   "cat",      "catalog",  
    "catch",    "category", "cattle",   "caught",   "cause",    "caution",  "cave",     "ceiling",  
    "celery",   "cement",   "census",   "century",  "cereal",   "certain",  "chair",    "chalk",    
    "champion", "change",   "chaos",    "chapter",  "charge",   "chase",    "chat",     "cheap",    
    "check",    "cheese",   "chef",     "cherry",   "chest",    "chicken",  "chief",    "child",    
    "chimney",  "choice",   "choose",   "chronic",  "chuckle",  "chunk",    "churn",    "cigar",    
    "cinnamon", "circle",   "citizen",  "city",     "civil",    "claim",    "clap",     "clarify",  
    "claw",     "clay",     "clean",    "clerk",    "clever",   "click",    "client",   "cliff",    
    "climb",    "clinic",   "clip",     "clock",    "clog",     "close",    "cloth",    "cloud",    
    "clown",    "club",     "clump",    "cluster",  "clutch",   "coach",    "coast",    "coconut",  
    "code",     "coffee",   "coil",     "coin",     "collect",  "color",    "column",   "combine",  
    "come",     "comfort",  "comic",    "common",   "company",  "concert",  "conduct",  "confirm",  
    "congress", "connect",  "consider", "control",  "convince", "cook",     "cool",     "copper",   
    "copy",     "coral",    "core",     "corn",     "correct",  "cost",     "cotton",   "couch",    
    "country",  "couple",   "course",   "cousin",   "cover",    "coyote",   "crack",    "cradle",   
    "craft",    "cram",     "crane",    "crash",    "crater",   "crawl",    "crazy",    "cream",    
    "credit",   "creek",    "crew",     "cricket",  "crime",    "crisp",    "critic",   "crop",     
    "cross",    "crouch",   "crowd",    "crucial",  "cruel",    "cruise",   "crumble",  "crunch",   
    "crush",    "cry",      "crystal",  "cube",     "culture",  "cup",      "cupboard", "curious",  
    "current",  "curtain",  "curve",    "cushion",  "custom",   "cute",     "cycle",    "dad",      
    "damage",   "damp",     "dance",    "danger",   "daring",   "dash",     "daughter", "dawn",     
    "day",      "deal",     "debate",   "debris",   "decade",   "december", "decide",   "decline",  
    "decorate", "decrease", "deer",     "defense",  "define",   "defy",     "degree",   "delay",    
    "deliver",  "demand",   "demise",   "denial",   "dentist",  "deny",     "depart",   "depend",   
    "deposit",  "depth",    "deputy",   "derive",   "describe", "desert",   "design",   "desk",     
    "despair",  "destroy",  "detail",   "detect",   "develop",  "device",   "devote",   "diagram",  
    "dial",     "diamond",  "diary",    "dice",     "diesel",   "diet",     "differ",   "digital",  
    "dignity",  "dilemma",  "dinner",   "dinosaur", "direct",   "dirt",     "disagree", "discover", 
    "disease",  "dish",     "dismiss",  "disorder", "display",  "distance", "divert",   "divide",   
    "divorce",  "dizzy",    "doctor",   "document", "dog",      "doll",     "dolphin",  "domain",   
    "donate",   "donkey",   "donor",    "door",     "dose",     "double",   "dove",     "draft",    
    "dragon",   "drama",    "drastic",  "draw",     "dream",    "dress",    "drift",    "drill",    
    "drink",    "drip",     "drive",    "drop",     "drum",     "dry",      "duck",     "dumb",     
    "dune",     "during",   "dust",     "dutch",    "duty",     "dwarf",    "dynamic",  "eager",    
    "eagle",    "early",    "earn",     "earth",    "easily",   "east",     "easy",     "echo",     
    "ecology",  "economy",  "edge",     "edit",     "educate",  "effort",   "egg",      "eight",    
    "either",   "elbow",    "elder",    "electric", "elegant",  "element",  "elephant", "elevator", 
    "elite",    "else",     "embark",   "embody",   "embrace",  "emerge",   "emotion",  "employ",   
    "empower",  "empty",    "enable",   "enact",    "end",      "endless",  "endorse",  "enemy",    
    "energy",   "enforce",  "engage",   "engine",   "enhance",  "enjoy",    "enlist",   "enough",   
    "enrich",   "enroll",   "ensure",   "enter",    "entire",   "entry",    "envelope", "episode",  
    "equal",    "equip",    "era",      "erase",    "erode",    "erosion",  "error",    "erupt",    
    "escape",   "essay",    "essence",  "estate",   "eternal",  "ethics",   "evidence", "evil",     
    "evoke",    "evolve",   "exact",    "example",  "excess",   "exchange", "excite",   "exclude",  
    "excuse",   "execute",  "exercise", "exhaust",  "exhibit",  "exile",    "exist",    "exit",     
    "exotic",   "expand",   "expect",   "expire",   "explain",  "expose",   "express",  "extend",   
    "extra",    "eye",      "eyebrow",  "fabric",   "face",     "faculty",  "fade",     "faint",    
    "faith",    "fall",     "false",    "fame",     "family",   "famous",   "fan",      "fancy",    
    "fantasy",  "farm",     "fashion",  "fat",      "fatal",    "father",   "fatigue",  "fault",    
    "favorite", "feature",  "february", "federal",  "fee",      "feed",     "feel",     "female",   
    "fence",    "festival", "fetch",    "fever",    "few",      "fiber",    "fiction",  "field",    
    "figure",   "file",     "film",     "filter",   "final",    "find",     "fine",     "finger",   
    "finish",   "fire",     "firm",     "first",    "fiscal",   "fish",     "fit",      "fitness",  
    "fix",      "flag",     "flame",    "flash",    "flat",     "flavor",   "flee",     "flight",   
    "flip",     "float",    "flock",    "floor",    "flower",   "fluid",    "flush",    "fly",      
    "foam",     "focus",    "fog",      "foil",     "fold",     "follow",   "food",     "foot",     
    "force",    "forest",   "forget",   "fork",     "fortune",  "forum",    "forward",  "fossil",   
    "foster",   "found",    "fox",      "fragile",  "frame",    "frequent", "fresh",    "friend",   
    "fringe",   "frog",     "front",    "frost",    "frown",    "frozen",   "fruit",    "fuel",     
    "fun",      "funny",    "furnace",  "fury",     "future",   "gadget",   "gain",     "galaxy",   
    "gallery",  "game",     "gap",      "garage",   "garbage",  "garden",   "garlic",   "garment",  
    "gas",      "gasp",     "gate",     "gather",   "gauge",    "gaze",     "general",  "genius",   
    "genre",    "gentle",   "genuine",  "gesture",  "ghost",    "giant",    "gift",     "giggle",   
    "ginger",   "giraffe",  "girl",     "give",     "glad",     "glance",   "glare",    "glass",    
    "glide",    "glimpse",  "globe",    "gloom",    "glory",    "glove",    "glow",     "glue",     
    "goat",     "goddess",  "gold",     "good",     "goose",    "gorilla",  "gospel",   "gossip",   
    "govern",   "gown",     "grab",     "grace",    "grain",    "grant",    "grape",    "grass",    
    "gravity",  "great",    "green",    "grid",     "grief",    "grit",     "grocery",  "group",    
    "grow",     "grunt",    "guard",    "guess",    "guide",    "guilt",    "guitar",   "gun",      
    "gym",      "habit",    "hair",     "half",     "hammer",   "hamster",  "hand",     "happy",    
    "harbor",   "hard",     "harsh",    "harvest",  "hat",      "have",     "hawk",     "hazard",   
    "head",     "health",   "heart",    "heavy",    "hedgehog", "height",   "hello",    "helmet",   
    "help",     "hen",      "hero",     "hidden",   "high",     "hill",     "hint",     "hip",      
    "hire",     "history",  "hobby",    "hockey",   "hold",     "hole",     "holiday",  "hollow",   
    "home",     "honey",    "hood",     "hope",     "horn",     "horror",   "horse",    "hospital", 
    "host",     "hotel",    "hour",     "hover",    "hub",      "huge",     "human",    "humble",   
    "humor",    "hundred",  "hungry",   "hunt",     "hurdle",   "hurry",    "hurt",     "husband",  
    "hybrid",   "ice",      "icon",     "idea",     "identify", "idle",     "ignore",   "ill",      
    "illegal",  "illness",  "image",    "imitate",  "immense",  "immune",   "impact",   "impose",   
    "improve",  "impulse",  "inch",     "include",  "income",   "increase", "index",    "indicate", 
    "indoor",   "industry", "infant",   "inflict",  "inform",   "inhale",   "inherit",  "initial",  
    "inject",   "injury",   "inmate",   "inner",    "innocent", "input",    "inquiry",  "insane",   
    "insect",   "inside",   "inspire",  "install",  "intact",   "interest", "into",     "invest",   
    "invite",   "involve",  "iron",     "island",   "isolate",  "issue",    "item",     "ivory",    
    "jacket",   "jaguar",   "jar",      "jazz",     "jealous",  "jeans",    "jelly",    "jewel",    
    "job",      "join",     "joke",     "journey",  "joy",      "judge",    "juice",    "jump",     
    "jungle",   "junior",   "junk",     "just",     "kangaroo", "keen",     "keep",     "ketchup",  
    "key",      "kick",     "kid",      "kidney",   "kind",     "kingdom",  "kiss",     "kit",      
    "kitchen",  "kite",     "kitten",   "kiwi",     "knee",     "knife",    "knock",    "know",     
    "lab",      "label",    "labor",    "ladder",   "lady",     "lake",     "lamp",     "language", 
    "laptop",   "large",    "later",    "latin",    "laugh",    "laundry",  "lava",     "law",      
    "lawn",     "lawsuit",  "layer",    "lazy",     "leader",   "leaf",     "learn",    "leave",    
    "lecture",  "left",     "leg",      "legal",    "legend",   "leisure",  "lemon",    "lend",     
    "length",   "lens",     "leopard",  "lesson",   "letter",   "level",    "liar",     "liberty",  
    "library",  "license",  "life",     "lift",     "light",    "like",     "limb",     "limit",    
    "link",     "lion",     "liquid",   "list",     "little",   "live",     "lizard",   "load",     
    "loan",     "lobster",  "local",    "lock",     "logic",    "lonely",   "long",     "loop",     
    "lottery",  "loud",     "lounge",   "love",     "loyal",    "lucky",    "luggage",  "lumber",   
    "lunar",    "lunch",    "luxury",   "lyrics",   "machine",  "mad",      "magic",    "magnet",   
    "maid",     "mail",     "main",     "major",    "make",     "mammal",   "man",      "manage",   
    "mandate",  "mango",    "mansion",  "manual",   "maple",    "marble",   "march",    "margin",   
    "marine",   "market",   "marriage", "mask",     "mass",     "master",   "match",    "material", 
    "math",     "matrix",   "matter",   "maximum",  "maze",     "meadow",   "mean",     "measure",  
    "meat",     "mechanic", "medal",    "media",    "melody",   "melt",     "member",   "memory",   
    "mention",  "menu",     "mercy",    "merge",    "merit",    "merry",    "mesh",     "message",  
    "metal",    "method",   "middle",   "midnight", "milk",     "million",  "mimic",    "mind",     
    "minimum",  "minor",    "minute",   "miracle",  "mirror",   "misery",   "miss",     "mistake",  
    "mix",      "mixed",    "mixture",  "mobile",   "model",    "modify",   "mom",      "moment",   
    "monitor",  "monkey",   "monster",  "month",    "moon",     "moral",    "more",     "morning",  
    "mosquito", "mother",   "motion",   "motor",    "mountain", "mouse",    "move",     "movie",    
    "much",     "muffin",   "mule",     "multiply", "muscle",   "museum",   "mushroom", "music",    
    "must",     "mutual",   "myself",   "mystery",  "myth",     "naive",    "name",     "napkin",   
    "narrow",   "nasty",    "nation",   "nature",   "near",     "neck",     "need",     "negative", 
    "neglect",  "neither",  "nephew",   "nerve",    "nest",     "net",      "network",  "neutral",  
    "never",    "news",     "next",     "nice",     "night",    "noble",    "noise",    "nominee",  
    "noodle",   "normal",   "north",    "nose",     "notable",  "note",     "nothing",  "notice",   
    "novel",    "now",      "nuclear",  "number",   "nurse",    "nut",      "oak",      "obey",     
    "object",   "oblige",   "obscure",  "observe",  "obtain",   "obvious",  "occur",    "ocean",    
    "october",  "odor",     "off",      "offer",    "office",   "often",    "oil",      "okay",     
    "old",      "olive",    "olympic",  "omit",     "once",     "one",      "onion",    "online",   
    "only",     "open",     "opera",    "opinion",  "oppose",   "option",   "orange",   "orbit",    
    "orchard",  "order",    "ordinary", "organ",    "orient",   "original", "orphan",   "ostrich",  
    "other",    "outdoor",  "outer",    "output",   "outside",  "oval",     "oven",     "over",     
    "own",      "owner",    "oxygen",   "oyster",   "ozone",    "pact",     "paddle",   "page",     
    "pair",     "palace",   "palm",     "panda",    "panel",    "panic",    "panther",  "paper",    
    "parade",   "parent",   "park",     "parrot",   "party",    "pass",     "patch",    "path",     
    "patient",  "patrol",   "pattern",  "pause",    "pave",     "payment",  "peace",    "peanut",   
    "pear",     "peasant",  "pelican",  "pen",      "penalty",  "pencil",   "people",   "pepper",   
    "perfect",  "permit",   "person",   "pet",      "phone",    "photo",    "phrase",   "physical", 
    "piano",    "picnic",   "picture",  "piece",    "pig",      "pigeon",   "pill",     "pilot",    
    "pink",     "pioneer",  "pipe",     "pistol",   "pitch",    "pizza",    "place",    "planet",   
    "plastic",  "plate",    "play",     "please",   "pledge",   "pluck",    "plug",     "plunge",   
    "poem",     "poet",     "point",    "polar",    "pole",     "police",   "pond",     "pony",     
    "pool",     "popular",  "portion",  "position", "possible", "post",     "potato",   "pottery",  
    "poverty",  "powder",   "power",    "practice", "praise",   "predict",  "prefer",   "prepare",  
    "present",  "pretty",   "prevent",  "price",    "pride",    "primary",  "print",    "priority", 
    "prison",   "private",  "prize",    "problem",  "process",  "produce",  "profit",   "program",  
    "project",  "promote",  "proof",    "property", "prosper",  "protect",  "proud",    "provide",  
    "public",   "pudding",  "pull",     "pulp",     "pulse",    "pumpkin",  "punch",    "pupil",    
    "puppy",    "purchase", "purity",   "purpose",  "purse",    "push",     "put",      "puzzle",   
    "pyramid",  "quality",  "quantum",  "quarter",  "question", "quick",    "quit",     "quiz",     
    "quote",    "rabbit",   "raccoon",  "race",     "rack",     "radar",    "radio",    "rail",     
    "rain",     "raise",    "rally",    "ramp",     "ranch",    "random",   "range",    "rapid",    
    "rare",     "rate",     "rather",   "raven",    "raw",      "razor",    "ready",    "real",     
    "reason",   "rebel",    "rebuild",  "recall",   "receive",  "recipe",   "record",   "recycle",  
    "reduce",   "reflect",  "reform",   "refuse",   "region",   "regret",   "regular",  "reject",   
    "relax",    "release",  "relief",   "rely",     "remain",   "remember", "remind",   "remove",   
    "render",   "renew",    "rent",     "reopen",   "repair",   "repeat",   "replace",  "report",   
    "require",  "rescue",   "resemble", "resist",   "resource", "response", "result",   "retire",   
    "retreat",  "return",   "reunion",  "reveal",   "review",   "reward",   "rhythm",   "rib",      
    "ribbon",   "rice",     "rich",     "ride",     "ridge",    "rifle",    "right",    "rigid",    
    "ring",     "riot",     "ripple",   "risk",     "ritual",   "rival",    "river",    "road",     
    "roast",    "robot",    "robust",   "rocket",   "romance",  "roof",     "rookie",   "room",     
    "rose",     "rotate",   "rough",    "round",    "route",    "royal",    "rubber",   "rude",     
    "rug",      "rule",     "run",      "runway",   "rural",    "sad",      "saddle",   "sadness",  
    "safe",     "sail",     "salad",    "salmon",   "salon",    "salt",     "salute",   "same",     
    "sample",   "sand",     "satisfy",  "satoshi",  "sauce",    "sausage",  "save",     "say",      
    "scale",    "scan",     "scare",    "scatter",  "scene",    "scheme",   "school",   "science",  
    "scissors", "scorpion", "scout",    "scrap",    "screen",   "script",   "scrub",    "sea",      
    "search",   "season",   "seat",     "second",   "secret",   "section",  "security", "seed",     
    "seek",     "segment",  "select",   "sell",     "seminar",  "senior",   "sense",    "sentence", 
    "series",   "service",  "session",  "settle",   "setup",    "seven",    "shadow",   "shaft",    
    "shallow",  "share",    "shed",     "shell",    "sheriff",  "shield",   "shift",    "shine",    
    "ship",     "shiver",   "shock",    "shoe",     "shoot",    "shop",     "short",    "shoulder", 
    "shove",    "shrimp",   "shrug",    "shuffle",  "shy",      "sibling",  "sick",     "side",     
    "siege",    "sight",    "sign",     "silent",   "silk",     "silly",    "silver",   "similar",  
    "simple",   "since",    "sing",     "siren",    "sister",   "situate",  "six",      "size",     
    "skate",    "sketch",   "ski",      "skill",    "skin",     "skirt",    "skull",    "slab",     
    "slam",     "sleep",    "slender",  "slice",    "slide",    "slight",   "slim",     "slogan",   
    "slot",     "slow",     "slush",    "small",    "smart",    "smile",    "smoke",    "smooth",   
    "snack",    "snake",    "snap",     "sniff",    "snow",     "soap",     "soccer",   "social",   
    "sock",     "soda",     "soft",     "solar",    "soldier",  "solid",    "solution", "solve",    
    "someone",  "song",     "soon",     "sorry",    "sort",     "soul",     "sound",    "soup",     
    "source",   "south",    "space",    "spare",    "spatial",  "spawn",    "speak",    "special",  
    "speed",    "spell",    "spend",    "sphere",   "spice",    "spider",   "spike",    "spin",     
    "spirit",   "split",    "spoil",    "sponsor",  "spoon",    "sport",    "spot",     "spray",    
    "spread",   "spring",   "spy",      "square",   "squeeze",  "squirrel", "stable",   "stadium",  
    "staff",    "stage",    "stairs",   "stamp",    "stand",    "start",    "state",    "stay",     
    "steak",    "steel",    "stem",     "step",     "stereo",   "stick",    "still",    "sting",    
    "stock",    "stomach",  "stone",    "stool",    "story",    "stove",    "strategy", "street",   
    "strike",   "strong",   "struggle", "student",  "stuff",    "stumble",  "style",    "subject",  
    "submit",   "subway",   "success",  "such",     "sudden",   "suffer",   "sugar",    "suggest",  
    "suit",     "summer",   "sun",      "sunny",    "sunset",   "super",    "supply",   "supreme",  
    "sure",     "surface",  "surge",    "surprise", "surround", "survey",   "suspect",  "sustain",  
    "swallow",  "swamp",    "swap",     "swarm",    "swear",    "sweet",    "swift",    "swim",     
    "swing",    "switch",   "sword",    "symbol",   "symptom",  "syrup",    "system",   "table",    
    "tackle",   "tag",      "tail",     "talent",   "talk",     "tank",     "tape",     "target",   
    "task",     "taste",    "tattoo",   "taxi",     "teach",    "team",     "tell",     "ten",      
    "tenant",   "tennis",   "tent",     "term",     "test",     "text",     "thank",    "that",     
    "theme",    "then",     "theory",   "there",    "they",     "thing",    "this",     "thought",  
    "three",    "thrive",   "throw",    "thumb",    "thunder",  "ticket",   "tide",     "tiger",    
    "tilt",     "timber",   "time",     "tiny",     "tip",      "tired",    "tissue",   "title",    
    "toast",    "tobacco",  "today",    "toddler",  "toe",      "together", "toilet",   "token",    
    "tomato",   "tomorrow", "tone",     "tongue",   "tonight",  "tool",     "tooth",    "top",      
    "topic",    "topple",   "torch",    "tornado",  "tortoise", "toss",     "total",    "tourist",  
    "toward",   "tower",    "town",     "toy",      "track",    "trade",    "traffic",  "tragic",   
    "train",    "transfer", "trap",     "trash",    "travel",   "tray",     "treat",    "tree",     
    "trend",    "trial",    "tribe",    "trick",    "trigger",  "trim",     "trip",     "trophy",   
    "trouble",  "truck",    "true",     "truly",    "trumpet",  "trust",    "truth",    "try",      
    "tube",     "tuition",  "tumble",   "tuna",     "tunnel",   "turkey",   "turn",     "turtle",   
    "twelve",   "twenty",   "twice",    "twin",     "twist",    "two",      "type",     "typical",  
    "ugly",     "umbrella", "unable",   "unaware",  "uncle",    "uncover",  "under",    "undo",     
    "unfair",   "unfold",   "unhappy",  "uniform",  "unique",   "unit",     "universe", "unknown",  
    "unlock",   "until",    "unusual",  "unveil",   "update",   "upgrade",  "uphold",   "upon",     
    "upper",    "upset",    "urban",    "urge",     "usage",    "use",      "used",     "useful",   
    "useless",  "usual",    "utility",  "vacant",   "vacuum",   "vague",    "valid",    "valley",   
    "valve",    "van",      "vanish",   "vapor",    "various",  "vast",     "vault",    "vehicle",  
    "velvet",   "vendor",   "venture",  "venue",    "verb",     "verify",   "version",  "very",     
    "vessel",   "veteran",  "viable",   "vibrant",  "vicious",  "victory",  "video",    "view",     
    "village",  "vintage",  "violin",   "virtual",  "virus",    "visa",     "visit",    "visual",   
    "vital",    "vivid",    "vocal",    "voice",    "void",     "volcano",  "volume",   "vote",     
    "voyage",   "wage",     "wagon",    "wait",     "walk",     "wall",     "walnut",   "want",     
    "warfare",  "warm",     "warrior",  "wash",     "wasp",     "waste",    "water",    "wave",     
    "way",      "wealth",   "weapon",   "wear",     "weasel",   "weather",  "web",      "wedding",  
    "weekend",  "weird",    "welcome",  "west",     "wet",      "whale",    "what",     "wheat",    
    "wheel",    "when",     "where",    "whip",     "whisper",  "wide",     "width",    "wife",     
    "wild",     "will",     "win",      "window",   "wine",     "wing",     "wink",     "winner",   
    "winter",   "wire",     "wisdom",   "wise",     "wish",     "witness",  "wolf",     "woman",    
    "wonder",   "wood",     "wool",     "word",     "work",     "world",    "worry",    "worth",    
    "wrap",     "wreck",    "wrestle",  "wrist",    "write",    "wrong",    "yard",     "year",     
    "yellow",   "you",      "young",    "youth",    "zebra",    "zero",     "zone",     "zoo"  ]

  
# ATTRIBUTION DES MOTS #
print("\n\n Création de la phrase mnémonique...\n")
print("Liste Binaire pour la phrase mnémonique : " + str(Splited))
j = 0
for i in Splited :
    Splited[j] = int(Splited[j],2) # Conversion de l'Entropie + Checksum en binaire en décimal
    j = j+1
words = [bip39wordlist[Splited[i]] for i in range(0, len(Splited))] # Attribution des mots par rapport au nombre 
word_string = ' '.join(words) # Réunification de la liste pour former une phrase mnémonique
print("Phrase mnémonique : " + word_string)


# EXTRACTION DE LA MASTER PRIVATE KEY ET DU CHAIN CODE #
print("\n\n Extraction de la master private key et du chain code...\n")
hashSha512 = hashlib.sha512( word_string.encode("utf-8") ).hexdigest() # Encodage du mnémonique avec Sha512
print("Hash Sha512 : " + hashSha512) # Récupération du Hash total
masterprivatekey = hashSha512[0:len(hashSha512)//2]
print("Master private key (partie gauche) : " + masterprivatekey) # Partie gauche du Hash total
chaincode = hashSha512[len(hashSha512)//2:]
print("Chain Code (partie droite) : " + chaincode) # Partie droite du Hash total


# EXCTRACTION DE LA MASTER PUBLIC KEY #
print("\n\n Extraction de la master public key...\n")
private_key_bytes = codecs.decode(masterprivatekey, 'hex') # Décodage de la clé privée en bits
public_key_raw = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key # Génération de la public key avec SECP256k1 la courbe eliptique utilisée par Bitcoin
public_key_bytes = public_key_raw.to_string() # Mise en string
public_key_hex = codecs.encode(public_key_bytes, 'hex') # Encodage de la public key en bits
public_key = (b'04' + public_key_hex).decode("utf-8") # Ajout des bits '0x04' au départ car c'est une public key pout Bitcoin
# Regard si le dernier bit est égal ou différent
if (ord(bytearray.fromhex(public_key[-2:])) % 2 == 0):
    public_key_compressed = '02'
else:
    public_key_compressed = '03'
    
public_key_compressed += public_key[2:66] #Récupération de la partie voulue pour la public key compressed
print("Master public key compressed : " + public_key_compressed)

# GENERATION D'UNE CLE ENFANT #
print("\n\n Génération d'une clé enfant...\n")
NewhashSha512 = hashlib.sha512( (public_key + chaincode).encode("utf-8") ).hexdigest() # Encodage de la public key parent + chaincode + index avec Sha512
print("Hash512 pour les clés enfants : " + str(NewhashSha512))
childprivatekey = NewhashSha512[:len(NewhashSha512)//2]
print("Child Private Key (partie gauche) : " + childprivatekey)
childchaincode = NewhashSha512[len(NewhashSha512)//2:]
print("Child chaincode : " + childchaincode)

# GENERATION D'UNE CLE ENFANT A INDEX N #
print("\n\n Génération d'une clé enfant a index n...\n")
index = padd_binary(format(int(input(print("Index voulu pour la clé enfant : "))),'b'),32) #Récupération de l'index puis conversion en binaire sur 32 bits
print("Index en binaire sur 32 bits : " + index)
NewhashSha512 = hashlib.sha512( (public_key + chaincode + index).encode("utf-8") ).hexdigest() # Encodage de la public key parent + chaincode + index avec Sha512
print("Hash512 pour les clés enfants : " + str(NewhashSha512))
childprivatekey = NewhashSha512[:len(NewhashSha512)//2]
print("Child Private Key (partie gauche) : " + childprivatekey)
childchaincode = NewhashSha512[len(NewhashSha512)//2:]
print("Child chaincode (partie droite) : " + childchaincode)


