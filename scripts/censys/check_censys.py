import censys.ipv4
c = censys.ipv4.CensysIPv4(api_id="SUA-API-ID", api_secret="SUA-API-SECRET")

# the report method constructs a report using a query, an aggretaion field, and the 
# number of buckets to bin
c.report(""" "welcome to" AND tags.raw: "http" """, field="80.http.get.headers.server.raw", buckets=5)

# the view method lets you see the full JSON for an IP address
c.view('8.8.8.8')

# the search method lets you search the index using indexed fields, full text, and 
# combined predicates
for result in c.search("80.http.get.headers.server: Apache AND location.country: Japan", max_records=10):
    print result

# you can optionally specify which fields you want to come back for search results
IPV4_FIELDS = ['ip',
		 'updated_at',
		 '80.http.get.title',
		 '443.https.get.title',
		 '443.https.tls.certificate.parsed.subject_dn',
		 '443.https.tls.certificate.parsed.names',
		 '443.https.tls.certificate.parsed.subject.common_name',
		 '443.https.tls.certificate.parsed.extensions.subject_alt_name.dns_names',
		 '25.smtp.starttls.tls.certificate.parsed.names',
		 '25.smtp.starttls.tls.certificate.parsed.subject_dn',
		 '110.pop3.starttls.tls.certificate.parsed.names',
		 '110.pop3.starttls.tls.certificate.parsed.subject_dn']

data = list(c.search("80.http.get.headers.server: Apache AND location.country: Japan", 
                             IPV4_FIELDS, max_records=10))		 
print data