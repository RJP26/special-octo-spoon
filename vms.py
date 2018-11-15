def vms_local_ads(ad_log):
    """ Function receives VMS logs as a list and creates output file with specific local ad attempts only. """
    print("------------\nIn function\n------------")
    keywords = ['0653: (INFO)  processCueTones', 'VMSApp(1712) None: {event} TAD', 'TuneToAdChannel', 'VMSApp(1859) Error: Debug: {event} TAD', 'CurrUri', 'Tune2AdChannel', 
                'mediamanager(1173) Debug: {event} TAD', 'TuneBack2ContentChannel', 'Tune2AdChannel', '0885: (ERROR)']
    for line in ad_log:
        for key in keywords:
            if key in line:
                print(line.rstrip())
                file = open('testfile.txt', 'a', encoding="ansi")
                file.write(line.rstrip() + "\r")
    print("------------\nOut of Function\n------------")

# Reads each line of VMS logclient file into a list.            
with open('VMS3log.txt', encoding="ansi") as file_object:
    lines = file_object.readlines()

vms_local_ads(lines)