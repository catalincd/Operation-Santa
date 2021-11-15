import Utils;

def GetPageString(pagePath, pageProperties = {}):
    staticPage = Utils.GetStringFromFile('./templates/' + pagePath)

    parts = staticPage.split('&&')
    page = ""

    for i in range(len(parts)):
        if i % 2 == 0:
            page += parts[i]
        else:
            if parts[i] in pageProperties:
                page += pageProperties[parts[i]]
            else:
                page += parts[i]

    return page