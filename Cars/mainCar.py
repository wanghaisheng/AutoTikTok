import openai
import random 
import requests
import json
import io
import base64
from PIL import Image, PngImagePlugin

openai.api_key = "OpenAI-API"

def generate_car_prompt(car_name):
    prompt = f"""Generate a 900-second deform prompt for a cool car edit featuring a {car_name}. Make the format look like this but have the prompt in each text different.{{
        "0": "{car_name} in a parking lot, gleaming in daylight, 'Ordinary Day' text overlay",
        "50": "Interior of {car_name}, music blaring, GPS set, 'Ready to Roll' text",
        "100": "Passenger in {car_name} messing with a GoPro, 'Capturing Moments' text",
        "150": "GoPro leaning out the window of {car_name}, capturing the car's speed, 'Living on the Edge' text",
        "200": "Rearview mirror view in {car_name} of multiple sports cars following, 'Drawing Attention' text",
        "250": "Close-up of {car_name} driver's worried face, 'Something's Off' text",
        "300": "Driver in {car_name} pulling over, sports cars surrounding, 'Showdown' text",
        "350": "Driver in {car_name} struggling with seatbelt, tension rising, 'Critical Moments' text",
        "400": "Bystander noticing {car_name}, 'Unexpected Savior' text",
        "450": "Bystander in {car_name} talking to sports car drivers, 'Clearing the Air' text",
        "500": "Drivers in {car_name} looking at GoPro footage, 'The Revelation' text",
        "550": "Sports car drivers around {car_name} laughing, giving thumbs up, 'Misunderstanding Cleared' text",
        "600": "{car_name} driver sitting back in car, sigh of relief, 'Close Call' text",
        "650": "Driver in {car_name} checking glove box, realizing sunglasses are missing, 'The Real Loss' text",
        "700": "{car_name} parked in a garage, driver contemplating, 'Reflecting' text",
        "750": "GoPro in {car_name} placed on a shelf, 'Lesson Learned' text",
        "800": "Driver polishing {car_name}, 'New Beginnings' text",
        "850": "{car_name} text about responsible driving and filming, 'Drive Safe, Capture Wisely' text",
        "900": "Montage of {car_name}'s journey, 'An Ordinary Drive Made Extraordinary' text overlay, epic music crescendo"
    }}"""

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# List of different cars
cars = [
    "Porsche gt3",
    "Ferrari 488",
    "Lamborghini Huracan",
    "Tesla Model S",
    "McLaren P1",
    "Bugatti Chiron",
    "Aston Martin Vantage",
    "Chevrolet Corvette Z06",
    "Dodge Viper",
    "Nissan GT-R",
    "BMW M4",
    "Ford Mustang Shelby GT500",
    "Audi R8",
    "Jaguar F-Type",
    "Mercedes-AMG GT",
    "Alfa Romeo 4C",
    "Koenigsegg Jesko",
    "Pagani Huayra",
    "Lotus Evora",
    "Porsche 918 Spyder",
    "Lamborghini Aventador",
    "Ferrari LaFerrari",
    "McLaren 720S",
    "Bugatti Veyron",
    "Aston Martin DBS",
    "Chevrolet Camaro ZL1",
    "Maserati GranTurismo",
    "BMW M8",
    "Dodge Challenger Hellcat",
    "Ford GT",
    "Audi RS 6 Avant",
    "Cadillac CTS-V",
    "Lexus LC 500",
    "Mercedes-Benz SLR McLaren",
    "Alpine A110",
    "Koenigsegg Regera",
    "Pagani Zonda",
    "Lotus Exige",
    "Porsche Carrera GT",
    "Lamborghini Gallardo",
    "Ferrari F40",
    "McLaren F1",
    "TVR Sagaris",
    "Aston Martin One-77",
    "Chevrolet Corvette Stingray",
    "Maserati MC12",
    "BMW M5",
    "Dodge Charger SRT Hellcat",
    "Audi RS 7",
    "Jaguar XKR",
    "Mercedes-Benz SLS AMG",
    "Noble M600",
    "Koenigsegg Agera",
    "Pagani Huayra Roadster",
    "Lotus Elise",
    "Porsche Taycan",
    "Lamborghini Murcielago",
    "Ferrari F50",
    "McLaren 600LT",
    "Rimac C_Two",
    "Aston Martin DB11",
    "Chevrolet Corvette C8",
    "Maserati Alfieri",
    "BMW i8",
    "Dodge Challenger SRT Demon",
    "Audi TT RS",
    "Jaguar XJ220",
    "Mercedes-Benz CLK GTR",
    "W Motors Lykan Hypersport",
    "Koenigsegg Gemera",
    "Pagani Huayra BC",
    "Lotus Esprit",
    "Porsche Boxster",
    "Lamborghini Diablo",
    "Ferrari Enzo",
    "McLaren 570S",
    "Rimac Nevera",
    "Aston Martin Valkyrie",
    "Chevrolet Camaro SS",
    "Maserati Quattroporte",
    "BMW Z4",
    "Dodge Viper ACR",
    "Audi S5",
    "Jaguar XK",
    "Mercedes-AMG Project One",
    "W Motors Fenyr SuperSport",
    "Koenigsegg One:1",
    "SSC Tuatara",
    "Lotus 3-Eleven",
    "Porsche Panamera",
    "Lamborghini Veneno",
    "Ferrari 812 Superfast",
    "McLaren GT",
    "Rimac Concept One",
    "Aston Martin Rapide",
    "Chevrolet Camaro IROC-Z",
    "Maserati Levante Trofeo",
    "BMW M2",
    "Dodge Dart Swinger",
    "Audi RS Q8",
]

random_car = random.choice(cars)

#Making Diffusion Prompt for car
print(f"Generating prompt for {random_car}...")
#generated_prompt = generate_car_prompt(random_car)
#print(generated_prompt)

negative_Prompt = "nsfw, nude, humans, people, person, duplicate, weird, glitchy, deformed"
generated_prompt = {
"0": "Drone flying smoothly over a picturesque landscape",
"50": "Drone descending gently towards a serene river",
"100": "Drone skimming the water's surface, capturing reflections",
"150": "Drone ascending over lush forests",
"200": "Drone navigating through a narrow canyon",
"250": "Drone hovering near a cascading waterfall",
"300": "Drone capturing a flock of birds in flight",
"350": "Drone gliding over a tranquil lake",
"400": "Drone ascending towards a majestic mountain peak",
"450": "Drone circling around a historic landmark",
"500": "Drone diving into a bustling cityscape",
"550": "Drone capturing a breathtaking sunset over the city skyline",
"600": "Drone soaring high above the city",
"650": "Drone hovering near a rooftop party",
"700": "Drone flying over a vibrant fireworks display",
"750": "Drone returning gracefully to the launch point",
"800": "Drone landing smoothly on the ground"
}

#---------------------------------------------------------------------------------------------------------------------------------------
import webuiapi

# create API client
api = webuiapi.WebUIApi()

# create API client with custom host, port
api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)

# create API client with custom host, port and https
api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)

# create API client with default sampler, steps.
api = webuiapi.WebUIApi(sampler='Euler a', steps=20)

# optionally set username, password when --api-auth=username:password is set on webui.
# username, password are not protected and can be derived easily if the communication channel is not encrypted.
# you can also pass username, password to the WebUIApi constructor.
api.set_auth('username', 'password')

result1 = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
                    seed=1003,
                    styles=["anime"],
                    cfg_scale=7,
                      sampler_index='DDIM',
                      steps=30,
                      enable_hr=True,
                      hr_scale=2,
                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
                      hr_second_pass_steps=20,
                      hr_resize_x=1536,
                      hr_resize_y=1024,
                      denoising_strength=0.4,
                    )

# images contains the returned images (PIL images)
result1.images
# image is shorthand for images[0]
result1.image
# info contains text info about the api call
result1.info
# info contains paramteres of the api call
result1.parameters
result1.image