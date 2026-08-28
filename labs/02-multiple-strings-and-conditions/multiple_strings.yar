rule Suspicious_Download_Pattern
{
    strings:
        $download = "DOWNLOAD_FILE"
        $execute  = "EXECUTE_FILE"
        $network  = "REMOTE_SERVER"

    condition:
        2 of them
}
