from systemAPI.serializers import SystemSerializer, SystemDetailedSerializer, UserSerializer, RulesSerializer
from systemAPI.serializers import ComponentSerializer, ComponentPropertySerializer, ComponentStateSerializer
from systemAPI.serializers import EntitySerializer, EntityStateSerializer, EntityPropertySerializer
from .models import System

def find(it, dicts):
    for d in range(0, len(dicts)):
        if dicts[d]['name'].lower() == it['name'].lower() and dicts[d]['parent'].lower() == it["parent"].lower():
            return d
    return -1


def strp(strlist):
    for st in range(0, len(strlist)):
        strlist[st] = strlist[st].strip(" \\,\n\r")
    return strlist


def xdesc(lines, i, x, fname):
    inf = lines[i].strip(" \\,\n\r")
    inf = inf.split(',')
    inf = strp(inf)
    if len(inf) == 2:
        item = {'name': inf[0], 'description': inf[1], 'parent': fname}
    elif len(inf) == 3:
        item = {'name': inf[1], 'description': inf[2], 'parent': inf[0]}

    found = find(item, x)
    if found > -1:
        x[found].update(item)

    else:
        x.append(item)


def xx(lines, i, x):
    inf = lines[i].strip(" \\,\n\r")
    inf = inf.split(',')
    inf = strp(inf)

    for prop in range(1, len(inf)):
        item = {'name': inf[prop], 'description': '', 'parent': inf[0]}
        found = find(item, x)
        if found > -1:
            x[found].update(item)
        else:
            x.append(item)


def printdic(dic):
    for i in dic:
        print(i, '\n')


def checkparent(parents, sons, fname):
    parentlist = [d['name'].lower() for d in parents]
    for son in sons:
        if son['parent'].lower() not in parentlist:
            parents.append({
                'name': son['parent'],
                'description': '',
                'parent': fname
            })
            parentlist.append(son['parent'].lower())
    return parents


def add_to_db(request, serializer, parentlist, parentname, listtocreate):
    newlist = []
    #print('adding to database')
    for l in listtocreate:
        parent = None
        for p in parentlist:
            #print(p, l['parent'])
            if p.__str__() == l['parent']:
                parent = p.pk
                break
        #print('parent', parent)
        if parent == None:
            continue
        xserializer = serializer(
            data={'name': l['name'], "description": l['description'], parentname: parent}, context={'request': request})
        # print('sssss', xserializer.is_valid(), xserializer.errors)
        if xserializer.is_valid():
            sys = xserializer.save()
            newlist.append(sys)
    return newlist


def get_file(f, name, request):
    working = None
    components = []
    cstates = []
    cprops = []
    ents = []
    estates = []
    eprops = []
    trans = []
    lines = []
    sys = None
    for li in f:
        lines.append(li.decode("utf-8"))
    # lines = f
    for i in range(0, len(lines)):
        if '#Component_Description'in lines[i]:
            working = 0
            continue
        elif '#Component_States_Description' in lines[i]:
            working = 1
            continue
        elif '#Component_States' in lines[i]:
            working = 2
            continue
        elif '#Component_Properties_Description'in lines[i]:
            working = 3
            continue
        elif '#Component_Properties' in lines[i]:
            working = 4
            continue
        elif '#Environmental_entities_description' in lines[i]:
            working = 5
            continue
        elif '#Environmental_entities_States_Description' in lines[i]:
            working = 6
            continue
        elif '#Environmental_entities_States' in lines[i]:
            working = 7
            continue
        elif '#Environmental_entities_Properties_Description' in lines[i]:
            working = 8
            continue
        elif '#Environmental_entities_Properties' in lines[i]:
            working = 9
            continue
        elif '#Transition_rules' in lines[i]:
            working = 10
            continue

        if working == 0:  # component Descriptions
            xdesc(lines, i, components, name)
        elif working == 1:  # component state descriptions
            xdesc(lines, i, cstates, name)
        elif working == 2:  # Component States
            xx(lines, i, cstates)
        elif working == 3:  # component property descriptions
            xdesc(lines, i, cprops, name)
        elif working == 4:  # component property
            xx(lines, i, cprops)
        elif working == 5:  # entity description
            xdesc(lines, i, ents, name)
        elif working == 6:  # entity state description
            xdesc(lines, i, estates, name)
        elif working == 7:  # entity state
            xx(lines, i, estates)
        elif working == 8:  # entity properties description
            xdesc(lines, i, eprops, name)
        elif working == 9:  # entity properties
            xx(lines, i, eprops)
        elif working == 10:  # transition rules
            # #print(working, lines[i])
            item = {'name': lines[i].strip(" \\,\n\r"), 'description': '', 'parent': name}
            trans.append(item)


# add_to_db(request, serializer, parentlist, parentname, listtocreate):

    #print("components\n")
    #printdic(components)
    #print("states\n")
    #printdic(cstates)
    components =     checkparent(components, cstates, name)

    #print("props\n")
    #printdic(cprops)
    components =     checkparent(components, cprops, name)

    # print("ents\n")
    # printdic(ents)

    # print("estates\n")
    # printdic(estates)
    ents = checkparent(ents, estates, name)
    # printdic(ents)

    # print("eprops\n")
    # printdic(eprops)
    ents = checkparent(ents, eprops, name)

    # print("trans\n")
    # printdic(trans)

# using add_to_db():
    # create a system save instance to variable
    sysserializer = SystemSerializer(
        data={'name': name}, context={'request': request})
    if sysserializer.is_valid():
        sys = sysserializer.save()
    # create component
    components=add_to_db(request, ComponentSerializer, [sys], 'System', components)
    # create enteties
    ents = add_to_db(request, EntitySerializer, [sys], 'System', ents)
    # create states
    add_to_db(request, ComponentStateSerializer,
                           components, 'Component', cstates)    
    add_to_db(request, EntityStateSerializer,
              ents, 'Environmental_Entity', estates)
    # create props
    add_to_db(request, ComponentPropertySerializer,
              components, 'Component', cprops)
    add_to_db(request, EntityPropertySerializer,
              ents, 'Environmental_Entity', eprops)

    # create trans rules
    add_to_db(request, RulesSerializer,[sys], 'System', trans)
