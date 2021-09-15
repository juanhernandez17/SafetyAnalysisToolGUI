def xdesc(datalist):
    result = ''
    for c in datalist:
        name = c['name']
        description = c['description']
        if description != '':
            result+= f'{name}, {description}\n'
        else:
            result+= f'{name}, Description\n'
    return result
def xxdesc(datalist, sorp):
    result = ''
    for c in datalist:
        cname = c['name']
        for p in c[sorp]:
            name = p['name']
            description = p['description']
            if description != '':
                result += f'{cname}, {name}, {description}\n'
    return result
def xlist(datalist, sorp):
    result = ''
    parentlist = []
    for c in datalist:
        name = c['name']
        parentlist = [d['name'] for d in c[sorp]]
        if len(parentlist) > 0:
            conc = name + ', ' + ', '.join(parentlist)+'\n'
            result += conc
    return result
def generate_file(data):
    fi = ''
    # print components with descriptions if no description print 'Description'
    fi+='#Component_Description\n'
    fi+=xdesc(data['components'])
# print component states
    fi+='#Component_States\n'
    fi+=xlist(data['components'],'states')

# print component state descriptions if available
    fi+='#Component_States_Description\n'
    fi+=xxdesc(data['components'], 'states')

# print component properties
    fi+='#Component_Properties\n'
    fi+=xlist(data['components'], 'properties')

# print component properties descriptions if available
    fi+='#Component_Properties_Description\n'
    fi+=xxdesc(data['components'], 'properties')
# print envent with descriptions if no description print 'Description'
    fi+='#Environmental_entities_description\n'
    fi+=xdesc(data['entities'])
# print envent states
    fi+='#Environmental_entities_States\n'
    fi+=xlist(data['entities'], 'states')
# print envent state descriptions if available
    fi+='#Environmental_entities_States_Description\n'
    fi+=xxdesc(data['entities'], 'states')
# print envent properties
    fi+='#Environmental_entities_Properties\n'
    fi+=xlist(data['entities'], 'properties')
# print envent properties descriptions if available
    fi+='#Environmental_entities_Properties_Description\n'
    fi+=xxdesc(data['entities'], 'properties')
# print rules
    fi+='#Transition_rules\n'
    for r in data['rules']:
        name = r['name']
        fi+=f'{name}\n'
    return fi