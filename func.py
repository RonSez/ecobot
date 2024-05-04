from random import choice


intro_text = """
    Air pollution is the presence of harmful or excessive quantities of substances in the air, which can have negative effects on human health, the environment, and the climate. 
    Common air pollutants include particulate matter (PM), nitrogen dioxide (NO2), sulfur dioxide (SO2), carbon monoxide (CO), ozone (O3), and volatile organic compounds (VOCs). 
    Sources of air pollution include vehicle emissions, industrial processes, agricultural activities, and burning of fossil fuels.
    Exposure to air pollution can lead to respiratory and cardiovascular diseases, allergies, asthma, and other health problems. 
    It can also contribute to climate change, ecosystem damage, and reduced air quality, impacting both human and environmental well-being.
    """

def air_pollution_intro():
    return intro_text


air_pollution_facts = [
    "Air pollution is responsible for over 7 million premature deaths worldwide each year.",
    "Indoor air pollution can be as harmful as outdoor air pollution, especially in poorly ventilated spaces.",
    "Children, the elderly, and individuals with pre-existing health conditions are particularly vulnerable to the effects of air pollution.",
    "Vehicle emissions are a major source of air pollution, releasing pollutants such as nitrogen oxides and particulate matter.",
    "Reducing air pollution can lead to significant health and economic benefits, including lower healthcare costs and increased productivity.",
    "Air pollution is a leading environmental risk factor for diseases such as stroke, heart disease, lung cancer, and respiratory infections.",
    "Smog, a type of air pollution, is formed when pollutants react with sunlight, creating a haze of harmful gases and particulates.",
]

# Function to get a random air pollution fact
def get_random_air_pollution_fact():
    return choice(air_pollution_facts)


solutions = [
    "Promoting the use of electric vehicles to reduce emissions from transportation.",
    "Implementing stricter regulations on industrial emissions and pollution control measures.",
    "Encouraging the adoption of renewable energy sources such as solar and wind power.",
    "Planting trees and creating green spaces to absorb pollutants and improve air quality.",
    "Promoting energy efficiency and reducing energy consumption to decrease pollution from power plants.",
    "Educating the public about the health effects of air pollution and the importance of sustainable practices.",
    "Supporting research and innovation to develop cleaner technologies and alternative fuels.",
]

# Function to get a random solution
def get_random_solution():
    return choice(solutions)