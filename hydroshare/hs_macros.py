import os
import time

from selenium.webdriver.common.keys import Keys

from dateutil import parser
from hs_elements import HomePage, AppsPage, DiscoverPage, ResourcePage, \
    HelpPage, AboutPage, APIPage, LoginPage, ProfilePage, GroupsPage, \
    GroupPage, NewGroupModal, MyResourcesPage
from timing import HSAPI_GUI_RESPONSE


class Home:
    def to_my_resources(self, driver):
        HomePage.to_my_resources.click(driver)

    def to_discover(self, driver):
        HomePage.to_discover.click(driver)

    def to_apps(self, driver):
        HomePage.to_apps.click(driver)

    def to_help(self, driver):
        HomePage.to_help.click(driver)

    def to_about(self, driver):
        HomePage.to_about.click(driver)

    def to_collaborate(self, driver):
        HomePage.to_collaborate.click(driver)

    def login(self, driver, username, password):
        HomePage.to_login.click(driver)
        LoginPage.username.inject_text(driver, username)
        LoginPage.password.inject_text(driver, password)
        LoginPage.submit.click(driver)

    def to_profile(self, driver):
        HomePage.profile_image.click(driver)
        HomePage.profile_button.click(driver)


class Apps:
    def show_info(self, driver, num):
        AppsPage.info(num).click(driver)

    def count(self, driver):
        return AppsPage.container.get_immediate_child_count(driver)

    def to_resource(self, driver, num):
        AppsPage.resource(num).click(driver)

    def get_title(self, driver, num):
        return AppsPage.title(num).get_text(driver)


class Discover:
    def sort_order(self, driver, option):
        """ Set the sort order to {{option}} """
        DiscoverPage.sort_order.select_option_text(driver, option)

    def sort_direction(self, driver, option):
        """ Set the sort direction to {{option}} """
        DiscoverPage.sort_direction.select_option_text(driver, option)

    def to_resource(self, driver, title):
        """ Navigate to the {{title}} resource landing page by clicking
        on it within the table
        """
        DiscoverPage.to_resource(title).click(driver)

    def col_index(self, driver, col_name):
        """ Indentify the index for a discover page column, given the
        column name.  Indexes here start at one since the
        end application here is xpath, and those indexes are 1 based
        """
        num_cols = DiscoverPage.col_headers.get_child_count(driver)
        for i in range(1, num_cols+1):
            name_to_check = DiscoverPage.col_index(i).get_text(driver)
            if name_to_check == col_name:
                return i
        return 0

    def check_sorting_multi(self, driver, column_name, ascend_or_descend):
        """ Check discover page rows are sorted correctly.  The automated
        testing system checks the first eight rows against the rows that
        are 1, 2, and 3 positions down, relative to the base row (a total
        of 24 checks)
        """
        baseline_rows = 8
        all_pass = True
        for i in range(1, baseline_rows):
            for j in range(1, 4):
                if not self.check_sorting_single(driver, column_name,
                                                 ascend_or_descend, i, i+j):
                    all_pass = False
        return all_pass

    def check_sorting_single(self, driver, column_name, ascend_or_descend,
                             row_one, row_two):
        """ Confirm that two rows are sorted correctly relative to
        eachother
        """
        col_ind = self.col_index(driver, column_name)
        if column_name == 'Title':
            first_element = DiscoverPage.cell_strong_href(col_ind, row_one)
            second_element = DiscoverPage.cell_strong_href(col_ind, row_two)
            first_two_vals = [first_element.get_text(driver),
                              second_element.get_text(driver)]
        elif column_name == 'First Author':
            first_element = DiscoverPage.cell_href(col_ind, row_one)
            second_element = DiscoverPage.cell_href(col_ind, row_two)
            first_two_vals = [first_element.get_text(driver),
                              second_element.get_text(driver)]
        else:
            first_element = DiscoverPage.cell(col_ind, row_one)
            second_element = DiscoverPage.cell(col_ind, row_two)
            first_two_vals = [first_element.get_text(driver),
                              second_element.get_text(driver)]
        if ('Date' in column_name) or (column_name == 'Last Modified'):
            date_one = parser.parse(first_two_vals[0])
            date_two = parser.parse(first_two_vals[1])
            if ascend_or_descend == 'Descending':
                return date_one >= date_two
            elif ascend_or_descend == 'Ascending':
                return date_one <= date_two
        else:
            value_one, value_two = first_two_vals
            if ascend_or_descend == 'Descending':
                return value_one >= value_two
            elif ascend_or_descend == 'Ascending':
                return value_one <= value_two

    def filters(self, driver, author=None, subject=None, resource_type=None,
                owner=None, variable=None, sample_medium=None, unit=None,
                availability=None):
        """ Use the filters on the left side of the Discover interface.
        Filters should include author(s) {{author}}, subject(s) {{subject}},
        resource type(s) {{resource_type}}, owner(s) {{owner}}, variables
        {{variable}}, sample medium(s) {{sample_medium}}, unit(s) {{unit}},
        and availability(s) {{availability}}
        """
        if type(author) is list:
            for author_item in author:
                filter_el = DiscoverPage.filter_author(author_item)
                filter_el.click(driver)
        elif author is not None:
            filter_el = DiscoverPage.filter_author(author)
            filter_el.click(driver)
        if type(subject) is list:
            for subject_item in subject:
                filter_el = DiscoverPage.filter_subject(subject_item)
                filter_el.click(driver)
        elif subject is not None:
            filter_el = DiscoverPage.filter_subject(subject)
            filter_el.click(driver)
        if type(resource_type) is list:
            for resource_type_item in resource_type:
                filter_el = DiscoverPage.filter_resource_type(resource_type_item)
                filter_el.click(driver)
        elif resource_type is not None:
            filter_el = DiscoverPage.filter_resource_type(resource_type)
            filter_el.click(driver)
        if type(owner) is list:
            for owner_item in owner:
                filter_el = DiscoverPage.filter_owner(owner_item)
                filter_el.click(driver)
        elif owner is not None:
            filter_el = DiscoverPage.filter_owner(owner)
            filter_el.click(driver)
        if type(variable) is list:
            for variable_item in variable:
                filter_el = DiscoverPage.filter_variable(variable_item)
                filter_el.click(driver)
        elif variable is not None:
            filter_el = DiscoverPage.filter_variable(variable)
            filter_el.click(driver)
        if type(sample_medium) is list:
            for sample_medium_item in sample_medium:
                filter_el = DiscoverPage.filter_sample_medium(sample_medium_item)
                filter_el.click(driver)
        elif sample_medium is not None:
            filter_el = DiscoverPage.filter_sample_medium(sample_medium)
            filter_el.click(driver)
        if type(unit) is list:
            for unit_item in unit:
                filter_el = DiscoverPage.filter_unit(unit_item)
                filter_el.click(driver)
        elif unit is not None:
            filter_el = DiscoverPage.filter_unit(unit)
            filter_el.click(driver)
        if type(availability) is list:
            for availability_item in availability:
                filter_el = DiscoverPage.filter_availability(availability_item)
                filter_el.click(driver)
        elif availability is not None:
            filter_el = DiscoverPage.filter_availability(availability)
            filter_el.click(driver)


class Resource:
    def size_download(self, driver, BASE_URL):
        """ Check the size of the BagIt download """
        download_href = ResourcePage.bagit.get_href(driver, BASE_URL)
        os.system('wget -q {}'.format(download_href))
        download_file = download_href.split('/')[-1]
        file_size = os.stat(download_file).st_size
        os.system('rm {}'.format(download_file))
        return file_size

    def open_with_jupyterhub(self, driver):
        ResourcePage.open_with.click(driver)
        ResourcePage.open_jupyterhub.click(driver)

    def get_title(self, driver):
        return ResourcePage.title.get_text(driver)


class Help:
    def open_core(self, driver, index):
        HelpPage.core_item(index).click(driver)

    def count_core(self, driver):
        return HelpPage.core_root.get_immediate_child_count(driver)

    def get_core_topic(self, driver, index):
        return HelpPage.core_item(index).get_text(driver)

    def to_core_breadcrumb(self, driver):
        HelpPage.core_breadcrumb.click(driver)

    def to_footer_terms(self, driver):
        HelpPage.footer_terms.click(driver)

    def to_footer_privacy(self, driver):
        HelpPage.footer_privacy.click(driver)

    def to_footer_sitemap(self, driver):
        HelpPage.footer_sitemap.click(driver)

    def get_title(self, driver):
        return HelpPage.title.get_text(driver)


class About:
    def toggle_tree(self, driver):
        AboutPage.tree_root.click(driver)

    def expand_tree_top(self, driver, item):
        item = item.replace(' ', '-').lower()
        AboutPage.tree_top(item).click(driver)

    def open_policy(self, driver, policy):
        policy = policy.replace(' ', '-').lower()
        AboutPage.tree_policy(policy).click(driver)

    def get_title(self, driver):
        return AboutPage.article_title.get_text(driver)


class API:
    def expand_hsapi(self, driver):
        APIPage.hsapi.click(driver)

    def endpoint_index(self, driver, path, method):
        num_endpoints = APIPage.endpoint_list.get_immediate_child_count(driver)
        for i in range(1, num_endpoints+1):
            check_path = APIPage.path_by_index(i).get_text(driver)
            check_method = APIPage.type_by_index(i).get_text(driver)
            if check_path == path and check_method == method:
                return i
        return 0

    def toggle_endpoint(self, driver, path, method):
        endpoint_ind = self.endpoint_index(driver, path, method)
        APIPage.path_by_index(endpoint_ind).click(driver)

    def set_resource_id(self, driver, path, method, resource_id):
        endpoint_ind = self.endpoint_index(driver, path, method)
        APIPage.parameter_by_index(endpoint_ind).inject_text(driver, resource_id)

    def submit(self, driver, path, method):
        endpoint_ind = self.endpoint_index(driver, path, method)
        APIPage.submit(endpoint_ind).click(driver)
        time.sleep(HSAPI_GUI_RESPONSE)

    def response_code(self, driver, path, method):
        endpoint_ind = self.endpoint_index(driver, path, method)
        return APIPage.response_code(endpoint_ind).get_text(driver)


class Profile:
    def to_editor(self, driver):
        ProfilePage.edit.click(driver)

    def add_org(self, driver, org):
        ProfilePage.add_org.inject_text(driver, org)
        ProfilePage.add_org.inject_text(driver, Keys.ARROW_DOWN)
        ProfilePage.add_org.inject_text(driver, Keys.ENTER)

    def delete_org(self, driver, index):
        ProfilePage.delete_org(index).click(driver)

    def save(self, driver):
        ProfilePage.save.click(driver)


class Groups:
    def create_group(self, driver, name, purpose, about, privacy):
        GroupsPage.create_group.click(driver)
        NewGroupModal.name.inject_text(driver, name)
        NewGroupModal.purpose.inject_text(driver, purpose)
        NewGroupModal.about.inject_text(driver, about)
        if privacy.lower() == 'public':
            NewGroupModal.public.click(driver)
        elif privacy.lower() == 'discoverable':
            NewGroupModal.discoverable.click(driver)
        else:
            NewGroupModal.private.click(driver)
        NewGroupModal.submit.click(driver)


class Group:
    def check_title(self, driver):
        return GroupPage.name.get_text(driver)


class MyResources:
    def create_resource(self, driver, title):
        MyResourcesPage.create_new.click(driver)
        MyResourcesPage.title.click(driver)
        MyResourcesPage.title.inject_text(driver, title)
        MyResourcesPage.create_resource.click(driver)


Home = Home()
Apps = Apps()
Discover = Discover()
Resource = Resource()
Help = Help()
About = About()
API = API()
Profile = Profile()
Groups = Groups()
Group = Group()
MyResources = MyResources()
