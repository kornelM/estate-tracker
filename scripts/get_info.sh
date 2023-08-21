#!/bin/bash

filename="../output.txt"
counter=1
endpoint="https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/malopolskie/krakow/krakow/krakow?distanceRadius=0&viewType=listing&limit=72&page="
isFirstCall=true
totalPages=true

echo "Removing file"
rm -f $filename
echo 'Creating file'
touch $filename
echo 'Filling file with data'
echo "{\"offers\":[">>$filename

for i in {1..1000}
do
	echo "Sending GET request: $i"
	endpoint_whole=$endpoint$counter
	echo $endpoint_whole
	line=$(curl --location --request GET $endpoint_whole -H 'Cookie: lang=pl' -H 'Accept-Encoding: text' -H 'Connection: keep-alive' -H 'Accept: */*' -H 'User-Agent: PostmanRuntime/7.32.3' -H 'Host: www.otodom.pl' -H 'Postman-Token: 1d1c53c3-391f-451d-bc69-fc3b09022152$counter' | grep -m 1 -o '<script id="__NEXT_DATA__" type="application/transformer" crossorigin="anonymous">.*</script>' | sed 's/<script id="__NEXT_DATA__" type="application\/transformer">//;s/<\/script>//' | grep -o '<script id="__NEXT_DATA__" type="application/transformer" crossorigin="anonymous">.*' | cut -f2- -d: )

  if [ "$isFirstCall" ]
  then
    totalPages=$(echo $line | grep -oP '"totalPages":\K\d+')
    echo "Found $totalPages pages"
  fi
	echo "{\"name\":\"data_$counter\",">>$filename
	echo "\"value\":"$line>>$filename

	if [ "$counter" -lt "$totalPages" ]
	then
	  echo ",">>$filename
	fi

  if [ "$counter" -eq "$totalPages" ]
  then
    echo "Reached last page, I'm ending my work"
    break
  fi

	(( counter++ ))
	echo "I'm about to sleep"
	sleep .6
  echo "======================"
  line=

done

echo "]}">>$filename


#cat $filename | jq
