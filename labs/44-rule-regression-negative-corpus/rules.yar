rule Training_Paired_Markers {
    meta:
        purpose = "Synthetic regression fixture; no real malware signatures"
    strings:
        $start = "COURSE:ALPHA" ascii
        $end = "COURSE:OMEGA" ascii
    condition:
        $start and $end and filesize < 1KB
}
