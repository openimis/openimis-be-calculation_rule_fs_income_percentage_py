CLASS_RULE_PARAM_VALIDATION = [
    {
        "class": "ContributionPlan",
        "parameters": [
            {
                "type": "number",
                "name": "rate",
                "label": {
                    "en": "Percentage of income",
                    "fr": "Pourcentage du salaire"
                },
                "rights": {
                    "read": "151201",
                    "write": "151202",
                    "update": "151203",
                    "replace": "151206",
                },
                'relevance': "True",
                'condition': "INPUT>1",
                "default": "5"
            },
        ],
    },
    {
        "class": "ContractDetails",
        "parameters": [
            {
                "type": "number",
                "name": "income",
                "label": {
                    "en": "Income",
                    "fr": "Salaire"
                },
                "rights": {
                    "read": "152101",
                    "write": "152102",
                    "update": "152103",
                    "replace": "152103",
                },
                "relevance": "True",
                "condition": "INPUT>100",
                "default": ""
            }
        ],
    },
    {
        "class": "PolicyHolderInsuree",
        "parameters": [
            {
                "type": "number",
                "name": "income",
                "label": {
                    "en": "Income",
                    "fr": "Salaire"
                },
                "rights": {
                    "read": "150201",
                    "write": "150202",
                    "update": "150203",
                    "replace": "150206",
                },
                "relevance": "True",
                "condition": "INPUT>100",
                "default": ""
            }
        ],
    },
]

DESCRIPTION_CONTRIBUTION_VALUATION = F"" \
                                     F"This calcutation will add the income in the contract details " \
                                     F"and PHinsuree and the percentage in the Contribution plan" \
                                     F" so when a contract valuation is requested then the calculation will" \
                                     F" determine the value based on the contract details income and CP percentage"

FROM_TO = []
