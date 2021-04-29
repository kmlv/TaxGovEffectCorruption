from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Marco Gutierrez'

doc = """
Small survey on prosociality based on Global preferences survey
"""


class Constants(BaseConstants):
    name_in_url = 'prosociality'
    players_per_group = None
    num_rounds = 1
    likert_choices=[choice for choice in range(11)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    punish_your_punisher = models.IntegerField(choices=Constants.likert_choices, 
                            widget=widgets.RadioSelectHorizontal, verbose_name="""
                            ¿Qué tan dispuesto
                            está usted a castigar a
                            alguien que lo(a) trata a
                            usted injustamente,
                            incluso cuando existan
                            riesgos para usted de
                            sufrir consecuencias
                            personales?""") # [WP13419]

    punish_others_punisher = models.IntegerField(choices=Constants.likert_choices,
                            widget=widgets.RadioSelectHorizontal, verbose_name="""
                            ¿Qué tan dispuesto(a)
                            está usted a castigar a
                            alguien que trata a los
                            demás injustamente,
                            incluso cuando existan
                            riesgos para usted de
                            sufrir consecuencias
                            personales?""") # [WP13420]

    donate_without_reward = models.IntegerField(choices=Constants.likert_choices,
                            widget=widgets.RadioSelectHorizontal, verbose_name="""
                            ¿Qué tan dispuesto(a)
                            está usted a hacer
                            donaciones a causas
                            benéficas sin esperar
                            nada a cambio?""") # [WP13421]

    reciprocity = models.IntegerField(choices=Constants.likert_choices,
                            widget=widgets.RadioSelectHorizontal, verbose_name="""
                            Cuando alguien me hace un
                            favor, estoy dispuesto a
                            devolverlo.""") # [WP13422]

    revenge = models.IntegerField(choices=Constants.likert_choices,
                            widget=widgets.RadioSelectHorizontal, verbose_name="""
                            Si me tratan muy
                            injustamente, tomaré
                            revancha en la primera
                            ocasión, incluso aunque deba
                            pagar un costo por ello.""") # [WP13423]

    stranger_payback = models.IntegerField(choices=[(1, "No, no le entregaría ningún obsequio"),
                            (2, "El obsequio que cuesta 2 Soles"),
                            (3, "El obsequio que cuesta 4 Soles"),
                            (4, "El obsequio que cuesta 6 Soles"),
                            (5, "El obsequio que cuesta 8 Soles"),
                            (6, "El obsequio que cuesta 10 Soles"),
                            (7, "El obsequio que cuesta 12 Soles"),
                            (8, "(NS/NR)")], verbose_name="""
                            Por favor piense en que haría usted en la siguiente situación. Está en un área que no conoce mucho y se da cuenta que se ha
                            perdido. Le pide orientación a un extraño. El extraño le ofrece llevarlo a su destino.
                            
                            Ayudarlo a usted le cuesta al extraño unos 8 Soles en total. Sin embargo, el extraño dice que no desea que usted le de dinero. Usted
                            tiene seis obsequios. El obsequio más económico cuesta 2 Soles y el más costoso cuesta 12 Soles. ¿Le daría al extraño uno de los
                            obsequios como agradecimiento?
                            
                            ¿Qué obsequio le entregaría?""") # [WP13458]
                            