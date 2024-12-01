from matplotlib import pyplot as plt

def simulate_population_growth(city_population, birth_rate, years):

    Index = ['Miami', 'Tampa', 'Orlando', 'Sarasota', 'Jacksonville', 'Fort Myers', 'Tallahassee', 'Florida City', 'Clearwater', 'Bradenton']

    input('Please choose a city')

    #Variables:
    #city_population: The current population of selected city.
    #birth_rate: annual birth rate (as a decimal)
    #years: Number of years simulated

    #Returns:
    #A list containing the city population for each city and year

    population = [city_population]

    for year in range(1, years + 1):
        births = population[-1] * birth_rate
        population.append(population[-1] + births)

    return population

if __name__ =='_main_':
    #program parameters
    Miami_city = 440,000
    Tampa_city = 380,000
    Orlando_city = 310,000
    Sarasota_city = 55,000
    Jacksonville_city = 950,000
    Fort_Myers_city = 86,000
    Tallahassee_city = 200,000
    Florida_city_city = 13,000
    Clearwater_city = 120,000
    Bradenton_city = 56,000

    city_population = []
    birth_rate = 0.02
    years = 20

    population_sizes = simulate_population_growth(city_population, birth_rate, years)

    #The results
    plt.plot(range(years + 1), population_sizes)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population growth by city Simulator')
    plt.show()