import random

def generate_random_text(
		num_words=1,
		the_words=None,
		include_punctuation=False,
		include_digits=False):
	text = ""
	words = [
		"the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it","for", "not", "on", "with", 
		"as", "you", "do", "at", "this", "but", "his", "by", "from", "us", "we", "say", "her", "she", "or",
		"an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", 
		"who", "get", "which", "go", "me", "when", "make", "can", "like", "he", "time", "no", "just", "him", "know",
		"take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", 
		"then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use",
		"two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", 
		"these", "give", "day", "most", "they",
	]
	word_pairs = [
		("above", "the"), ("across", "the"), ("after", "the"), ("against", "the"), ("along", "the"),
		("among", "the"), ("around", "the"), ("at", "the"), ("before", "the"), ("behind", "the"),
		("below", "the"), ("beneath", "the"), ("beside", "the"), ("between", "the"), ("by", "the"),
		("down", "the"), ("during", "the"), ("except", "the"), ("for", "the"), ("from", "the"),
		("in", "the"), ("inside", "the"), ("into", "the"), ("like", "the"), ("near", "the"),
		("of", "the"), ("off", "the"), ("on", "the"), ("onto", "the"), ("out of", "the"),
		("outside", "the"), ("over", "the"), ("past", "the"), ("since", "the"), ("through", "the"),
		("throughout", "the"), ("till", "the"), ("to", "the"), ("toward", "the"), ("under", "the"),
		("underneath", "the"), ("until", "the"), ("up", "the"), ("upon", "the"), ("with", "the"),
		("within", "the"), ("without", "the"), ("and", "the"), ("but", "the"), ("or", "the"),
		("nor", "the"), ("for", "the"), ("yet", "the"), ("so", "the"), ("as", "the"), ("when", "the"),
		("where", "the"), ("why", "the"), ("how", "the"), ("while", "the"), ("if", "the"), ("because", "the"),
		("as if", "the"), ("though", "the"), ("even though", "the"), ("as though", "the"),
		("whether or not", "the"), ("in order that", "the"), ("in case", "the"), ("in the event that", "the"),
		("provided that", "the"), ("unless", "the"), ("until", "the"), ("before", "the"), ("after", "the"),
		("once", "the"), ("whenever", "the"), ("while", "the"), ("as soon as", "the"), ("as long as", "the"),
		("whenever", "the"), ("wherever", "the"), ("whoever", "the"), ("however", "the"), ("whatever", "the"),
		("whichever", "the"), ("no matter how", "the"), ("in spite of", "the"), ("regardless of", "the"),
		("whereas", "the"), ("otherwise", "the"), ("as much as", "the"),
		("rather than", "the"), ("in addition to", "the"), ("likewise", "the"), ("similarly", "the"),
		("furthermore", "the"), ("moreover", "the"), ("instead", "the")
	]
	adjectives = [
		"beautiful", "handsome", "ugly", "happy", "sad", "angry", "fierce", "scary", "powerful", "strong",
		"weak", "big", "small", "tiny", "gigantic", "fat", "thin", "old", "new", "young", "bright", "dark",
		"light", "heavy", "smooth", "rough", "soft", "hard", "shiny", "dull", "quiet", "noisy", "loud",
		"fascinating", "mysterious", "curious", "enigmatic", "perplexing", "enigmatic",
		"bizarre", "strange", "peculiar", "uncommon", "unexpected", "unprecedented", "unanticipated", 
		"extraordinary", "unbelievable", "remarkable", "astounding", "amazing", "incredible", "unbelievable",
		"miraculous", "phenomenal", "prodigious", "stupendous", "miraculous", "sublime", "splendid",
		"delightful", "enjoyable", "pleasurable", "wonderful", "splendid", "fabulous", "breathtaking",
		"awe-inspiring", "mind-blowing", "incredible", "fabulous", "splendid", "delightful", "dazzling", 
		"stunning", "gorgeous", "breathtaking", "magnificent", "resplendent", "splendid", "beautiful", 
		"majestic", "splendid", "grand", "grandiose", "opulent", "luxurious", "deluxe", "sumptuous", 
		"ornate", "elegant", "refined", "graceful", "delicate", "exquisite", "intricate", "detailed", 
		"intricate", "captivating", "mesmerizing", "enchanting", "bewitching", "enthralling", "hypnotic",
		"spellbinding", "mesmerizing", "alluring", "seductive", "charming", "graceful", "ravishing", 
		"appealing", "pleasant", "inviting", "cozy", "comfortable", "warm", "inviting", "hospitable",
		"genial", "friendly", "amicable", "sociable", "companionable", "convivial", "jovial", "merry",
		"happy", "joyful", "lively", "vibrant", "animated", "marvellous", "radiant", "glorious", "regal",
		"complex", "delightful", "welcoming", "cheerful",
	]
	office_words = [
		"office", "workplace", "workspace", "corporate",
		"business", "enterprise", "company", "organization",
		"firm", "incorporation", "institution", "agency",
		"department", "division", "unit", "team", "staff",
		"employee", "colleague", "associate", "partner", "manager",
		"supervisor", "executive", "director", "officer", "leader",
		"coordinator", "facilitator", "consultant", "analyst",
		"specialist", "expert", "advisor", "mentor", "coach", "trainer",
		"instructor", "teacher", "professor", "lecturer", "researcher",
		"scientist", "engineer", "technician", "assistant", "associate",
		"aide", "assistant", "helper", "support", "service", "maintenance",
		"operation", "production", "manufacturing", "development", "design",
		"innovation", "creativity", "strategy", "planning", "policy",
		"regulation", "law", "compliance", "ethics", "standards",
		"quality", "performance", "measurement", "assessment", "evaluation",
		"feedback", "analysis", "synthesis", "solution", "resolution",
		"decision", "choice", "option", "variation", "alternative",
		"possibility", "probability", "risk", "uncertainty", "diversity",
		"inclusion", "equity", "fairness", "justice", "rights", "opportunity",
		"access", "mobility", "flexibility", "adaptability", "agility",
		"resilience", "sustainability", "growth", "expansion", "increase",
		"improvement", "advancement", "success", "achievement", "recognition",
		"reward", "compensation", "benefits", "perks", "incentives", "bonuses",
		"allowances", "pensions", "retirement", "security", "safety",
		"health", "wellness", "happiness", "satisfaction", "fulfilment",
		"purpose", "meaning", "value", "culture", "tradition", "custom",
		"habit", "routine", "rule", "protocol", "procedure", "process",
		"system", "method", "technique", "approach", "tool", "resource",
		"asset", "capital", "investment", "funding", "budget", "cost", "expense",
		"charge", "fee", "price", "value", "worth", "profit", "gain", "loss",
		"impact", "consequence", "result", "outcome", "effect", "influence", "change",
		"transformation", "evolution", "progress", "movement", "shift", "trend",
		"pattern", "structure", "hierarchy", "order", "rank", "class", "status",
		"position", "role", "function", "responsibility", "duty", "obligation",
		"commitment", "dedication", "focus", "attention", "awareness", "concentration",
		"observation", "perception", "sensation", "intuition", "insight", "understanding",
		"comprehension", "knowledge"
	]
	punctuation = [".", "?", "!", ",", ":", ";"]
	capitalize_first_word = random.random() < 0.5

	if the_words == None:
		the_words = office_words
	for i in range(num_words):
		if i > 0:
			text += " "
		if random.random() < 0.5:
			pair = random.choice(word_pairs)
			text += pair[0] + " " + pair[1]
		elif random.random() < 0.25:
			adjective = random.choice(adjectives)
			noun = random.choice(words)
			text += adjective + " " + noun
		else:
			word = random.choice(words)
			if capitalize_first_word and i == 0:
				word = word.capitalize()
			text += word
		last_word = text.split()[-1]
		if last_word == "the" and the_words:
			text += " " + random.choice(the_words)
	if include_punctuation:
		text += random.choice(punctuation)
	if include_digits:
		text += str(random.randint(0, 9))
	return text