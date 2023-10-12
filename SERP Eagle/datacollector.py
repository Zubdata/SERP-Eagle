"""
This module is designed for collecting data.
"""

import logging
from datasaver import DataSaver


class DataCollector:

    def __init__(self, page_parser_obj) -> None:
        self.page_parser = page_parser_obj

    def organic_results_parsing(self):
        """To collect organic results"""

        organic_results_data_list = []

        all_orgainic_results = self.page_parser.get_element(
            css_selector='div[jscontroller="SC7lYd"]', many=True)

        if all_orgainic_results != None:

            for results in all_orgainic_results:
                heading = self.page_parser.get_element_text(
                    '.yuRUbf h3.LC20lb.MBeuO.DKV0Md', parent=results)
                url = self.page_parser.get_element_attribute(
                    '.yuRUbf a', parent=results, value='href')
                meta_description = self.page_parser.get_element_text(
                    'div[data-snf="nke7rc"]', parent=results)
                image_url = self.page_parser.get_element_attribute(
                    'div[data-snf="Vjbam"] img', parent=results, value="src")

                organic_results_data_list.append({
                    "Heading": heading,
                    "Url": url,
                    "Meta description": meta_description,
                    "Image url": image_url

                })

        return {
            "Organic Results": organic_results_data_list
        }

    def featured_snippet(self):
        """To get fatured snippet"""

        featured_snippet = self.page_parser.get_element(
            css_selector=".xpdopen")

        heading = self.page_parser.get_element_text(
            '.yuRUbf h3.LC20lb.MBeuO.DKV0Md', parent=featured_snippet)
        url = self.page_parser.get_element_attribute(
            '.yuRUbf a', parent=featured_snippet, value="href")
        description = self.page_parser.get_element_text(
            '[class="wDYxhc"]', parent=featured_snippet)

        return {
            "Featured Snippet": {
                "Heading": heading,
                "Url": url,
                "Description": description
            }
        }

    def people_also_ask(self):
        """To collect questions that people also ask, with thier answers"""

        people_also_ask_data_list = []

        all_people_ask_question_elements = self.page_parser.get_element(
            css_selector='[jsname="yEVEwb"]', many=True)

        if all_people_ask_question_elements != None:
            for question in all_people_ask_question_elements:

                question_text = self.page_parser.get_element_text(
                    parent=question, css_selector='[class="CSkcDe"]')
                answer = self.page_parser.get_hidden_element_text(
                    css_selector='[jsname="yEVEwb"] [class="wDYxhc"]', parent=question)
                

                people_also_ask_data_list.append({
                    "Question": question_text,
                    "Answer": answer
                })

        return {
            "People Also Ask": people_also_ask_data_list
        }

    def related_searches(self):
        """To collect related queries or searches"""

        related_searches_data_list = []
        all_reslted_searches = self.page_parser.get_element(
            css_selector='.k8XOCe ', many=True)
        if all_reslted_searches != None:
            for related_search in all_reslted_searches:
                related_search_text = self.page_parser.get_text_of_locator(
                    locator=related_search)
                related_searches_data_list.append(related_search_text)

        return {
            "Related Searches": related_searches_data_list
        }

    def paid_ads(self):
        """To get paid(Ad) resutls"""

        paid_ads_list = []
        all_paid_ads = self.page_parser.get_element(
            css_selector='[class="uEierd"]', many=True)
        if all_paid_ads != None:
            for paid_ad in all_paid_ads:
                ad_heading = self.page_parser.get_element_text(
                    css_selector='[class="sVXRqc"] div[role="heading"]', parent=paid_ad)
                ad_url = self.page_parser.get_element_attribute(
                    css_selector='[class="sVXRqc"]', parent=paid_ad, value="href")
                ad_meta_description = self.page_parser.get_element_text(
                    css_selector='[class="MUxGbd yDYNvb lyLwlc"]', parent=paid_ad)

                paid_ads_list.append({
                    "Heading": ad_heading,
                    "Url": ad_url,
                    "Meta description": ad_meta_description
                })

        return {
            "Paid Ads": paid_ads_list
        }

    def main(self):

        main_data_dict = {}
        logging.info("collecting organic results")
        main_data_dict.update(self.organic_results_parsing())
        logging.info("organic results have been scraped")

        logging.info("collecting Featured snippet")
        main_data_dict.update(self.featured_snippet())
        logging.info("Featured snippet has been scraped")

        logging.info("collecting People also ask")
        main_data_dict.update(self.people_also_ask())
        logging.info("People also ask has been scraped")

        logging.info("collecting related searches")
        main_data_dict.update(self.related_searches())
        logging.info("Related searches has been scraped")

        logging.info("collecting Paid ads")
        main_data_dict.update(self.paid_ads())
        logging.info("Paid ads has been scraped")

        DataSaver.save_data(data=main_data_dict)
