from body import startPaging, getItemPages, startScraping



if __name__ == '__main__':
    url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=amante&rh=i%3Aaps%2Ck%3Aamante"
    a = startPaging(url,"#pagnNextLink")
    b = getItemPages(a, ".a-size-small.a-text-normal")
    startScraping(b) #(b, xpathlist, output)