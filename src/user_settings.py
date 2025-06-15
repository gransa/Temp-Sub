# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://awa.inekokkk.immobilien/amei/6ca22ad3b96aa6601fbe4457dad107a2",
    "https://sub.xn--3bs984e5qg.xyz/s/d2ddf60933dd08ad67d3585f72ed16c3",
    "https://sub.xn--vpn-3f0h822m.com/s/56c52d37015ce5c33fd0b6112b639f08",
    "https://sub.xn--3bs984e5qg.xyz/s/dcd03ae545a147ebb07420bcdd321ef5",
    "https://jc.huasuan666.top/api/v1/client/subscribe?token=8bc38a0c131e9b3fcd3a9083824c23e9",
    "https://sub.xn--vpn-3f0h822m.com/s/ff7bb35d4ee18502c7e3b9f5bca2dfa2",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 100

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": True,
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
