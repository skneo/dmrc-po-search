import os
import requests
from bs4 import BeautifulSoup

# url = "https://www.delhimetrorail.com/pages/en/corporate/list-of-purchase-order-for-store-department"
# response = requests.get(url)
response="""<div class="container pb-3">
				<h2 class="my-4">List of Purchase Order for Store Department</h2>

				<ul class="doublelinks">
					<li><a href="https://backend.delhimetrorail.com/documents/3670/INDEX_VjV7ZeG.PDF" target="_blank"
							title="Purchase Order from 01.10.2022 to 31.12.2022 ">Purchase Order from 01.10.2022 to
							31.12.2022 </a></li>
					<li><a href="https://backend.delhimetrorail.com/documents/3445/INDEX_QS2j0Ui.PDF" target="_blank"
							title="Purchase Order from 01.07.2022 to 30.09.2022 ">Purchase Order from 01.07.2022 to
							30.09.2022 </a></li>
					<li><a href="https://backend.delhimetrorail.com/documents/2839/INDEX_k47U0vh.PDF" target="_blank"
							title="Purchase Order from 01.04.2022 to 31.03.2022 ">Purchase Order from 01.04.2022 to
							30.06.2022 </a></li>
					<li><a href="https://backend.delhimetrorail.com/documents/2429/INDEX_9_5_22.PDF" target="_blank"
							title="Purchase Order from 01.01.2022 to 31.03.2022 ">Purchase Order from 01.01.2022 to
							31.03.2022 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-DECEM21.PDF" target="_blank"
							title="Purchase Order from 01.09.2021 to 30.09.2021 ">Purchase Order from 01.10.2021 to
							31.12.2021 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-SEPT2021.PDF" target="_blank"
							title="Purchase Order from 01.09.2021 to 30.09.2021 ">Purchase Order from 01.09.2021 to
							30.09.2021 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-AUG2021.PDF" target="_blank"
							title="Purchase Order from 01.08.2021 to 31.08.2021 ">Purchase Order from 01.08.2021 to
							31.08.2021 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-JULY_2021.PDF" target="_blank"
							title="Purchase Order from 01.12.2020 to 31.07.2021">Purchase Order from 01.12.2020 to
							31.07.2021 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-JUNE20NOV20.PDF"
							target="_blank" title="Purchase Order from 1-06-2020 to 30-11-2020">Purchase Order from
							1-06-2020 to 30-11-2020 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-FEB20-MAY20.PDF"
							target="_blank" title="Purchase Order from 1-02-2020 to 31-05-2020">Purchase Order from
							1-02-2020 to 31-05-2020 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-DEC19-JAN20.PDF"
							target="_blank" title="Purchase Order from 1-12-2019 to 31-01-2020">Purchase Order from
							1-12-2019 to 31-01-2020 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-SEPT19-NOV19.PDF"
							target="_blank" title="Purchase Order from 1-09-2019 to 30-11-2019">Purchase Order from
							1-09-2019 to 30-11-2019 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-JUNE19-AUG19.PDF"
							target="_blank" title="Purchase Order from 1-06-2019 to 30-08-2019">Purchase Order from
							1-06-2019 to 30-08-2019 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-MARCH19TOMAY19.PDF"
							target="_blank" title="Purchase Order from 1-03-2019 to 31-05-2019">Purchase Order from
							1-03-2019 to 31-05-2019 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-YEARJAN19FEB19.PDF"
							target="_blank" title="Purchase Order from 1-01-2019 to 28-02-2019">Purchase Order from
							1-01-2019 to 28-02-2019 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-YEAROCT18DEC18.PDF"
							target="_blank" title="Purchase Order from 1-10-2018 to 31-12-2018">Purchase Order from
							1-10-2018 to 31-12-2018 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-JULY18SEPT18.PDF"
							target="_blank" title="Purchase Order from 1-07-2018 to 30-09-2018">Purchase Order from
							1-07-2018 to 30-09-2018 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-APIR18JUNE18.PDF"
							target="_blank" title="Purchase Order from 1-04-2018 to 30-06-2018">Purchase Order from
							1-04-2018 to 30-06-2018 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-APIR17MAR18.PDF"
							target="_blank" title="Purchase Order from 1-04-2017 to 31-03-2018">Purchase Order from
							1-04-2017 to 31-03-2018 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-APIR16MAR17.PDF"
							target="_blank" title="Purchase Order from 1-04-2016 to 31-03-2017">Purchase Order from
							1-04-2016 to 31-03-2017 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-YEAR20152016.PDF"
							target="_blank" title="Purchase Order from 1-04-2015 to 31-03-2016">Purchase Order from
							1-04-2015 to 31-03-2016 </a></li>
					<li><a href="https://backend.delhimetrorail.com/media/documents/INDEX-YEAR20142015.PDF"
							target="_blank" title="Purchase Order from 1-04-2014 to 31-03-2015">Purchase Order from
							1-04-2014 to 31-03-2015 </a></li>
				</ul>
			</div>"""
soup = BeautifulSoup(response, "html.parser")

pdf_count = 0
folder = "files"

if not os.path.exists(folder):
    os.makedirs(folder)

for link in soup.find_all("a"):
    if ".PDF" in link.get("href"):
        pdf_count += 1
        pdf_url = link.get("href")
        response = requests.get(pdf_url, timeout=5)
        file_name = pdf_url.split("/")[-1]
        file_path = os.path.join(folder, file_name)
        with open(file_path, "wb") as f:
            f.write(response.content)

print(f"Number of PDF files downloaded: {pdf_count}") 
