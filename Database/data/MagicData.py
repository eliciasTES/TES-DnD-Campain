# Inserting multiple rows efficiently
magic_data = [
    (
        "Fireball",                          # name
        "A compressed sphere of fire that explodes on impact.",  # description

        "Destruction",                       # school
        "spell",                             # magic_type
        "fire",                              # element
        "projectile",                        # subtype

        35,                                  # mana_cost
        0,                                   # stamina_cost
        4,                                   # cooldown
        1.5,                                 # cast_time
        0,                                   # duration
        60,                                  # range
        10,                                  # area_of_effect

        80,                                  # damage
        0,                                   # healing

        1,                                   # level_required
        "intelligence",                      # scaling_stat
        1.2,                                 # power_scale

        "damage",                            # effect_type
        "burn",                              # status_effect
        0.3,                                 # effect_strength

        1,                                   # requires_target
        1,                                   # is_aoe

        "common",                            # rarity
        "Imperial College of Magic",         # origin
        "A basic destructive spell taught to novice mages."
    )
]