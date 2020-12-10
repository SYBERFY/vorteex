def human_readable(mode, resource, findings, categories, sources):
    print('Type:', resource)
    print('Categories:', ', '.join(categories))

    for name, finding in findings.items():
        print('\n' + name)
        print(finding)

    print('\nSources:', ', '.join(sources))
