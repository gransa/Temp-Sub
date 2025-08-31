# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://sni.medicaltreatment.ir/rewrite?url=https%3A%2F%2Fgetafreenode.com%2Fsubscribe%2F%3Fuuid%3D942b9cb8-92fa-46ac-ae91-f69c8234434b%0Ahttps%3A%2F%2Fgetafreenode.com%2Fsubscribe%2F%3Fuuid%3D0cb527d9-6117-4bcf-a52b-1704b3458cef%0Ahttps%3A%2F%2Fgetafreenode.com%2Fsubscribe%2F%3Fuuid%3D5eaa121d-4362-444d-8219-29b02c35303a&nocache=1",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 1000

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 365
