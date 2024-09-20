#1
space_telescope_missions_dict = {
"Hubble Space Telescope" : "Observing distant galaxies and astronomical phenomena.",
"Chandra X-ray Observatory" : "Studying X-ray emissions from high-energy regions.",
"James Webb Space Telescope (JWST)" : "Observing the universe in infrared light.",
"Spitzer Space Telescope" : "Studying the universe in infrared wavelengths.",
"Kepler Space Telescope" : "Searching for exoplanets by detecting transits."
} 
#2
print(space_telescope_missions_dict)

#3
print("The mission of the 3rd Telescope is: ",space_telescope_missions_dict["James Webb Space Telescope (JWST)" ])
      
#4
space_telescope_missions_dict["Hubble Space Telescope"] = "Shine"

#5
del space_telescope_missions_dict["Spitzer Space Telescope"]

#6
last_key = list(space_telescope_missions_dict.keys())[-1]
last_value = space_telescope_missions_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)