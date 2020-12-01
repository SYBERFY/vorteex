from PyInquirer import prompt


def checkbox(message, choices):
    question = {
        'type': 'checkbox',
        'message': message,
        'name': 'default',
        'choices': [dict(name=choice) for choice in choices]
    }

    return prompt(question).get('default')


def input(message):
    question = {
        'type': 'input',
        'name': 'default',
        'message': message,
    }

    return prompt(question).get('default')


def confirm(message):
    question = {
        'type': 'confirm',
        'name': 'default',
        'message': message,
    }

    return prompt(question).get('default')
