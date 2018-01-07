BEGIN{
    path = "/data/raw/ZIPincome/"
    command = "zcat " path "IncomePop.gz"
    temp = "./tempZips"
    output_file = "./NYCzips"
    final = "./NYCzipsSorted"
    FS = "|"
    OFS = "|"

    #extracting out all of the nyc zip codes from income and population data
    while((command |  getline)> 0){
	if (($1 < 10300) && ($1 > 10000)){
	    print $3, $1, $4 |" sort -g >"  output_file
	    }
    }


}
