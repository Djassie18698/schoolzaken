def writer2():
    bestand = open("configopdracht4.txt", "a")
    getallen = ['acceptance_wait_time: 10', 'auth_timeout: 60', 'include:', '- /etc/salt/extra_config', '- /etc/roles/webserver']
    for i in getallen:
        bestand.write("#" +i+ "\n")
    bestand.close()
    bestand= open("log.txt", "a")
    bestand.write("regel wordt geprint \n")
    bestand.close()

writer2()