from nautobot.extras.plugins import PluginConfig


class NetBoxRpMappingsConfig(PluginConfig):
    name = "nautobot_rp_mapping"
    verbose_name = "Nautobot RP Mapping"
    description = "Manage static RP Maps in Nautobot"
    version = "0.1"
    base_url = "rp-mapping"
    author = "Thomas Bridge"
    author_email = "thomas.bridge@icloud.com"


config = NetBoxRpMappingsConfig
