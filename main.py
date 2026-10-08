from pyscript import document

EAST_ASIA_NICKNAMES = {
    "japan": "Land of the Rising Sun",
    "china": "The Red Dragon",
    "south korea": "Land of the Morning Calm",
    "north korea": "The Hermit Kingdom",
    "mongolia": "Land of the Eternal Blue Sky",
    "taiwan": "The Formosa Island",
}

def lookup_nickname(country_input):
    """
    Retrieves the nickname from dictionary without using if/else.
    """
    return EAST_ASIA_NICKNAMES.get(country_input, "Country not in atlas.")


def show_nickname(event):
    """
    Handles button click, gets input, and displays result.
    """
    user_input = document.querySelector("#country").value.strip().lower()

    output = lookup_nickname(user_input)

    document.querySelector("#result").innerText = output