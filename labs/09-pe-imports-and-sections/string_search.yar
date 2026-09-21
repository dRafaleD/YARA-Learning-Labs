rule String_Search_GetLastError
{
    meta:
        author = "dRafaleD"
        description = "Harmless contrast rule: content search for GetLastError"
        lab = "09"
        purpose = "education"

    strings:
        $api = "GetLastError"

    condition:
        $api
}
