base_image = "./layers/Whelps/"

traits = ["Backgrounds", "Whelps"]


image_size = (600, 700)

item_name = "Whelps of the west"

description = "only pfp"

"""
We have 3 DNA generation types:
- 1: sequential; deterministic, all the possible DNA configurations will be generated
- 2: random; random DNA generation
- 3: random DNA generation based on rarity configuration
"""
dna_generation_type = 2

# The image url in metadata json files
image_url = "https://ifps.QmcfV1UjAJ4SgM7eqE99ZtcWKrojPPS7YdDdLophVT9hFy"

##########################################################################
### WARNING!!! DO NOT EDIT BELOW THIS LINE, IT MIGHT BREAK THE ENGINE. ###
##########################################################################
engine_type = "complex"
