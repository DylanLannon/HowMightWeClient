questions = [
    {
        "question": "What is the name of your charity?",
        "input_type": "text"
    },
    {
        "question": "How many boxes would you like to have for each component?",
        "input_type": "range",
        "slider_range": [[1, 8], [1, 8], [1, 8], [1, 8], [1, 8]],
        "slider_num": 5,
        "subtitle": ["Inputs","Activities","Outputs","Outcomes","Impacts"]
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
        "question": "What resources are needed to succeed?",
        "input_type": "textarea",
        "toc_component": "Inputs"
    },
    {
        "question": "How will you mitigate the problems you are trying to address?",
        "input_type": "textarea",
        "toc_component": "Activities"
    },
    {
        "question": "How do you know your solutions have been successfully implemented?",
        "input_type": "textarea",
        "toc_component": "Outputs"
    },
    {
        "question": "What are the differences you expect to see from your work?",
        "input_type": "textarea",
        "toc_component": "Outcomes"
    },
    {
        "question": "What are the long-term goals you are trying to achieve?",
        "input_type": "textarea",
        "toc_component": "Impacts"
    }
]