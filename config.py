# Configuration settings for different PDF layouts
standard_columns = [
    "Compagnie", "N° Agent", "Contractant", "Echéance", "Nature de l'opération (code)", "Nature de l'opération (libellé)", "Catégorie Branche",
    "Police", "N° Facture", "Débit", "Crédit", "Emmission",
]



AG_settings={
    "columns":[
        "Contractant", "null", "Echéance", "Nature de l'opération (code)", "Nature de l'opération (libellé)", "Catégorie Branche",
        "Police", "R1", "Débit", "R2", "Crédit", "Emmission", "S", "Cie"
    ],
    "crop_settings":{
    },
    "data_row_top":2,
    "data_row_bot":0,
    "nb_pages":0,
    "extract_settings":{
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "snap_y_tolerance": 4,
        "intersection_x_tolerance": 15,
    },
    "mandatory_columns": ["Contractant", "Emmission"],
    "Emmision_format": "%d",
    "agent_pattern": r"compte\s*N\s*[˚°]\s*([A-Z0-9\-\/]+)\s*relev",
}

NN_settings={
    "columns":[
        "Contractant","Echéance","Nature de l'opération (code)", "Police", "Débit", "Crédit", "Emmission"
    ],
    "crop_settings":{
    },
    "data_row_top":1,
    "data_row_bot":0,
    "nb_pages":0,
    "extract_settings":{
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "snap_y_tolerance": 4,
        "intersection_x_tolerance": 15,
    },
    "mandatory_columns": ["Nature de l'opération (code)", "Emmission"],
    "Emmision_format": "%d/%m/%Y",
    "agent_pattern": r"producteur\s*N\s*[˚°]\s*([A-Z0-9\-\/]+)\s*de",
}

Allianz_settings={
    "columns":[
        "Nature de l'opération (code)", "N° Facture", "Contractant", "Police", "Débit", "Crédit", "Emmission"
    ],
    "crop_settings":{
    },
    "data_row_top":1,
    "data_row_bot":0,
    "nb_pages":0,
    "extract_settings":{
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "snap_y_tolerance": 4,
        "intersection_x_tolerance": 15,
    },
    "mandatory_columns": ["Nature de l'opération (code)", "Emmission"],
    "Emmision_format": "%d.%m.%Y",
    "agent_pattern": r"producteur\s*N\s*[˚°]\s*:\s*([A-Z0-9\-\/]+)\s*[0-9]",
}

Baloise_settings={
    "columns":[
        "Contractant", "Référence", "Echéance",
          "Nature de l'opération (code)", "Police", "Sinistre", "Débit", "null", "Crédit", "null2", "Emmission"
    ],
    "crop_settings":{
        "vertical_strategy": "text",
        "horizontal_strategy": "text",
    },
    "extract_settings":{
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [40,210, 255, 305, 460, 500, 555, 622, 632, 725, 735, 802]
    },
    "mandatory_columns": ["Nature de l'opération (code)", "Emmission"],
    "Emmision_format": "%d/%m/%Y",
    "agent_pattern": r"Intermédiaire\s*([A-Z0-9\-\/]+)\s*",
    "data_row_top":1,
    "data_row_bot":0,
    "nb_pages":0,
}
DAS_settings={
    "columns":[
        "Contractant", "Echéance", "Nature de l'opération (code)", "Catégorie Branche", "Police", "Débit", "Crédit", "Emmission"
    ],
    "crop_settings":{
    },
    "data_row_top":1,
    "data_row_bot":0,
    "nb_pages":0,
    "extract_settings":{
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "snap_y_tolerance": 4,
        "intersection_x_tolerance": 15,
    },
    "mandatory_columns": ["Nature de l'opération (code)", "Emmission"],
    "Emmision_format": "%d/%m/%Y",
    "agent_pattern": r"PRODUCTEUR\s*:\s*([A-Z0-9\-\/]+)\s*",
}

Vivium_settings={
    "columns":[
        "Contractant", "Echéance",
          "Nature de l'opération (code)", "Catégorie Branche", "Police", "null", "Débit", "null2", "Crédit", "Emmission", "observation"
    ],
    "crop_settings":{
        "vertical_strategy": "text",
        "horizontal_strategy": "text",
    },
    "extract_settings":{
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [28,140, 195, 300, 320, 380, 390, 445, 455, 515, 530, 580]
    },
    "mandatory_columns": ["Nature de l'opération (code)", "Emmission"],
    "Emmision_format": "%d",
    "agent_pattern": r"Producteur\s*:\s*[0-9\-]*\s*/([A-Z0-9\-\/]+)\s*",
    "data_row_top":1,
    "data_row_bot":0,
    "nb_pages":0,
}

DKV_settings={
    "columns":[
        "N° Agent", "Nature de l'opération (code)", "Nature de l'opération (libellé)", "Police", "Contractant", "null", "null2", "null3",
        "Echéance", "Emmission", "Débit", "Crédit",
    ],
    "crop_settings":{
        "vertical_strategy": "text",
        "horizontal_strategy": "text",
    },
    "data_row_top":1,
    "data_row_bot":0,
    "nb_pages":0,
    "extract_settings":{
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [57,107,140, 200,230, 293, 318, 383, 417, 450,480,499,513]
    },
    "mandatory_columns": ["Nature de l'opération (code)", "Emmission"],
    "Emmision_format": "%Y-%m-%d",
    "agent_pattern": "",
}

company_lst = {"Vivium":Vivium_settings,"Allianz":Allianz_settings, "Baloise":Baloise_settings, "DKV":DKV_settings, "NN":NN_settings, 
                "DAS":DAS_settings,"AG":AG_settings}