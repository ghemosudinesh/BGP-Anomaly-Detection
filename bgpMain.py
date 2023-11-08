class BGPMain:
    ASID = 0;
    timeStamp = '';
    mrtHeaderLength = '';
    peerASNumber = 0;
    localASNumber = 0;
    peerIPAddress = '';
    localIPAddress = '';
    bgpMessageLength = 0;
    withdrawnRoutesLength = 0;
    bgpWithdrawnRoutes = 0;
    totalPathAttributeLength = 0;
    nlri = 0;
    pathAttributes = 0;

class ASNLRI:
    ASID = 0;
    nlri = '';
    withdrawnRoutes = '';
    mpReachNLRI = '';
    mpUnreachWR = '';

class PathAttribute:
    ASID = 0;
    flagsTypeLength = '';
    serialNumber = 0;
    pathType = '';
    pathAttributeValue = '';
    asPathSegmentLength = 0;
    asPathSegmentValue = 0;
    mpReachNlriLength = 0
    mpReachNlriNextHop = '';
    mpReachNlri = '';
    mpUnreachNlriWR = '';

class TimestampDetails:
    timestamp = '';
    ACount = 0;
    WCount = 0;
    IGPCount = 0;
    EGPCount = 0;
    InCompleteCount = 0;

    ASPathLengthList = [];
    maxASPathLength = 0;
    avgASPathLength = 0;
    avgUniqueASPathLength = 0;
    announcedNLRI = 0;
    withdrawnNLRI = 0;
    
    
    
    

    
