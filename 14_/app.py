from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

ps = [
    "Pommy ipsum black pudding the dog's dinner ear hole roast beef eton mess upper class ever so, lad blimey superb naff off oo ecky thump goggledegook doolally. Apple and pears sausage roll pennyboy tallywhacker some mothers do 'ave 'em rubbish stop arsing around a right corker macca, is she 'avin a laugh pillock rivetting stuff bangers and mash barmy fish and chips. Ridiculous odds and sods ey up chuck absolute twoddle the black death ee bah gum one feels that fancy a cuppa, chinwag plum pudding ear hole bloody mary spiffing The Hounds of Baskerville copped a bollocking farewell, I'd reet fancy a Time Lord doolally off the hook treacle ponce. ",
    "See a man about a dog tallywhacker it's me peepers marvelous nutter gallivanting around, Doctor Who working class chin up pie-eyed. Good old fashioned knees up indeed get away with ya it's just not cricket sweets twiglets bits 'n bobs bugger one off, cheesed off bogroll is she 'avin a laugh bog roll bugger black cab brown sauce getting on my wick, a reet bobbydazzler biscuits every fortnight ever so a right corker bits 'n bobs on the beat. A reet bobbydazzler Dalek a week on Sunday fancied a flutter, at the boozer blimey. Old chap ee bah gum ey up, Kate and Will. Know your onions sweets it's spitting superb fried toast, wellies drizzle blimey. ",
    "Copped a bollocking scarper bangers and mash in a pickle fish fingers and custard chin up ended up brown bread a bottle of plonk, Sonic Screwdriver Bob's your uncle naff off how's your father a total jessie ey up. Bread and butter pudding and thus Union Jack narky doing my head in Bad Wolf Dr. Watson, ey up chuck have a butcher's at this penny-dreadful pork dripping naff off scally wibbly-wobbly timey-wimey stuff, make a brew is she 'avin a laugh black cab what a doddle absobloodylootely. Bloody mary jolly good black cab scrubber warts and all wind up ridiculous, bogroll scarper plum pudding manky crisps. "
]

@app.route("/", methods=["GET","POST"])
def foo():
    return render_template( 'index.html',p1=ps[0])


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()