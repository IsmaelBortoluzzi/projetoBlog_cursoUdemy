from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):  # se n herda, da esse erro: TypeError at /posts/7 object() takes no parameters

    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        palavroes =   ['Anus',
                       'Baba-ovo',
                       'Babaovo',
                       'Babaca',
                       'Bacura',
                       'Bagos',
                       'Baitola',
                       'Bebum',
                       'Besta',
                       'Bicha',
                       'Bisca',
                       'Bixa',
                       'Boazuda',
                       'Boceta',
                       'Boco',
                       'Boiola',
                       'Bolagato',
                       'Boquete',
                       'Bolcat',
                       'Bosseta',
                       'Bosta',
                       'Bostana',
                       'Brecha',
                       'Brexa',
                       'Brioco',
                       'Bronha',
                       'Buca',
                       'Buceta',
                       'Bunda',
                       'Bunduda',
                       'Burra',
                       'Burro',
                       'Busseta',
                       'Cachorra',
                       'Cachorro',
                       'Cadela',
                       'Caga',
                       'Cagado',
                       'Cagao',
                       'Cagona',
                       'Canalha',
                       'Caralho',
                       'Casseta',
                       'Cassete',
                       'Checheca',
                       'Chereca',
                       'Chibumba',
                       'Chibumbo',
                       'Chifruda',
                       'Chifrudo',
                       'Chota',
                       'Chochota',
                       'Chupada',
                       'Chupado',
                       'Clitoris',
                       'Cocaina',
                       'Coco',
                       'Corna',
                       'Corno',
                       'Cornuda',
                       'Cornudo',
                       'Cu',
                       'Curalho',
                       'Cuzao',
                       'Cuzuda',
                       'Cuzudo',
                       'Debil',
                       'Demonio',
                       'Difunto',
                       'Doida',
                       'Doido',
                       'Egua',
                       'Escrota',
                       'Escroto',
                       'Esporro',
                       'Fedida',
                       'Fedido',
                       'Fedor',
                       'Feia',
                       'Feio',
                       'Feiosa',
                       'Feioso',
                       'Feioza',
                       'Feiozo',
                       'Felacao',
                       'Fenda',
                       'Foda',
                       'Fodao',
                       'Fode',
                       'FodidaFodido',
                       'Fudendo',
                       'Fudecao',
                       'Fudida',
                       'Fudido',
                       'Furada',
                       'Furado',
                       'Furão',
                       'Furnicar',
                       'Furo',
                       'Furona',
                       'Gaiata',
                       'Gaiato',
                       'Gay',
                       'Grelinho',
                       'Grelo',
                       'Idiota',
                       'Idiotice',
                       'Imbecil',
                       'Iscrota',
                       'Iscroto',
                       'Japa',
                       'Ladra',
                       'Ladrona',
                       'Lalau',
                       'Leprosa',
                       'Leproso',
                       'Lésbica',
                       'Macaca',
                       'Macaco',
                       'Machona',
                       'Machorra',
                       'Manguaca',
                       'Manguaca',
                       'Meleca',
                       'Merda',
                       'Mija',
                       'Mijada',
                       'Mijado',
                       'Mijo',
                       'Mocrea',
                       'Mocreia',
                       'Moleca',
                       'Moleque',
                       'Mondronga',
                       'Mondrongo',
                       'Naba',
                       'Nadega',
                       'Nojeira',
                       'Nojenta',
                       'Nojento',
                       'Nojo',
                       'Olhota',
                       'Otaria',
                       'Ot-ria',
                       'Otario',
                       'Otário',
                       'Paca',
                       'Pau',
                       'Peia',
                       'Peido',
                       'Pemba',
                       'Pênis',
                       'Pentelha',
                       'Pentelho',
                       'Perereca',
                       'Peru',
                       'Pica',
                       'Picao',
                       'Pilantra',
                       'Piranha',
                       'Piroca',
                       'Piroco',
                       'Piru',
                       'Porra',
                       'Prega',
                       'Prostibulo',
                       'Prost-bulo',
                       'Prostituta',
                       'Prostituto',
                       'Punheta',
                       'Punhetao',
                       'Pus',
                       'Pustula',
                       'Puta',
                       'Puto',
                       'Puxa-saco',
                       'Puxasaco',
                       'Rabao',
                       'Rabo',
                       'Rabuda',
                       'Rabudao',
                       'Rabudo',
                       'Rabudona',
                       'Rachado',
                       'Ramela',
                       'Remela',
                       'Retardada',
                       'Retardado',
                       'Ridícula',
                       'Rola',
                       'Rolinha',
                       'Rosca',
                       'Sacana',
                       'Safada',
                       'Safado',
                       'Sapatao',
                       'Sifilis',
                       'Siririca',
                       'Tarada',
                       'Tarado',
                       'Testuda',
                       'Tezao',
                       'Tezuda',
                       'Tezudo',
                       'Trocha',
                       'Trolha',
                       'Troucha',
                       'Trouxa',
                       'Troxa',
                       'Vaca',
                       'Vagabunda',
                       'Vagabundo',
                       'Vagina',
                       'Veada',
                       'Veadao',
                       'Veado',
                       'Viada',
                       'Víado',
                       'Viadao',
                       'Xavasca',
                       'Xerereca',
                       'Xexeca',
                       'Xibiu',
                       'Xibumba',
                       'Xota',
                       'Xochota',
                       'Xoxota',
                       'Xana',
                       'Xaninha',
        ]
        print(comentario)

        for palavrao in palavroes:
            print(palavrao)
            if palavrao.lower() in comentario.lower():
                self.add_error(
                    'comentario',
                    'Não seja boca suja. Nosso blog não aceita palavrões'
                )


    class Meta:
        model = Comentario  # se n poe isso, da esse erro: TypeError at /posts/7 object() takes no parameters

        fields = ('nome_comentario', 'email_comentario', 'comentario')
