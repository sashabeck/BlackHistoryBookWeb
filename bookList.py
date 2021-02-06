import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


books = [
    {'id': 0,
     'genre': 'Action and Adventure',
     'length': 100,
     'title': 'The Hate You Give',
     'author': 'Angie Thomas',
     'year_published': '2017',
     'summary': 'Sixteen-year-old Starr Carter moves between two worlds: the poor neighborhood where she lives and the fancy suburban prep school she attends. The uneasy balance between these worlds is shattered when Starr witnesses the fatal shooting of her childhood best friend Khalil at the hands of a police officer. Khalil was unarmed.'},

    {'id': 1,
     'genre': 'Classic',
     'length': 300,
     'title': 'Concrete Rose',
     'author': 'Angie Thomas',
     'published': '2021',
     'summary': 'If there’s one thing seventeen-year-old Maverick Carter knows, it’s that a real man takes care of his family. As the son of a former gang legend, Mav does that the only way he knows how: dealing for the King Lords. With this money he can help his mom, who works two jobs while his dad’s in prison. Life’s not perfect, but with a fly girlfriend and a cousin who always has his back, Mav’s got everything under control. Until, that is, Maverick finds out he’s a father. Suddenly he has a baby, Seven, who depends on him for everything. But it’s not so easy to sling dope, finish school, and raise a child. So when he’s offered the chance to go straight, he takes it. In a world where he’s expected to amount to nothing, maybe Mav can prove he’s different. When King Lord blood runs through your veins, though, you can\'t just walk away. Loyalty, revenge, and responsibility threaten to tear Mav apart, especially after the brutal murder of a loved one. He’ll have to figure out for himself what it really means to be a man.'},

    {'id': 2,
     'genre': 'Classic',
     'length': 600,
     'title': 'Becoming',
     'author': 'Michelle Obama',
     'published': '2018',
     'summary': 'n a life filled with meaning and accomplishment, Michelle Obama has emerged as one of the most iconic and compelling women of our era. As First Lady of the United States of America—the first African American to serve in that role—she helped create the most welcoming and inclusive White House in history, while also establishing herself as a powerful advocate for women and girls in the U.S. and around the world, dramatically changing the ways that families pursue healthier and more active lives, and standing with her husband as he led America through some of its most harrowing moments. Along the way, she showed us a few dance moves, crushed Carpool Karaoke, and raised two down-to-earth daughters under an unforgiving media glare. In her memoir, a work of deep reflection and mesmerizing storytelling, Michelle Obama invites readers into her world, chronicling the experiences that have shaped her—from her childhood on the South Side of Chicago to her years as an executive balancing the demands of motherhood and work, to her time spent at the world’s most famous address. With unerring honesty and lively wit, she describes her triumphs and her disappointments, both public and private, telling her full story as she has lived it—in her own words and on her own terms. Warm, wise, and revelatory, Becoming is the deeply personal reckoning of a woman of soul and substance who has steadily defied expectations—and whose story inspires us to do the same.' }

]
            