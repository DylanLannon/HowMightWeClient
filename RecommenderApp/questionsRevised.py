# This is a list of questions created after the third meeting with Hannah Underwood. 

# Once implemented correctly in the future, these questions will be able to automatically fill the boxes in the diagram 
# based on the options chosen, rather than the previous solution where the user had too much freedom and no guidance.
# To use this, replace the question import dependency in app.py to this files' name.
questions = [
    {
        "question": "What is the name of your charity?",
        "input_type": "text"
    },
    {
        "question": "What type of charity work do you do?",
        "input_type": "radio",
        "options": [
            "Animal Welfare",
            "Childcare",
            "Education",
            "Healthcare",
            "Medical Research",
            "Environmental Protection",
            "Public Benevolent Institution",
            "Food Bank",
            "Community Shed",
            "Other"
        ]
    },
    {
        "question": "What is the core mission of your charity?",
        "input_type": "radio",
        "options": [
            "maintaining relationships",
            "change existing policies",
            "achieving a specific goal",
            "fundraising",
            "public benefit",
            "safeguarding the community"
        ],
        "toc_component": "Impacts"
    },
    {
        "question": "How do you think your charity is going to affect the community?",
        "input_type": "radio",
        "options": [
            "Needs will be addressed",
            "Awareness will increase",
            "More information will be available",
            "Provide a voice for your mission",
            "Inspire other people to do the same",
            "Financial aid"
        ],
        "toc_component": "Outcomes"
    },
    {
        "question": "Who is mainly interested in your charity?",
        "input_type": "radio",
        "options": [
            "Volunteers",
            "Employees",
            "Donators",
            "Community",
            "Government",
            "Beneficiaries",
            "Partners"
        ],
        "toc_component": "Inputs"
    },
    {
        "question": "What kind of advancements are you aiming to achieve?",
        "input_type": "radio",
        "options": [
            "Promoting your goals",
            "Community relief",
            "Direct changes that propel you towards your goals",
            "Create more opportunities to help"
        ],
        "toc_component": "Outputs"
    },
    {
        "question": "What strategies are you going to use to make changes happen?",
        "input_type": "radio",
        "options": [
            "Community interaction",
            "Campaigns",
            "Training programs",
            "Direct services"
        ],
        "toc_component": "Activities"
    }
]