config = {

    # example of a reference dict
    # if actor dict has a key with a str value (vs dict), will look for a key in the config file with the same value
    # (e.g. if key in actor dict is set to "bg", will look for "bg" key in `config` var)
    # will check if a key with that name exists in the main `config` dict
    # if it exists, will check if the actor dict key's value string matches a key in the corresponding dict
    "bg": {
        "default": {
            "type": "img",
            "value": r"C:\project\UI_standard.png"
        },
        "spirit": {
            "type": "img",
            "value": r"C:\project\UI_static.png"
        },
    },

    # text styles for "txt" layers must be defined here
    # must have all these values unless said to be optional
    "font": {
        "title": {
            "font": r"C:\project\FOT-Matisse Pro M.otf",
            "fill": "#F09600",          # text color, hex code (with #)
            "pointsize": 33,            # font size
            "kerning": 2,               # OPTIONAL
            # "alignment": "left",      # OPTIONAL; defaults to "left" if omitted, otherwise must be "left", "center", or "right"
            "position_x": 366,          # number of pixels of top left of text from left side of screen
            "position_y": 896,          # number of pixels from top of screen
        },
        # "example_additional_font_style": {
        #   "font": r"path_to_font",
        #   "fill": "#FFFFFF"
        #   "pointsize": 8,
        #   "position_x": 0
        #   "position_y": 0
        # }
    },

    "actor": {
        # where images/text to overlay are specified based on the actor set in Aegisub's Actor field
        # order doesn't matter, specified in `stack` var further down
        # general format is as follows:

        # "name_in_actor_field": {
        #   "my_image_layer": {
        #       "type": "img",
        #       "value": r"absolute\path\to\image.png"  # drawn at top left, so should be same resolution as video
        #   },
        #   "my_text_layer": {
        #       "type": "txt",
        #       "font": "my_font_style",    # name of key in "font" dict
        #       "value": "my text to draw"
        #   },
        #   "my_animated_layer": {     # EXPERIMENTAL, drawn via a separate ffmpeg filter, so less performant (probably)
                                       # unfinished, you probably shouldn't use this
        #       "type": "ff",
        #       "value": r"absolute\path\to\video"
        #   },
        #   "my_blank_defined_layer": {     # really only used in "%Default" for a layer that won't be used by default so you don't have to specify "type" or "font" each time
        #       "type": "txt",
        #       "font": "my_font_style",
        #       "value": None
        #   },
        #   "layer_from_%Default_I_dont_want": None
        # }

        # "type" must be either "img", "txt", or "ff"
        # "type" and "value" (and "font" if "txt") must be defined in individual actor or %Default


        # REQUIRED, default actor when no actor is set in Aegisub's Actor field
        # also specifies the default values for the layer values defined in an actor
        # (for example, for "name", all actors will have the type set as "txt", with font "title" unless specified otherwise)
        # don't have to define all layers in stack in "%Default", can define them in a specific actor
        "%Default": {
            "name": {
                "type": "txt",
                "font": "title",
                "value": None
            },
            "portrait": {
                "type": "img",
                "value": None
            },
            "bg": "default",
        },

        # REQUIRED, for if actor is set in Aegisub, but isn't defined in config
        # meant for one-off characters like "Threatening Man" and such
        # all "value" keys are replaced with actor name
        "%Name": {
            "name": {"value": None}
        },

        # additional actors go here (well, order of the dict doesn't actually matter)
        "Yashiki": {
            "name": {"value": "Kazuo Yashiki"},
            "portrait": {"value": r"C:\project\portrait_yashiki.png"},
            # "name_plate": {"value": r"path\to\name\plate.png", "type": "img"}   # example of an additional layer you can give
                                                                                  # to an actor without specifying it in %Default
        },

        "Mashita": {
            "name": {"value": "Satoru Mashita"},
            "portrait": {"value": r"C:\project\portrait_mashita.png"}
        },

        "Akira": {
            "name": {"value": "Akira Kijima"},
            "bg": "spirit"
        },

    },

    # if these names are typed into Aegisub's Effect field, overrides an actor's set layers for that line
    # is additive, like how actors are to "%Default"
    # basically, layers are taken from "%Default", layer values are overridden by the defined actor, and are then overridden by the defined effect
    "effect": {
        "DefaultBG": {
            "bg": "default"
        },
        "SpiritBG": {
            "bg": "spirit",
            "portrait": None
        },
        "NoBG": {
            "bg": None
        },
        "PortraitNPC": {
            "bg": "default",
            "portrait": {"value": r"C:\project\portrait_NPC.png"}
        }
    }
}

# layer order for a given actor
# first in list is top layer, last in list is bottom layer
# specifying a layer without using it in the config is fine (such as name_plate here)
# subtitles in .ass will always be drawn on top of these
stack = ["name", "name_plate", "portrait", "bg"]    

# directory where temp files (combined images) are stored
# keep in mind that temp files are not cleared automatically
# will be created automatically if it doesn't exist
kitchen = r"C:\project\temp"