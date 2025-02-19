from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

information = """ Timothée Hal Chalamet (pronunciación en inglés: /ˈtɪməθi ˈʃæləmeɪ/;3​4​ pronunciación en francés: /timɔte ʃalamɛ/; Hell's Kitchen, Manhattan, Nueva York, 27 de diciembre de 1995) es un actor francoestadounidense.5​ Ha sido nominado para dos Premios Óscar, tres BAFTAs, cuatro Globos de Oro, cinco SAG y seis Premios de la Crítica Cinematográfica.

Chalamet comenzó su carrera cuando era adolescente en televisión, apareciendo en la serie dramática Homeland en 2012. Dos años más tarde, hizo su debut cinematográfico en la comedia dramática Men, Women & Children y apareció en la película de ciencia ficción Interstellar. Chalamet saltó a la fama internacional con el papel principal de un adolescente enamorado en la película de Luca Guadagnino Call Me by Your Name (2017), lo que le valió una nominación al Premio de la Academia al Mejor Actor.

Además de papeles secundarios en las películas de Greta Gerwig Lady Bird (2017) y Mujercitas (2019), Chalamet asumió papeles protagónicos como el drogadicto Nic Sheff en la película biográfica Beautiful Boy (2018) y un joven caníbal en la película de terror romántico de Guadagnino Bones and All (2022), que también produjo. Luego, Chalamet comenzó a protagonizar películas de gran presupuesto, interpretando a Paul Atreides en la película de ciencia ficción de Denis Villeneuve Dune (2021) y su secuela Dune: Part Two (2024), y a Willy Wonka en la película de fantasía musical de Paul King Wonka (2023).

En el escenario, Chalamet protagonizó la obra autobiográfica de John Patrick Shanley Prodigal Son en 2016, por la que ganó un premio Lucille Lortel y obtuvo una nominación a un premio Drama League. Fuera de la pantalla, ha sido etiquetado como un símbolo sexual y un ícono de la moda."""

if __name__ == "__main__":
    load_dotenv()

    summary_template= f"""
    Given the information {information} about a person from I want create: 
    1. A short summary\n
    2. Two interesting facts about them 

"""

    summary_prompt_template = PromptTemplate(
        input_variables =["information"], template=summary_template )

    llm = ChatOpenAI(temperature=0, model_name= "gpt-3.5-turbo")

    chain= summary_prompt_template | llm

    res= chain.invoke(input={"information":information})
    print(res)