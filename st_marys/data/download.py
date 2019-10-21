"""Download HTML for all archive web pages."""



import requests



url = "http://aomol.msa.maryland.gov/megafile/msa/speccol/sc2900/sc2908/000001/000369/html/"
pages = ["am369--{}.html".format(i + 1) for i in range(145)]
for page in pages:
    print("Downloading " + page + " ...")
    response = requests.get(url + page)
    with open("../../data/" + page, "w+") as f:
        f.write(response.text)
