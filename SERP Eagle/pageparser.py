"""
This module is responsible for parsing web page
OR
Dealing with elements on page
"""

from playwright.sync_api import TimeoutError


class Parser:

    def __init__(self, page) -> None:
        self.page = page

    def get_element(self, css_selector, parent=None, many=False):
        """
        This function acts as a wrapper for the Playwright's element selection API.

        Args:
            - css_selector (str): A CSS selector used to choose elements.
            - parent (Locator): This should be a Locator object. If you wish to locate an element within a sub-tree of another element, provide it as the 'parent' argument.
            - many (bool): This is a boolean parameter. Set it to True if you intend to select multiple elements.

        Returns:
            - A Locator object or a list of Locator objects.
            - None: If the selector does not match any elements.
        """

        try:
            if parent:
                result = parent.locator(css_selector)

                if result.count() > 0:

                    if many:
                        result = result.all()

                    else:
                        result = result.first
                else:
                    result = None

            else:
                result = self.page.locator(css_selector)
                if result.count() > 0:
                    if many:
                        result = result.all()

                    else:
                        result = result.first

                else:

                    result = None

        except TimeoutError:
            # If element is not found, return none
            result = None

        return result

    def get_element_text(self, css_selector, parent=None):
        """Will use to get text from an element
        Args:
            - css_selector (str): A CSS selector used to choose elements.
            - parent (Locator): This should be a Locator object. If you wish to locate an element within a sub-tree of another element, provide it as the 'parent' argument.

        Return:
            - String of text
            - None    
        """

        try:
            if parent:
                element = self.get_element(
                    css_selector=css_selector, parent=parent)
            else:
                element = self.get_element(css_selector=css_selector)

            if element != None:
                return element.text_content()

            return None
        except TimeoutError:
            return None

    def get_text_of_locator(self, locator):
        """It will be used, when you have locator object and want to get its text, unlike get_element_text
        in which you have to give css selector

        Args:
            - Locator (Locator)

        """

        try:
            return locator.text_content()

        except TimeoutError:
            return None

    def get_element_attribute(self, css_selector, value, parent=None):
        """This will be used to get attribute of an alements.
        Args:
            - css_selector (str): A CSS selector used to choose elements.
            - value (str): Name of attribute that you wanna find
            - parent (Locator): This should be a Locator object. If you wish to locate an element within a sub-tree of another element, provide it as the 'parent' argument.
        Return:
            - String of value of attribute
            - None

        """

        try:

            if parent:
                element = self.get_element(
                    css_selector=css_selector, parent=parent)
            else:
                element = self.get_element(css_selector=css_selector)

            if element != None:
                return element.get_attribute(value)

            return None

        except TimeoutError:
            return None

    def get_hidden_element_text(self, css_selector, parent=None):
        """We cannot get answer of questions, as they are hidden and can be seen by clicking on it.
        But, we can get it through Js. So this will be used to get answers text
        Args:
            - css_selector (str): A CSS selector used to choose elements.
            - parent (Locator): This should be a Locator object. If you wish to locate an element within a sub-tree of another element, provide it as the 'parent' argument.

        Return:
            - String of element text
            - None



        """

        js_code_with_parent = f''' (parent) => {{
                //Use parent as the context to find the child element
                const child = parent.querySelector('{css_selector}');
                return child.textContent;}}'''

        js_code_with_page = f'''
                // Use parent as the context to find the child element
                const child = document.querySelector('{css_selector}');
                return child.textContent;
                '''

        try:
            if parent:
                return str(parent.evaluate_handle(js_code_with_parent))
            else:
                return str(self.page.evaluate(js_code_with_page))
        except:
            return None
