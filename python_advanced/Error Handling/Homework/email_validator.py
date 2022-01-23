import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ['com', 'bg', 'org', 'net']

user = input()
while user != 'End':
    if '@' not in user:
        raise MustContainAtSymbolError('Email must contain @')
    if len(re.findall(r'[a-zA-Z]+@', user)[0]) <= 5:
        raise MustContainAtSymbolError('Name must be more than 4 characters')
    elif user.split('.')[1] not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: .{', .'.join(valid_domains)}")
    else:
        print('Email valid')

    user = input()
