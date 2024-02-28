import random

insults = ["Get Good Shayan",
           "Can you shut up",
           "Professional Yapper",
           "stfu shayan",
           "un-fucking-bearable",
           "I'll Kill you myself Shayan",
           "No wonder bitch boy",
           "Anatomy 2 Shayan 0",
           "shayan haider , i know where you live",
           "nah u just a bitch shayan",
           "nobody wants to hear you speak, doofus",
           "cringe",
           "chat, can we ban shayan",
           "I wish to obliterate you, you pathetic waste of space",
           "ur family hates you im sure",
           "not funny lol",
           "are you restarted",
           "did your mom not breastfeed you enough",
           "Bahria's Harlot",
           "shayan looks like a pug that has to be put down cuz its ugly as fuck",
           "shayan looks like the fat guy they would put in a lifebouy ad"]


def handle_response() -> str:
    index = random.randint(0, len(insults)-1)
    return insults[index]